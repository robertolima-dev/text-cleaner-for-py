import pytest
from text_cleaner_for_py.performance_cleaner import PerformanceTextCleaner

@pytest.fixture
def performance_cleaner():
    return PerformanceTextCleaner()

def test_clean_text_cached(performance_cleaner):
    # Testa se o cache está funcionando
    text = "Olá, mundo! 🧹✨"
    result1 = performance_cleaner.clean_text_cached(text)
    result2 = performance_cleaner.clean_text_cached(text)
    assert result1 == result2
    assert result1 == "ola mundo"

def test_clean_texts_parallel(performance_cleaner):
    # Testa processamento paralelo de múltiplos textos
    texts = [
        "Olá, mundo! 🧹✨",
        "Bem-vindo ao Text Cleaner!",
        "Teste de performance"
    ]
    results = performance_cleaner.clean_texts_parallel(texts)
    assert len(results) == 3
    assert results[0] == "ola mundo"
    assert results[1] == "bem vindo ao text cleaner"
    assert results[2] == "teste de performance"

def test_clean_large_text(performance_cleaner):
    # Testa limpeza de texto grande
    large_text = "Olá, mundo! " * 1000  # Cria um texto grande
    result = performance_cleaner.clean_large_text(large_text)
    assert "ola mundo" in result
    assert len(result) > 0

def test_clean_text_with_options(performance_cleaner):
    # Testa limpeza com opções específicas
    text = "Olá! 👋 Visite https://exemplo.com"
    options = {
        'remove_emojis': True,
        'remove_urls': True
    }
    result = performance_cleaner.clean_text_with_options(text, options)
    assert "👋" not in result
    assert "https://exemplo.com" not in result
    assert "ola" in result

def test_cache_invalidation(performance_cleaner):
    # Testa se o cache é invalidado corretamente com diferentes opções
    text = "Olá, mundo! 👋"
    
    # Primeira limpeza com opções padrão
    result1 = performance_cleaner.clean_text_with_options(text, {})
    
    # Segunda limpeza com opções diferentes
    result2 = performance_cleaner.clean_text_with_options(text, {'remove_emojis': True})
    
    assert result1 != result2
    assert "👋" in result1
    assert "👋" not in result2

def test_parallel_processing_with_empty_list(performance_cleaner):
    # Testa processamento paralelo com lista vazia
    results = performance_cleaner.clean_texts_parallel([])
    assert len(results) == 0

def test_clean_large_text_with_small_chunk_size(performance_cleaner):
    # Testa limpeza de texto grande com chunk size pequeno
    text = "Olá, mundo! " * 10
    result = performance_cleaner.clean_large_text(text, chunk_size=5)
    assert "ola mundo" in result
    assert len(result) > 0 