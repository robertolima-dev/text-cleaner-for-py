import re
import unicodedata
from typing import List, Dict, Union
from datetime import datetime
import emoji
import langdetect
from langdetect import DetectorFactory
from nltk.stem import SnowballStemmer, WordNetLemmatizer
import nltk

# Garantir que os recursos necessários do NLTK estão disponíveis
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# Configurar o detector de idioma para ser determinístico
DetectorFactory.seed = 0

# Mapeamento de meses em português
MONTHS_PT = {
    1: 'janeiro',
    2: 'fevereiro',
    3: 'março',
    4: 'abril',
    5: 'maio',
    6: 'junho',
    7: 'julho',
    8: 'agosto',
    9: 'setembro',
    10: 'outubro',
    11: 'novembro',
    12: 'dezembro'
}

class AdvancedTextCleaner:
    def __init__(self):
        self.stemmers = {}
        self.lemmatizers = {}
        
    def detect_language(self, text: str) -> str:
        """Detecta o idioma do texto."""
        try:
            return langdetect.detect(text)
        except:
            return 'unknown'

    def remove_emojis(self, text: str) -> str:
        """Remove emojis e emoticons do texto."""
        return emoji.replace_emoji(text, '')

    def remove_urls(self, text: str) -> str:
        """Remove URLs do texto."""
        url_pattern = r'https?://\S+|www\.\S+'
        return re.sub(url_pattern, '', text)

    def remove_emails(self, text: str) -> str:
        """Remove endereços de email do texto."""
        email_pattern = r'\S+@\S+'
        return re.sub(email_pattern, '', text)

    def normalize_numbers(self, text: str) -> str:
        """Normaliza números no texto (ex: 1º -> primeiro)."""
        number_map = {
            '1º': 'primeiro', '2º': 'segundo', '3º': 'terceiro',
            '4º': 'quarto', '5º': 'quinto', '6º': 'sexto',
            '7º': 'sétimo', '8º': 'oitavo', '9º': 'nono',
            '10º': 'décimo'
        }
        for num, word in number_map.items():
            text = text.replace(num, word)
        return text

    def normalize_dates(self, text: str) -> str:
        """Normaliza datas no texto para um formato padrão."""
        date_patterns = [
            (r'(\d{2})/(\d{2})/(\d{4})', '%d/%m/%Y'),
            (r'(\d{2})-(\d{2})-(\d{4})', '%d-%m-%Y'),
            (r'(\d{4})/(\d{2})/(\d{2})', '%Y/%m/%d')
        ]
        
        for pattern, date_format in date_patterns:
            matches = re.finditer(pattern, text)
            for match in matches:
                try:
                    date = datetime.strptime(match.group(), date_format)
                    month = MONTHS_PT[date.month]
                    normalized_date = f"{date.day} de {month} de {date.year}"
                    text = text.replace(match.group(), normalized_date)
                except ValueError:
                    continue
        return text

    def normalize_currency(self, text: str) -> str:
        """Normaliza valores monetários no texto."""
        currency_pattern = r'R\$\s*(\d+(?:\.\d{3})*(?:,\d{2})?)'
        matches = re.finditer(currency_pattern, text)
        for match in matches:
            value = match.group(1).replace('.', '').replace(',', '.')
            normalized = f"R$ {float(value):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            text = text.replace(match.group(), normalized)
        return text

    def remove_typos(self, text: str) -> str:
        """Corrige erros comuns de digitação."""
        typo_map = {
            'vc': 'você',
            'pq': 'porque',
            'q': 'que',
            'tb': 'também',
            'tbm': 'também',
            'mt': 'muito',
            'mto': 'muito',
            'td': 'tudo',
            'tdo': 'tudo',
            'tda': 'toda',
            'tde': 'todo'
        }
        
        # Divide o texto em palavras e processa cada uma individualmente
        words = text.split()
        corrected_words = []
        for word in words:
            # Remove pontuação no final da palavra para fazer a comparação
            clean_word = word.strip('.,!?:;')
            # Verifica se a palavra está no mapa de correções
            if clean_word.lower() in typo_map:
                # Se houver pontuação, mantém ela no final
                punctuation = word[len(clean_word):]
                corrected = typo_map[clean_word.lower()] + punctuation
                corrected_words.append(corrected)
            else:
                corrected_words.append(word)
        
        return ' '.join(corrected_words)

    def remove_duplicate_text(self, text: str) -> str:
        """Remove texto duplicado mantendo apenas uma ocorrência."""
        words = text.split()
        seen = set()
        unique_words = []
        for word in words:
            if word not in seen:
                seen.add(word)
                unique_words.append(word)
        return ' '.join(unique_words)

    def normalize_abbreviations(self, text: str) -> str:
        """Normaliza abreviações comuns no texto."""
        abbr_map = {
            'ex.': 'exemplo',
            'etc.': 'etcetera',
            'vs.': 'versus',
            'i.e.': 'isto é',
            'e.g.': 'por exemplo',
            'Dr.': 'Doutor',
            'Dra.': 'Doutora',
            'Sr.': 'Senhor',
            'Sra.': 'Senhora',
            'Srta.': 'Senhorita'
        }
        for abbr, full in abbr_map.items():
            text = text.replace(abbr, full)
        return text

    def get_stemmer(self, language: str) -> SnowballStemmer:
        """Obtém ou cria um stemmer para o idioma especificado."""
        if language not in self.stemmers:
            try:
                self.stemmers[language] = SnowballStemmer(language)
            except ValueError:
                self.stemmers[language] = SnowballStemmer('english')
        return self.stemmers[language]

    def get_lemmatizer(self, language: str) -> WordNetLemmatizer:
        """Obtém ou cria um lemmatizer para o idioma especificado."""
        if language not in self.lemmatizers:
            self.lemmatizers[language] = WordNetLemmatizer()
        return self.lemmatizers[language]

    def stem_text(self, text: str, language: str = 'portuguese') -> str:
        """Aplica stemming ao texto."""
        stemmer = self.get_stemmer(language)
        words = text.split()
        stemmed_words = [stemmer.stem(word) for word in words]
        return ' '.join(stemmed_words)

    def lemmatize_text(self, text: str, language: str = 'portuguese') -> str:
        """Aplica lematização ao texto."""
        # Mapeamento de verbos em português para suas formas infinitivas
        verb_map = {
            'correndo': 'correr',
            'pulando': 'pular',
            'saltando': 'saltar',
            'fazendo': 'fazer',
            'dizendo': 'dizer',
            'vendo': 'ver',
            'indo': 'ir',
            'sendo': 'ser',
            'tendo': 'ter',
            'querendo': 'querer'
        }
        
        words = text.split()
        lemmatized_words = []
        for word in words:
            if word in verb_map:
                lemmatized_words.append(verb_map[word])
            else:
                lemmatized_words.append(word)
        return ' '.join(lemmatized_words)

    def clean_advanced(self, text: str, options: Dict[str, bool] = None) -> str:
        """
        Realiza uma limpeza avançada do texto com base nas opções especificadas.
        
        Opções disponíveis:
        - remove_emojis: Remove emojis e emoticons
        - remove_urls: Remove URLs
        - remove_emails: Remove endereços de email
        - normalize_numbers: Normaliza números por extenso
        - normalize_dates: Normaliza datas
        - normalize_currency: Normaliza valores monetários
        - remove_typos: Corrige erros comuns de digitação
        - remove_duplicates: Remove texto duplicado
        - normalize_abbreviations: Normaliza abreviações
        - stem: Aplica stemming
        - lemmatize: Aplica lematização
        """
        if options is None:
            options = {
                'remove_emojis': True,
                'remove_urls': True,
                'remove_emails': True,
                'normalize_numbers': True,
                'normalize_dates': True,
                'normalize_currency': True,
                'remove_typos': True,
                'remove_duplicates': True,
                'normalize_abbreviations': True,
                'stem': False,
                'lemmatize': False
            }

        if options.get('remove_emojis'):
            text = self.remove_emojis(text)
        if options.get('remove_urls'):
            text = self.remove_urls(text)
        if options.get('remove_emails'):
            text = self.remove_emails(text)
        if options.get('remove_typos'):
            text = self.remove_typos(text)
        if options.get('normalize_numbers'):
            text = self.normalize_numbers(text)
        if options.get('normalize_dates'):
            text = self.normalize_dates(text)
        if options.get('normalize_currency'):
            text = self.normalize_currency(text)
        if options.get('remove_duplicates'):
            text = self.remove_duplicate_text(text)
        if options.get('normalize_abbreviations'):
            text = self.normalize_abbreviations(text)

        language = self.detect_language(text)
        if options.get('stem'):
            text = self.stem_text(text, language)
        if options.get('lemmatize'):
            text = self.lemmatize_text(text, language)

        return text 