from typing import List, Dict, Optional
from spellchecker import SpellChecker
import re

class SpellCheckerCleaner:
    def __init__(self, language: str = 'pt'):
        """
        Inicializa o corretor ortográfico.
        
        Args:
            language (str): Idioma para correção ('pt' para português, 'en' para inglês)
        """
        self.spell = SpellChecker(language=language)
        self.language = language
        self.abbreviations = {
            'vc': 'você',
            'tb': 'também',
            'pq': 'porque',
            'q': 'que',
            'td': 'tudo',
            'vlw': 'valeu',
            'blz': 'beleza',
            'tbm': 'também',
            'pfv': 'por favor',
            'pf': 'por favor',
            'obg': 'obrigado',
            'obgd': 'obrigado',
            'tks': 'thanks',
            'thx': 'thanks',
            'pls': 'please',
            'ty': 'thank you',
        }
        
    def check_text(self, text: str) -> Dict[str, List[str]]:
        """
        Verifica erros ortográficos no texto.
        
        Args:
            text (str): Texto a ser verificado
            
        Returns:
            Dict[str, List[str]]: Dicionário com palavras incorretas e sugestões
        """
        # Remove pontuação e divide em palavras
        words = re.findall(r'\b\w+\b', text.lower())
        
        # Encontra palavras incorretas
        misspelled = self.spell.unknown(words)
        
        # Cria dicionário com palavras incorretas e suas sugestões
        result = {}
        for word in misspelled:
            result[word] = list(self.spell.candidates(word))
            
        return result
    
    def correct_text(self, text: str) -> str:
        """
        Corrige erros ortográficos no texto.
        
        Args:
            text (str): Texto a ser corrigido
            
        Returns:
            str: Texto corrigido
        """
        # Divide o texto em palavras e pontuação
        words = re.findall(r'\b\w+\b|[^\w\s]|\s+', text)
        corrected_words = []
        for word in words:
            if re.match(r'\b\w+\b', word):  # Se for uma palavra
                lower_word = word.lower()
                if lower_word in self.abbreviations:
                    correction = self.abbreviations[lower_word]
                    if word[0].isupper():
                        correction = correction.capitalize()
                    corrected_words.append(correction)
                elif lower_word in self.spell:
                    corrected_words.append(word)
                else:
                    correction = self.spell.correction(word)
                    if word[0].isupper():
                        correction = correction.capitalize()
                    corrected_words.append(correction)
            else:
                corrected_words.append(word)
        return ''.join(corrected_words)
    
    def get_suggestions(self, word: str) -> List[str]:
        """
        Obtém sugestões de correção para uma palavra.
        
        Args:
            word (str): Palavra para obter sugestões
            
        Returns:
            List[str]: Lista de sugestões de correção
        """
        return list(self.spell.candidates(word)) 