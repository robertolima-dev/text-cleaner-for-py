import pytest
import asyncio
from text_cleaner_for_py.performance_cleaner import PerformanceTextCleaner

@pytest.fixture
def cleaner():
    return PerformanceTextCleaner()

def test_parallel_text_processing(cleaner):
    texts = [
        "Olá, mundo! 🧹✨",
        "Bem-vindo ao Text Cleaner!",
        "Teste de performance"
    ]
    cleaned_texts = cleaner.clean_texts_parallel(texts)
    assert len(cleaned_texts) == 3
    assert all(isinstance(text, str) for text in cleaned_texts)
    assert "🧹" not in cleaned_texts[0]

def test_large_text_processing(cleaner):
    large_text = "Olá, mundo! " * 1000
    cleaned_text = cleaner.clean_large_text(large_text, chunk_size=1000)
    assert isinstance(cleaned_text, str)
    assert len(cleaned_text) > 0

def test_text_caching(cleaner):
    text = "Olá, mundo! 🧹✨"
    result1 = cleaner.clean_text_cached(text)
    result2 = cleaner.clean_text_cached(text)
    assert result1 == result2

def test_ocr_noise_removal(cleaner):
    text = "H3ll0 W0rld! Th1s 1s 4 t3st."
    cleaned = cleaner.remove_ocr_noise(text)
    assert "H3ll0" not in cleaned
    assert "Hello" in cleaned

def test_measurement_normalization(cleaner):
    text = "O produto pesa 1.5kg e mede 2.5m"
    normalized = cleaner.normalize_measurements(text)
    assert "1.5kg" not in normalized
    assert "1.5 quilogramas" in normalized
    assert "2.5m" not in normalized
    assert "2.5 metros" in normalized

def test_duplicate_content_removal(cleaner):
    text = "Olá mundo! Olá mundo! Como vai você?"
    cleaned = cleaner.remove_duplicates(text)
    # Verifica se não há duplicatas consecutivas
    sentences = cleaned.split('.')
    sentences = [s.strip() for s in sentences if s.strip()]
    assert len(sentences) == 2  # Deve ter apenas duas frases únicas

def test_proper_name_normalization(cleaner):
    text = "joão da silva e maria santos"
    normalized = cleaner.normalize_proper_names(text)
    # Verifica se os nomes foram capitalizados corretamente
    assert "João da Silva" in normalized
    assert "Maria Santos" in normalized
    # Verifica se as preposições foram mantidas em minúsculo
    assert "da" in normalized.lower()
    assert "e" in normalized.lower()

@pytest.mark.asyncio
async def test_async_text_processing(cleaner):
    texts = [
        "Olá, mundo! 🧹✨",
        "Bem-vindo ao Text Cleaner!",
        "Teste de performance"
    ]
    cleaned_texts = await cleaner.clean_texts_async(texts)
    assert len(cleaned_texts) == 3
    assert all(isinstance(text, str) for text in cleaned_texts)

def test_gpu_processing(cleaner):
    if not cleaner.is_gpu_available():
        pytest.skip("GPU not available")
    
    large_text = "Olá, mundo! " * 10000
    cleaned_text = cleaner.clean_text_gpu(large_text)
    assert isinstance(cleaned_text, str)
    assert len(cleaned_text) > 0

def test_distributed_cache(cleaner):
    if not cleaner.is_redis_available():
        pytest.skip("Redis not available")
    
    text = "Olá, mundo! 🧹✨"
    result1 = cleaner.clean_text_distributed_cache(text)
    result2 = cleaner.clean_text_distributed_cache(text)
    assert result1 == result2

def test_clean_text_with_options(cleaner):
    text = "Olá! 👋 Visite https://exemplo.com"
    options = {
        'remove_emojis': True,
        'remove_urls': True
    }
    cleaned_text = cleaner.clean_text_with_options(text, options)
    assert "👋" not in cleaned_text
    assert "https://exemplo.com" not in cleaned_text

def test_cache_invalidation(cleaner):
    text = "Teste de cache"
    result1 = cleaner.clean_text_cached(text)
    # Força invalidação do cache
    cleaner.clean_text_cached.cache_clear()
    result2 = cleaner.clean_text_cached(text)
    assert result1 == result2

def test_parallel_processing_with_empty_list(cleaner):
    texts = []
    cleaned_texts = cleaner.clean_texts_parallel(texts)
    assert len(cleaned_texts) == 0

def test_clean_large_text_with_small_chunk_size(cleaner):
    large_text = "Olá, mundo! " * 1000
    cleaned_text = cleaner.clean_large_text(large_text, chunk_size=10)
    assert isinstance(cleaned_text, str)
    assert len(cleaned_text) > 0 