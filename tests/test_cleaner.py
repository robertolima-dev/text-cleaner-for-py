# tests/test_cleaner.py
import sys
import os
import pytest
from text_cleaner_for_py.cleaner import (
    remove_accents,
    remove_special_characters,
    to_snake_case,
    to_camel_case,
    to_pascal_case,
    remove_html,
    remove_extra_spaces,
    clean_text
)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# 🔡 Teste para remoção de acentos
def test_remove_accents():
    assert remove_accents("Olá, você está bem?") == "Ola, voce esta bem?"

# ✂ Teste para remoção de caracteres especiais
def test_remove_special_characters():
    assert remove_special_characters("Olá! @#$%") == "Olá "

# 🔄 Testes de conversão de cases
def test_to_snake_case():
    assert to_snake_case("Texto Exemplo Aqui!") == "texto_exemplo_aqui"

def test_to_camel_case():
    assert to_camel_case("Texto Exemplo Aqui!") == "textoExemploAqui"

def test_to_pascal_case():
    assert to_pascal_case("Texto Exemplo Aqui!") == "TextoExemploAqui"

# 🌐 Teste para remoção de HTML
def test_remove_html():
    html_text = "<div><h1>Título</h1><p>Parágrafo</p></div>"
    assert remove_html(html_text) == "Título Parágrafo"

# 🔍 Teste para remoção de espaços extras
def test_remove_extra_spaces():
    assert remove_extra_spaces("Texto    com   espaços   extras.") == "Texto com espaços extras."

# 🧹 Testes para limpeza completa do texto
def test_clean_text_lower():
    texto = "<h1>Olá, Mundo!</h1>    Bem-vindo."
    assert clean_text(texto, case="lower") == "ola mundo bemvindo"

def test_clean_text_upper():
    texto = "<h1>Olá, Mundo!</h1>    Bem-vindo."
    assert clean_text(texto, case="upper") == "OLA MUNDO BEMVINDO"

def test_clean_text_title():
    texto = "<h1>Olá, Mundo!</h1>    Bem-vindo."
    assert clean_text(texto, case="title") == "Ola Mundo Bemvindo"

def test_clean_text_snake():
    texto = "<h1>Olá, Mundo!</h1>    Bem-vindo."
    assert clean_text(texto, case="snake") == "ola_mundo_bemvindo"

def test_clean_text_camel():
    texto = "<h1>Olá, Mundo!</h1>    Bem-vindo."
    assert clean_text(texto, case="camel") == "olaMundoBemvindo"

def test_clean_text_pascal():
    texto = "<h1>Olá, Mundo!</h1>    Bem-vindo."
    assert clean_text(texto, case="pascal") == "OlaMundoBemvindo"

# ⚠️ Teste para formato inválido
def test_clean_text_invalid_case():
    with pytest.raises(ValueError, match="⚠️ Formato de case inválido"):
        clean_text("Texto de teste", case="invalido")