# 📦 text_cleaner/cleaner_v1.py

import re
import unicodedata

import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords

# 📥 Garantir que o corpus de stopwords está disponível
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


def normalize_text(text: str) -> str:
    """🔡 Converte texto para minúsculas e remove acentos e caracteres especiais (após remover HTML).""" # noqa501
    text = remove_html_tags(text)
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8') # noqa501
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return clean_whitespace(text)


def remove_html_tags(text: str) -> str:
    """🧹 Remove tags HTML do texto."""
    return BeautifulSoup(text, "html.parser").get_text()


def clean_whitespace(text: str) -> str:
    """🧹 Remove espaços em excesso e quebras de linha."""
    return re.sub(r'\s+', ' ', text).strip()


def filter_letters(text: str) -> str:
    """🔍 Mantém apenas letras no texto."""
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return clean_whitespace(text)


def filter_numbers(text: str) -> str:
    """🔍 Mantém apenas números no texto."""
    return re.sub(r'[^0-9]', '', text)


def remove_stopwords(text: str, language: str = 'portuguese') -> str:
    """🔍 Remove stopwords do texto com base no idioma especificado."""
    stop_words = set(stopwords.words(language))
    words = text.split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    return ' '.join(filtered_words)


# 🌟 Exemplo de uso
if __name__ == "__main__":
    sample_text = "<p>Olá, mundo! Este é um exemplo de texto com <b>HTML</b> e stopwords.</p>" # noqa501
    print("Original:", sample_text)
    print("Normalizado:", normalize_text(sample_text))
    print("Sem HTML:", remove_html_tags(sample_text))
    print("Espaços limpos:", clean_whitespace(sample_text))
    print("Somente letras:", filter_letters(sample_text))
    print("Somente números:", filter_numbers("Telefone: 123-456-789"))
    print("Sem stopwords:", remove_stopwords(sample_text, language='portuguese')) # noqa501
    print("Sem stopwords:", remove_stopwords(sample_text, language='portuguese')) # noqa501
