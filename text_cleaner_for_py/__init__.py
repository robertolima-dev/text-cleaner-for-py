from text_cleaner_for_py.cleaner import (
    remove_accents,
    remove_special_characters,
    to_snake_case,
    to_camel_case,
    to_pascal_case,
    remove_html,
    remove_extra_spaces,
    clean_text,
)

from text_cleaner_for_py.cleaner_v1 import (
    normalize_text,
    remove_html_tags,
    clean_whitespace,
    filter_letters,
    filter_numbers,
    remove_stopwords,
)

from text_cleaner_for_py.advanced_cleaner import AdvancedTextCleaner

__version__ = "0.2.0"

__all__ = [
    # Funções básicas
    "remove_accents",
    "remove_special_characters",
    "to_snake_case",
    "to_camel_case",
    "to_pascal_case",
    "remove_html",
    "remove_extra_spaces",
    "clean_text",
    
    # Funções v1
    "normalize_text",
    "remove_html_tags",
    "clean_whitespace",
    "filter_letters",
    "filter_numbers",
    "remove_stopwords",
    
    # Classes avançadas
    "AdvancedTextCleaner",
]
