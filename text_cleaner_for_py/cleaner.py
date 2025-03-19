import re
import unicodedata

from bs4 import BeautifulSoup


# 🔡 Remover acentos e normalizar texto
def remove_accents(text: str) -> str:
    """Remove acentos do texto."""
    nfkd_form = unicodedata.normalize('NFKD', text)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


# ✂ Remover caracteres especiais
def remove_special_characters(text: str) -> str:
    """Remove caracteres especiais do texto."""
    return re.sub(r'[^\w\s]', '', text)


# 🔄 Converter para snake_case
def to_snake_case(text: str) -> str:
    """Converte texto para snake_case."""
    text = remove_accents(text)
    text = re.sub(r'\s+', '_', text.strip().lower())
    return re.sub(r'[^a-z0-9_]', '', text)


# 🔄 Converter para camelCase
def to_camel_case(text: str) -> str:
    """Converte texto para camelCase."""
    text = to_snake_case(text)
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


# 🔄 Converter para PascalCase
def to_pascal_case(text: str) -> str:
    """Converte texto para PascalCase."""
    return ''.join(word.capitalize() for word in to_snake_case(text).split('_')) # noqa501


# 🌐 Remover HTML
def remove_html(text: str) -> str:
    """Remove tags HTML do texto."""
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text(separator=' ', strip=True)


# 🔍 Remover múltiplos espaços
def remove_extra_spaces(text: str) -> str:
    """Remove espaços extras do texto."""
    return re.sub(r'\s+', ' ', text).strip()


# 🧹 Limpeza completa do texto
def clean_text(text: str, case: str = 'lower') -> str:
    """
    Limpeza completa do texto:
    - Remove HTML
    - Remove acentos
    - Remove caracteres especiais
    - Normaliza espaços
    - Converte o texto para o formato especificado
    """
    text = remove_html(text)
    text = remove_accents(text)
    text = remove_special_characters(text)
    text = remove_extra_spaces(text)

    if case == 'lower':
        return text.lower()
    elif case == 'upper':
        return text.upper()
    elif case == 'title':
        return text.title()
    elif case == 'snake':
        return to_snake_case(text)
    elif case == 'camel':
        return to_camel_case(text)
    elif case == 'pascal':
        return to_pascal_case(text)
    else:
        raise ValueError("⚠️ Formato de case inválido. Use: lower, upper, title, snake, camel ou pascal.") # noqa501


# __init__.py
__version__ = "0.1.0"
__all__ = [
    "remove_accents",
    "remove_special_characters",
    "to_snake_case",
    "to_camel_case",
    "to_pascal_case",
    "remove_html",
    "remove_extra_spaces",
    "clean_text",
]
