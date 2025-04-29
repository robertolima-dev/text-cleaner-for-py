import multiprocessing
from functools import lru_cache
from typing import List, Optional
from concurrent.futures import ProcessPoolExecutor
import re
import unicodedata

from .cleaner import clean_text
from .advanced_cleaner import AdvancedTextCleaner

class PerformanceTextCleaner:
    def __init__(self, max_workers: Optional[int] = None):
        """
        Inicializa o limpeza de texto com performance otimizada.
        
        Args:
            max_workers: Número máximo de workers para processamento paralelo.
                        Se None, usa o número de CPUs disponíveis.
        """
        self.max_workers = max_workers or multiprocessing.cpu_count()
        self.advanced_cleaner = AdvancedTextCleaner()
    
    def _remove_accents(self, text: str) -> str:
        """
        Remove acentos do texto.
        
        Args:
            text: Texto com acentos
            
        Returns:
            Texto sem acentos
        """
        return ''.join(c for c in unicodedata.normalize('NFD', text)
                      if unicodedata.category(c) != 'Mn')
    
    @lru_cache(maxsize=128)
    def clean_text_cached(self, text: str) -> str:
        """
        Versão com cache da limpeza de texto.
        
        Args:
            text: Texto a ser limpo
            
        Returns:
            Texto limpo
        """
        # Converte para minúsculas e remove acentos
        text = text.lower()
        text = self._remove_accents(text)
        # Remove emojis e caracteres especiais
        text = re.sub(r'[^\w\s-]', '', text)
        # Substitui hífens por espaços
        text = text.replace('-', ' ')
        # Remove espaços extras
        text = ' '.join(text.split())
        return text
    
    def clean_texts_parallel(self, texts: List[str]) -> List[str]:
        """
        Limpa múltiplos textos em paralelo.
        
        Args:
            texts: Lista de textos a serem limpos
            
        Returns:
            Lista de textos limpos
        """
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(self.clean_text_cached, texts))
    
    def clean_large_text(self, text: str, chunk_size: int = 1000) -> str:
        """
        Limpa um texto grande dividindo-o em chunks e processando em paralelo.
        
        Args:
            text: Texto grande a ser limpo
            chunk_size: Tamanho de cada chunk em caracteres
            
        Returns:
            Texto limpo
        """
        # Divide o texto em chunks
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        
        # Processa os chunks em paralelo
        cleaned_chunks = self.clean_texts_parallel(chunks)
        
        # Junta os chunks limpos
        return ''.join(cleaned_chunks)
    
    def clean_text_with_options(self, text: str, options: dict) -> str:
        """
        Limpa texto com opções específicas usando cache.
        
        Args:
            text: Texto a ser limpo
            options: Dicionário com opções de limpeza
            
        Returns:
            Texto limpo
        """
        # Cria uma chave única para o cache baseada nas opções
        cache_key = f"{text}_{str(sorted(options.items()))}"
        
        @lru_cache(maxsize=128)
        def _clean_with_options(key: str) -> str:
            result = text.lower()
            result = self._remove_accents(result)
            if options.get('remove_emojis', False):
                result = re.sub(r'[^\w\s-]', '', result)
                result = result.replace('-', ' ')
            if options.get('remove_urls', False):
                result = re.sub(r'https?://\S+', '', result)
            return ' '.join(result.split())
        
        return _clean_with_options(cache_key) 