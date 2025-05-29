import pytest
from text_cleaner_for_py.spell_checker import SpellCheckerCleaner

@pytest.fixture
def spell_checker():
    return SpellCheckerCleaner(language='pt')

def test_check_text(spell_checker):
    text = "Olá mundu! Como vai vc?"
    result = spell_checker.check_text(text)
    assert 'mundu' in result
    assert 'vc' in result
    assert len(result) == 2

def test_correct_text(spell_checker):
    text = "Olá mundu! Como vai vc?"
    corrected = spell_checker.correct_text(text)
    assert "mundo" in corrected.lower()
    assert "você" in corrected.lower()

def test_get_suggestions(spell_checker):
    word = "mundu"
    suggestions = spell_checker.get_suggestions(word)
    assert "mundo" in suggestions

def test_preserve_capitalization(spell_checker):
    text = "Olá Mundu!"
    corrected = spell_checker.correct_text(text)
    assert corrected == "Olá Mundo!"

def test_ignore_punctuation(spell_checker):
    text = "Olá, mundu! Como vai?"
    corrected = spell_checker.correct_text(text)
    assert "," in corrected
    assert "!" in corrected
    assert "?" in corrected

def test_empty_text(spell_checker):
    text = ""
    result = spell_checker.check_text(text)
    assert result == {}
    corrected = spell_checker.correct_text(text)
    assert corrected == ""

def test_no_errors(spell_checker):
    text = "Olá mundo! Como vai você?"
    result = spell_checker.check_text(text)
    assert result == {}
    corrected = spell_checker.correct_text(text)
    assert corrected == text 