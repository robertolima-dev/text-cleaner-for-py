import re
import unicodedata
from typing import Literal, Union

from bs4 import BeautifulSoup
from .exceptions import ValidationError, UnsupportedFormatError


# 🔡 Remover acentos e normalizar texto
def remove_accents(text: str) -> str:
    """
    Remove acentos do texto.
    
    Args:
        text: Texto de entrada com acentos
        
    Returns:
        Texto sem acentos
        
    Examples:
        >>> remove_accents("Olá, você está bem?")
        'Ola, voce esta bem?'
    """
    if not isinstance(text, str):
        raise ValidationError("text", text, "str")
    
    nfkd_form = unicodedata.normalize('NFKD', text)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


# ✂ Remover caracteres especiais
def remove_special_characters(text: str) -> str:
    """
    Remove caracteres especiais do texto.
    
    Args:
        text: Texto de entrada com caracteres especiais
        
    Returns:
        Texto sem caracteres especiais
        
    Examples:
        >>> remove_special_characters("Olá! @#$%")
        'Olá '
    """
    if not isinstance(text, str):
        raise ValidationError("text", text, "str")
    
    return re.sub(r'[^\w\s]', '', text)


# 🔄 Converter para snake_case
def to_snake_case(text: str) -> str:
    """
    Converte texto para snake_case.
    
    Args:
        text: Texto de entrada para conversão
        
    Returns:
        Texto convertido para snake_case
        
    Examples:
        >>> to_snake_case("Texto Exemplo Aqui!")
        'texto_exemplo_aqui'
    """
    if not isinstance(text, str):
        raise ValidationError("text", text, "str")
    
    text = remove_accents(text)
    text = re.sub(r'\s+', '_', text.strip().lower())
    return re.sub(r'[^a-z0-9_]', '', text)


# 🔄 Converter para camelCase
def to_camel_case(text: str) -> str:
    """
    Converte texto para camelCase.
    
    Args:
        text: Texto de entrada para conversão
        
    Returns:
        Texto convertido para camelCase
        
    Examples:
        >>> to_camel_case("Texto Exemplo Aqui!")
        'textoExemploAqui'
    """
    if not isinstance(text, str):
        raise ValidationError("text", text, "str")
    
    text = to_snake_case(text)
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


# 🔄 Converter para PascalCase
def to_pascal_case(text: str) -> str:
    """
    Converte texto para PascalCase.
    
    Args:
        text: Texto de entrada para conversão
        
    Returns:
        Texto convertido para PascalCase
        
    Examples:
        >>> to_pascal_case("Texto Exemplo Aqui!")
        'TextoExemploAqui'
    """
    if not isinstance(text, str):
        raise ValidationError("text", text, "str")
    
    return ''.join(word.capitalize() for word in to_snake_case(text).split('_'))


# 🌐 Remover HTML
def remove_html(text: str) -> str:
    """
    Remove tags HTML do texto.
    
    Args:
        text: Texto HTML de entrada
        
    Returns:
        Texto limpo sem tags HTML
        
    Examples:
        >>> remove_html("<div><h1>Título</h1><p>Parágrafo</p></div>")
        'Título Parágrafo'
    """
    if not isinstance(text, str):
        raise ValidationError("text", text, "str")
    
    soup = BeautifulSoup(text, 'html.parser')
    return soup.get_text(separator=' ', strip=True)


# 🔍 Remover múltiplos espaços
def remove_extra_spaces(text: str) -> str:
    """
    Remove espaços extras do texto.
    
    Args:
        text: Texto com espaços extras
        
    Returns:
        Texto com espaços normalizados
        
    Examples:
        >>> remove_extra_spaces("Texto    com   espaços   extras.")
        'Texto com espaços extras.'
    """
    if not isinstance(text, str):
        raise ValidationError("text", text, "str")
    
    return re.sub(r'\s+', ' ', text).strip()


# 🧹 Limpeza completa do texto
def clean_text(text: str, case: Literal['lower', 'upper', 'title', 'snake', 'camel', 'pascal'] = 'lower') -> str:
    """
    Limpeza completa do texto:
    - Remove HTML
    - Remove acentos
    - Remove caracteres especiais
    - Normaliza espaços
    - Converte o texto para o formato especificado
    
    Args:
        text: Texto de entrada para limpeza
        case: Formato de saída desejado ('lower', 'upper', 'title', 'snake', 'camel', 'pascal')
        
    Returns:
        Texto limpo no formato especificado
        
    Raises:
        ValidationError: Se o parâmetro 'text' não for uma string
        UnsupportedFormatError: Se o parâmetro 'case' for inválido
        
    Examples:
        >>> clean_text("<h1>Olá, Mundo!</h1>", case="lower")
        'ola mundo'
        >>> clean_text("Texto Exemplo", case="snake")
        'texto_exemplo'
    """
    if not isinstance(text, str):
        raise ValidationError("text", text, "str")
    
    if case not in ('lower', 'upper', 'title', 'snake', 'camel', 'pascal'):
        raise UnsupportedFormatError(case, ['lower', 'upper', 'title', 'snake', 'camel', 'pascal'])
    
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
        # Este ponto nunca deve ser alcançado devido à validação acima
        raise RuntimeError("Erro interno: formato de case inválido")



