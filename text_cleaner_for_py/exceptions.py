"""
Exceções customizadas para o text_cleaner_for_py.

Este módulo define exceções específicas para diferentes tipos de erros
que podem ocorrer durante o processamento de texto.
"""

from typing import Any, Optional


class TextCleanerError(Exception):
    """Exceção base para todos os erros do text_cleaner_for_py."""
    
    def __init__(self, message: str, details: Optional[Any] = None) -> None:
        """
        Inicializa a exceção.
        
        Args:
            message: Mensagem de erro
            details: Detalhes adicionais sobre o erro
        """
        super().__init__(message)
        self.message = message
        self.details = details
    
    def __str__(self) -> str:
        """Retorna a representação string da exceção."""
        if self.details:
            return f"{self.message} (Detalhes: {self.details})"
        return self.message


class ValidationError(TextCleanerError):
    """Exceção para erros de validação de entrada."""
    
    def __init__(self, field: str, value: Any, expected_type: str) -> None:
        """
        Inicializa a exceção de validação.
        
        Args:
            field: Nome do campo com erro
            value: Valor inválido
            expected_type: Tipo esperado
        """
        message = f"Campo '{field}' deve ser do tipo {expected_type}, recebeu {type(value).__name__}: {value}"
        super().__init__(message, {"field": field, "value": value, "expected_type": expected_type})


class ConfigurationError(TextCleanerError):
    """Exceção para erros de configuração."""
    
    def __init__(self, config_key: str, config_value: Any, reason: str) -> None:
        """
        Inicializa a exceção de configuração.
        
        Args:
            config_key: Chave de configuração com erro
            config_value: Valor da configuração
            reason: Motivo do erro
        """
        message = f"Configuração inválida para '{config_key}': {config_value}. {reason}"
        super().__init__(message, {"config_key": config_key, "config_value": config_value, "reason": reason})


class ProcessingError(TextCleanerError):
    """Exceção para erros durante o processamento de texto."""
    
    def __init__(self, operation: str, text: str, reason: str) -> None:
        """
        Inicializa a exceção de processamento.
        
        Args:
            operation: Operação que falhou
            text: Texto que estava sendo processado
            reason: Motivo da falha
        """
        message = f"Erro durante '{operation}': {reason}"
        super().__init__(message, {"operation": operation, "text": text, "reason": reason})


class UnsupportedFormatError(TextCleanerError):
    """Exceção para formatos não suportados."""
    
    def __init__(self, format_name: str, supported_formats: list[str]) -> None:
        """
        Inicializa a exceção de formato não suportado.
        
        Args:
            format_name: Formato não suportado
            supported_formats: Lista de formatos suportados
        """
        message = f"Formato '{format_name}' não é suportado. Formatos suportados: {', '.join(supported_formats)}"
        super().__init__(message, {"format_name": format_name, "supported_formats": supported_formats})


class LanguageNotSupportedError(TextCleanerError):
    """Exceção para idiomas não suportados."""
    
    def __init__(self, language: str, supported_languages: list[str]) -> None:
        """
        Inicializa a exceção de idioma não suportado.
        
        Args:
            language: Idioma não suportado
            supported_languages: Lista de idiomas suportados
        """
        message = f"Idioma '{language}' não é suportado. Idiomas suportados: {', '.join(supported_languages)}"
        super().__init__(message, {"language": language, "supported_languages": supported_languages})


class FileProcessingError(TextCleanerError):
    """Exceção para erros no processamento de arquivos."""
    
    def __init__(self, file_path: str, operation: str, reason: str) -> None:
        """
        Inicializa a exceção de processamento de arquivo.
        
        Args:
            file_path: Caminho do arquivo
            operation: Operação que falhou
            reason: Motivo da falha
        """
        message = f"Erro ao processar arquivo '{file_path}' durante '{operation}': {reason}"
        super().__init__(message, {"file_path": file_path, "operation": operation, "reason": reason})


class CacheError(TextCleanerError):
    """Exceção para erros relacionados ao cache."""
    
    def __init__(self, operation: str, reason: str) -> None:
        """
        Inicializa a exceção de cache.
        
        Args:
            operation: Operação de cache que falhou
            reason: Motivo da falha
        """
        message = f"Erro no cache durante '{operation}': {reason}"
        super().__init__(message, {"operation": operation, "reason": reason})


class PerformanceError(TextCleanerError):
    """Exceção para erros de performance."""
    
    def __init__(self, operation: str, reason: str, performance_metrics: Optional[dict] = None) -> None:
        """
        Inicializa a exceção de performance.
        
        Args:
            operation: Operação que falhou
            reason: Motivo da falha
            performance_metrics: Métricas de performance (opcional)
        """
        message = f"Erro de performance durante '{operation}': {reason}"
        super().__init__(message, {"operation": operation, "reason": reason, "performance_metrics": performance_metrics})
