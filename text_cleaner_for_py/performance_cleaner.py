import asyncio
import concurrent.futures
from functools import lru_cache
import re
from typing import List, Optional, Dict, Any
import torch
import redis
from text_cleaner_for_py.cleaner import clean_text

class PerformanceTextCleaner:
    def __init__(self, max_workers: int = 4, cache_size: int = 1000):
        self.max_workers = max_workers
        self._cache = {}
        self.cache_size = cache_size
        self._redis_client = None

    def clean_texts_parallel(self, texts: List[str]) -> List[str]:
        """Processa múltiplos textos em paralelo."""
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            return list(executor.map(clean_text, texts))

    def clean_large_text(self, text: str, chunk_size: int = 1000) -> str:
        """Processa um texto grande dividindo em chunks."""
        chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
        cleaned_chunks = self.clean_texts_parallel(chunks)
        return " ".join(cleaned_chunks)

    @lru_cache(maxsize=1000)
    def clean_text_cached(self, text: str) -> str:
        """Limpa o texto usando cache local."""
        return clean_text(text)

    def remove_ocr_noise(self, text: str) -> str:
        """Remove ruído comum em textos de OCR."""
        # Substitui números por letras comuns em OCR
        ocr_replacements = {
            '0': 'o', '1': 'i', '3': 'e', '4': 'a', '5': 's',
            '7': 't', '8': 'b', '9': 'g'
        }
        for num, letter in ocr_replacements.items():
            text = text.replace(num, letter)
        return text

    def normalize_measurements(self, text: str) -> str:
        """Normaliza unidades de medida no texto."""
        # Padrões comuns de medidas
        patterns = {
            r'(\d+(?:\.\d+)?)\s*kg': r'\1 quilogramas',
            r'(\d+(?:\.\d+)?)\s*m': r'\1 metros',
            r'(\d+(?:\.\d+)?)\s*cm': r'\1 centímetros',
            r'(\d+(?:\.\d+)?)\s*l': r'\1 litros',
            r'(\d+(?:\.\d+)?)\s*ml': r'\1 mililitros'
        }
        
        for pattern, replacement in patterns.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        return text

    def remove_duplicates(self, text: str) -> str:
        """Remove conteúdo duplicado no texto, considerando frases e sentenças."""
        # Divide por pontuação de fim de frase
        import string
        import re
        # Divide por ! ? .
        sentences = re.split(r'[.!?]', text)
        unique_sentences = []
        seen = set()
        for sentence in sentences:
            sentence = sentence.strip()
            if sentence and sentence not in seen:
                seen.add(sentence)
                unique_sentences.append(sentence)
        return '. '.join(unique_sentences) + ('.' if unique_sentences else '')

    def normalize_proper_names(self, text: str) -> str:
        """Normaliza nomes próprios no texto."""
        def capitalize_name(name):
            words = name.split()
            result = []
            for i, word in enumerate(words):
                if i == 0 or word.lower() not in ['da', 'de', 'do', 'das', 'dos', 'e']:
                    result.append(word.capitalize())
                else:
                    result.append(word.lower())
            return ' '.join(result)
        
        # Padrão para nomes próprios
        pattern = r'\b([a-zà-ú]+(?:\s+(?:da|de|do|das|dos|e)\s+[a-zà-ú]+)*)\b'
        
        def replace_name(match):
            return capitalize_name(match.group(1))
        
        return re.sub(pattern, replace_name, text, flags=re.IGNORECASE)

    async def clean_texts_async(self, texts: List[str]) -> List[str]:
        """Processa textos de forma assíncrona."""
        async def clean_single_text(text):
            return clean_text(text)
        
        tasks = [clean_single_text(text) for text in texts]
        return await asyncio.gather(*tasks)

    def is_gpu_available(self) -> bool:
        """Verifica se GPU está disponível."""
        return torch.cuda.is_available()

    def clean_text_gpu(self, text: str) -> str:
        """Processa texto usando GPU se disponível."""
        if not self.is_gpu_available():
            return clean_text(text)
        
        # Implementação básica de processamento GPU
        # Em um caso real, você usaria operações vetorizadas do PyTorch
        return clean_text(text)

    def is_redis_available(self) -> bool:
        """Verifica se Redis está disponível."""
        try:
            if self._redis_client is None:
                self._redis_client = redis.Redis(host='localhost', port=6379, db=0)
            self._redis_client.ping()
            return True
        except:
            return False

    def clean_text_distributed_cache(self, text: str) -> str:
        """Limpa texto usando cache distribuído (Redis)."""
        if not self.is_redis_available():
            return clean_text(text)
        
        cache_key = f"text_cleaner:{hash(text)}"
        cached_result = self._redis_client.get(cache_key)
        
        if cached_result:
            return cached_result.decode('utf-8')
        
        cleaned_text = clean_text(text)
        self._redis_client.set(cache_key, cleaned_text)
        return cleaned_text

    def clean_text_with_options(self, text: str, options: Dict[str, bool]) -> str:
        """Limpa texto com opções específicas."""
        result = text
        
        if options.get('remove_emojis', False):
            result = re.sub(r'[^\w\s-]', '', result)
        
        if options.get('remove_urls', False):
            result = re.sub(r'https?://\S+', '', result)
        
        return clean_text(result) 