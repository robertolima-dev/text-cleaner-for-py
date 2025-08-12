"""
Sistema de logging estruturado para o text_cleaner_for_py.

Este módulo fornece um sistema de logging configurável e estruturado
para monitorar o funcionamento da biblioteca.
"""

import logging
import logging.handlers
import sys
from pathlib import Path
from typing import Optional

from .config import config
from .exceptions import ConfigurationError


class ColoredFormatter(logging.Formatter):
    """Formatador de log com cores para terminal."""
    
    # Cores ANSI
    COLORS = {
        'DEBUG': '\033[36m',      # Cyan
        'INFO': '\033[32m',       # Green
        'WARNING': '\033[33m',    # Yellow
        'ERROR': '\033[31m',      # Red
        'CRITICAL': '\033[35m',   # Magenta
        'RESET': '\033[0m'        # Reset
    }
    
    def format(self, record: logging.LogRecord) -> str:
        """Formata o registro de log com cores."""
        # Adiciona cor ao nível do log
        level_color = self.COLORS.get(record.levelname, '')
        reset_color = self.COLORS['RESET']
        
        # Formata a mensagem
        formatted = super().format(record)
        
        # Adiciona cores se estiver no terminal
        if hasattr(sys.stderr, 'isatty') and sys.stderr.isatty():
            formatted = f"{level_color}{formatted}{reset_color}"
        
        return formatted


class StructuredFormatter(logging.Formatter):
    """Formatador de log estruturado para arquivos."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Formata o registro de log de forma estruturada."""
        # Informações básicas
        log_entry = {
            'timestamp': self.formatTime(record),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        
        # Adiciona exceção se houver
        if record.exc_info:
            log_entry['exception'] = self.formatException(record.exc_info)
        
        # Adiciona campos extras se houver
        if hasattr(record, 'extra_fields'):
            log_entry.update(record.extra_fields)
        
        # Formata como JSON-like (simplificado)
        formatted_parts = []
        for key, value in log_entry.items():
            if isinstance(value, str):
                formatted_parts.append(f"{key}='{value}'")
            else:
                formatted_parts.append(f"{key}={value}")
        
        return " | ".join(formatted_parts)


class TextCleanerLogger:
    """Logger principal para o text_cleaner_for_py."""
    
    def __init__(self, name: str = "text_cleaner_for_py") -> None:
        """
        Inicializa o logger.
        
        Args:
            name: Nome do logger
        """
        self.name = name
        self.logger = logging.getLogger(name)
        self._setup_logger()
    
    def _setup_logger(self) -> None:
        """Configura o logger com handlers e formatadores."""
        # Remove handlers existentes
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        
        # Configura o nível do logger
        log_config = config.get_logging_config()
        self.logger.setLevel(getattr(logging, log_config.level.upper()))
        
        # Handler para console com cores
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = ColoredFormatter(
            fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)
        
        # Handler para arquivo se configurado
        if log_config.file:
            self._setup_file_handler(log_config)
        
        # Não propaga para o logger raiz
        self.logger.propagate = False
    
    def _setup_file_handler(self, log_config) -> None:
        """Configura o handler para arquivo."""
        try:
            file_path = Path(log_config.file)
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Handler rotativo para arquivo
            file_handler = logging.handlers.RotatingFileHandler(
                filename=file_path,
                maxBytes=log_config.max_file_size,
                backupCount=log_config.backup_count,
                encoding='utf-8'
            )
            
            file_formatter = StructuredFormatter(
                fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )
            file_handler.setFormatter(file_formatter)
            
            self.logger.addHandler(file_handler)
            
        except Exception as e:
            # Se não conseguir configurar o arquivo, loga o erro mas não falha
            self.logger.warning(f"Não foi possível configurar logging para arquivo: {e}")
    
    def debug(self, message: str, **kwargs) -> None:
        """Log de debug."""
        self._log_with_extra(logging.DEBUG, message, **kwargs)
    
    def info(self, message: str, **kwargs) -> None:
        """Log de informação."""
        self._log_with_extra(logging.INFO, message, **kwargs)
    
    def warning(self, message: str, **kwargs) -> None:
        """Log de aviso."""
        self._log_with_extra(logging.WARNING, message, **kwargs)
    
    def error(self, message: str, **kwargs) -> None:
        """Log de erro."""
        self._log_with_extra(logging.ERROR, message, **kwargs)
    
    def critical(self, message: str, **kwargs) -> None:
        """Log crítico."""
        self._log_with_extra(logging.CRITICAL, message, **kwargs)
    
    def _log_with_extra(self, level: int, message: str, **kwargs) -> None:
        """Log com campos extras."""
        if kwargs:
            # Cria um registro com campos extras
            extra = {'extra_fields': kwargs}
            self.logger.log(level, message, extra=extra)
        else:
            self.logger.log(level, message)
    
    def log_operation(self, operation: str, text: str, result: str, **kwargs) -> None:
        """
        Log específico para operações de limpeza de texto.
        
        Args:
            operation: Nome da operação realizada
            text: Texto de entrada
            result: Resultado da operação
            **kwargs: Campos extras para o log
        """
        extra_fields = {
            'operation': operation,
            'input_length': len(text),
            'output_length': len(result),
            'compression_ratio': len(result) / len(text) if len(text) > 0 else 0,
            **kwargs
        }
        
        self.info(f"Operação '{operation}' concluída", **extra_fields)
    
    def log_error(self, operation: str, error: Exception, text: str = "", **kwargs) -> None:
        """
        Log específico para erros.
        
        Args:
            operation: Nome da operação que falhou
            error: Exceção que ocorreu
            text: Texto que estava sendo processado (opcional)
            **kwargs: Campos extras para o log
        """
        extra_fields = {
            'operation': operation,
            'error_type': type(error).__name__,
            'error_message': str(error),
            'input_length': len(text) if text else 0,
            **kwargs
        }
        
        self.error(f"Erro durante '{operation}': {error}", **extra_fields)
    
    def log_performance(self, operation: str, duration: float, **kwargs) -> None:
        """
        Log específico para métricas de performance.
        
        Args:
            operation: Nome da operação
            duration: Duração em segundos
            **kwargs: Campos extras para o log
        """
        extra_fields = {
            'operation': operation,
            'duration_seconds': duration,
            'duration_ms': duration * 1000,
            **kwargs
        }
        
        if duration > 1.0:
            self.warning(f"Operação '{operation}' demorou {duration:.2f}s", **extra_fields)
        else:
            self.debug(f"Operação '{operation}' concluída em {duration:.3f}s", **extra_fields)


# Logger global
logger = TextCleanerLogger()


def get_logger(name: str = None) -> TextCleanerLogger:
    """
    Retorna um logger configurado.
    
    Args:
        name: Nome do logger (opcional)
        
    Returns:
        Logger configurado
    """
    if name:
        return TextCleanerLogger(name)
    return logger
