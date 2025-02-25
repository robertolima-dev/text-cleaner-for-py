import pytest
import sys
import os
from text_cleaner_for_py.cleaner_v1 import (
    normalize_text,
    remove_html_tags,
    clean_whitespace,
    filter_letters,
    filter_numbers,
    remove_stopwords,
)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def sample_text():
    return "<p>Olá, mundo! Este é um exemplo de texto com <b>HTML</b> e stopwords.</p>"


def test_normalize_text(sample_text):
    result = normalize_text(sample_text)
    expected = "ola mundo este e um exemplo de texto com html e stopwords"
    assert result == expected


def test_remove_html_tags(sample_text):
    result = remove_html_tags(sample_text)
    expected = "Olá, mundo! Este é um exemplo de texto com HTML e stopwords."
    assert result == expected


def test_clean_whitespace():
    texto = "Texto   com   espaços    e  \n \n quebras."
    result = clean_whitespace(texto)
    expected = "Texto com espaços e quebras."
    assert result == expected


def test_filter_letters():
    texto = "Texto 123 com #caracteres$ %especiais&*"
    result = filter_letters(texto)
    expected = "Texto com caracteres especiais"
    assert result == expected


def test_filter_numbers():
    texto = "Telefone: 123-456-789"
    result = filter_numbers(texto)
    expected = "123456789"
    assert result == expected


def test_remove_stopwords():
    texto = "Este é um texto simples para teste de stopwords."
    result = remove_stopwords(texto, language="portuguese")
    expected = "texto simples teste stopwords."
    assert result == expected


# 🏃 **Execução dos testes**
if __name__ == "__main__":
    pytest.main(["-v", "tests/test_cleaner_v1.py"])
