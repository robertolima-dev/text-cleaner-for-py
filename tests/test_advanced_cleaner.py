import pytest
from text_cleaner_for_py.advanced_cleaner import AdvancedTextCleaner

@pytest.fixture
def cleaner():
    return AdvancedTextCleaner()

def test_detect_language(cleaner):
    assert cleaner.detect_language("Olá, como vai você?") == "pt"
    assert cleaner.detect_language("Hello, how are you?") == "en"

def test_remove_emojis(cleaner):
    text = "Olá! 👋 Como vai você? 😊"
    assert cleaner.remove_emojis(text) == "Olá!  Como vai você? "

def test_remove_urls(cleaner):
    text = "Visite https://exemplo.com ou www.exemplo.org"
    assert cleaner.remove_urls(text) == "Visite  ou "

def test_remove_emails(cleaner):
    text = "Meu email é teste@exemplo.com"
    assert cleaner.remove_emails(text) == "Meu email é "

def test_normalize_numbers(cleaner):
    text = "1º lugar, 2º lugar, 3º lugar"
    assert cleaner.normalize_numbers(text) == "primeiro lugar, segundo lugar, terceiro lugar"

def test_normalize_dates(cleaner):
    text = "Data: 25/12/2023"
    assert "25 de dezembro de 2023" in cleaner.normalize_dates(text)

def test_normalize_currency(cleaner):
    text = "Preço: R$ 1.234,56"
    assert cleaner.normalize_currency(text) == "Preço: R$ 1.234,56"

def test_remove_typos(cleaner):
    text = "vc sabe pq isso aconteceu?"
    assert cleaner.remove_typos(text) == "você sabe porque isso aconteceu?"

def test_remove_duplicate_text(cleaner):
    text = "texto texto repetido repetido"
    assert cleaner.remove_duplicate_text(text) == "texto repetido"

def test_normalize_abbreviations(cleaner):
    text = "Dr. Silva e Dra. Santos"
    assert cleaner.normalize_abbreviations(text) == "Doutor Silva e Doutora Santos"

def test_stem_text(cleaner):
    text = "correndo pulando saltando"
    stemmed = cleaner.stem_text(text)
    assert "corr" in stemmed
    assert "pul" in stemmed
    assert "salt" in stemmed

def test_lemmatize_text(cleaner):
    text = "correndo pulando saltando"
    lemmatized = cleaner.lemmatize_text(text)
    assert "correr" in lemmatized
    assert "pular" in lemmatized
    assert "saltar" in lemmatized

def test_clean_advanced(cleaner):
    text = "Olá! 👋 Visite https://exemplo.com ou envie email para teste@exemplo.com. Data: 25/12/2023. Preço: R$ 1.234,56. vc sabe pq?"
    cleaned = cleaner.clean_advanced(text)
    assert "👋" not in cleaned
    assert "https://exemplo.com" not in cleaned
    assert "teste@exemplo.com" not in cleaned
    assert "25 de dezembro" in cleaned and "2023" in cleaned
    assert "R$ 1.234,56" in cleaned
    assert "você" in cleaned
    assert "porque" in cleaned

def test_clean_advanced_with_options(cleaner):
    text = "Olá! 👋 Visite https://exemplo.com"
    options = {
        'remove_emojis': True,
        'remove_urls': False,
        'remove_emails': True,
        'normalize_numbers': False,
        'normalize_dates': False,
        'normalize_currency': False,
        'remove_typos': False,
        'remove_duplicates': False,
        'normalize_abbreviations': False,
        'stem': False,
        'lemmatize': False
    }
    cleaned = cleaner.clean_advanced(text, options)
    assert "👋" not in cleaned
    assert "https://exemplo.com" in cleaned 