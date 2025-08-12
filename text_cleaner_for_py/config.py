"""
Configurações centralizadas para o text_cleaner_for_py.

Este módulo define todas as configurações padrão e permite
personalização através de variáveis de ambiente ou arquivos de configuração.
"""

import os
from typing import Dict, List, Optional, Union
from dataclasses import dataclass, field

from .exceptions import ConfigurationError


@dataclass
class CleanerConfig:
    """Configurações para o processamento de texto."""
    
    # Configurações de limpeza
    remove_html: bool = True
    remove_accents: bool = True
    remove_special_chars: bool = True
    remove_extra_spaces: bool = True
    remove_emojis: bool = False
    remove_urls: bool = False
    remove_emails: bool = False
    
    # Configurações de normalização
    normalize_dates: bool = False
    normalize_numbers: bool = False
    normalize_measurements: bool = False
    normalize_proper_names: bool = False
    
    # Configurações de processamento
    default_case: str = "lower"
    supported_cases: List[str] = field(default_factory=lambda: [
        "lower", "upper", "title", "snake", "camel", "pascal"
    ])
    
    # Configurações de idioma
    default_language: str = "pt"
    supported_languages: List[str] = field(default_factory=lambda: [
        "pt", "en", "es", "fr", "de", "it"
    ])
    
    # Configurações de cache
    enable_cache: bool = True
    cache_ttl: int = 3600  # segundos
    max_cache_size: int = 1000
    
    # Configurações de performance
    max_workers: int = 4
    chunk_size: int = 1000
    enable_gpu: bool = False
    
    def validate(self) -> None:
        """Valida as configurações."""
        if self.default_case not in self.supported_cases:
            raise ConfigurationError(
                "default_case", 
                self.default_case, 
                f"Deve ser um dos valores suportados: {', '.join(self.supported_cases)}"
            )
        
        if self.default_language not in self.supported_languages:
            raise ConfigurationError(
                "default_language", 
                self.default_language, 
                f"Deve ser um dos idiomas suportados: {', '.join(self.supported_languages)}"
            )
        
        if self.max_workers < 1:
            raise ConfigurationError(
                "max_workers", 
                self.max_workers, 
                "Deve ser maior que 0"
            )
        
        if self.chunk_size < 1:
            raise ConfigurationError(
                "chunk_size", 
                self.chunk_size, 
                "Deve ser maior que 0"
            )


@dataclass
class RedisConfig:
    """Configurações para conexão com Redis."""
    
    host: str = "localhost"
    port: int = 6379
    db: int = 0
    password: Optional[str] = None
    ssl: bool = False
    timeout: int = 5
    
    def get_connection_params(self) -> Dict[str, Union[str, int, bool]]:
        """Retorna parâmetros de conexão para o Redis."""
        params = {
            "host": self.host,
            "port": self.port,
            "db": self.db,
            "ssl": self.ssl,
            "socket_timeout": self.timeout,
            "socket_connect_timeout": self.timeout
        }
        
        if self.password:
            params["password"] = self.password
            
        return params


@dataclass
class LoggingConfig:
    """Configurações para logging."""
    
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file: Optional[str] = None
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    backup_count: int = 5
    
    def validate(self) -> None:
        """Valida as configurações de logging."""
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if self.level.upper() not in valid_levels:
            raise ConfigurationError(
                "level", 
                self.level, 
                f"Deve ser um dos níveis válidos: {', '.join(valid_levels)}"
            )


class ConfigManager:
    """Gerenciador de configurações centralizado."""
    
    def __init__(self) -> None:
        """Inicializa o gerenciador de configurações."""
        self.cleaner = CleanerConfig()
        self.redis = RedisConfig()
        self.logging = LoggingConfig()
        
        self._load_from_environment()
        self._validate_all()
    
    def _load_from_environment(self) -> None:
        """Carrega configurações das variáveis de ambiente."""
        # Configurações do cleaner
        if os.getenv("TEXT_CLEANER_REMOVE_HTML"):
            self.cleaner.remove_html = os.getenv("TEXT_CLEANER_REMOVE_HTML").lower() == "true"
        
        if os.getenv("TEXT_CLEANER_DEFAULT_CASE"):
            self.cleaner.default_case = os.getenv("TEXT_CLEANER_DEFAULT_CASE")
        
        if os.getenv("TEXT_CLEANER_DEFAULT_LANGUAGE"):
            self.cleaner.default_language = os.getenv("TEXT_CLEANER_DEFAULT_LANGUAGE")
        
        if os.getenv("TEXT_CLEANER_MAX_WORKERS"):
            self.cleaner.max_workers = int(os.getenv("TEXT_CLEANER_MAX_WORKERS"))
        
        # Configurações do Redis
        if os.getenv("TEXT_CLEANER_REDIS_HOST"):
            self.redis.host = os.getenv("TEXT_CLEANER_REDIS_HOST")
        
        if os.getenv("TEXT_CLEANER_REDIS_PORT"):
            self.redis.port = int(os.getenv("TEXT_CLEANER_REDIS_PORT"))
        
        if os.getenv("TEXT_CLEANER_REDIS_PASSWORD"):
            self.redis.password = os.getenv("TEXT_CLEANER_REDIS_PASSWORD")
        
        # Configurações de logging
        if os.getenv("TEXT_CLEANER_LOG_LEVEL"):
            self.logging.level = os.getenv("TEXT_CLEANER_LOG_LEVEL")
    
    def _validate_all(self) -> None:
        """Valida todas as configurações."""
        self.cleaner.validate()
        self.logging.validate()
    
    def get_cleaner_config(self) -> CleanerConfig:
        """Retorna as configurações do cleaner."""
        return self.cleaner
    
    def get_redis_config(self) -> RedisConfig:
        """Retorna as configurações do Redis."""
        return self.redis
    
    def get_logging_config(self) -> LoggingConfig:
        """Retorna as configurações de logging."""
        return self.logging
    
    def update_cleaner_config(self, **kwargs) -> None:
        """Atualiza configurações do cleaner."""
        for key, value in kwargs.items():
            if hasattr(self.cleaner, key):
                setattr(self.cleaner, key, value)
            else:
                raise ConfigurationError(
                    key, 
                    value, 
                    f"Configuração '{key}' não existe no CleanerConfig"
                )
        
        self.cleaner.validate()
    
    def to_dict(self) -> Dict[str, Dict]:
        """Converte todas as configurações para dicionário."""
        return {
            "cleaner": self.cleaner.__dict__,
            "redis": self.redis.__dict__,
            "logging": self.logging.__dict__
        }


# Instância global de configuração
config = ConfigManager()
