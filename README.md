# 📚 **/text-cleaner-for-py**

🧹 **/text-cleaner-for-py** é um pacote Python leve e eficiente para **limpeza** e **normalização de text**. Ele oferece recursos para remoção de HTML, acentos, caracteres especiais, além de filtros, normalização e remoção de stopwords.

---

## ✨ **Funcionalidades**
- 🔡 **Normalização de text:**
  - Conversão para minúsculas.
  - Remoção de acentos e caracteres especiais.
- 🧹 **Limpeza avançada:**
  - Remoção de HTML e tags indesejadas.
  - Redução de múltiplos espaços e quebras de linha.
- 🔍 **Filtros de text:**
  - Manutenção de letras e números.
  - Remoção de stopwords com suporte a múltiplos idiomas.
- 🚀 **Funcionalidades Avançadas:**
  - Detecção automática de idioma
  - Remoção de emojis e emoticons
  - Remoção de URLs e emails
  - Normalização de números, datas e valores monetários
  - Correção de erros comuns de digitação
  - Remoção de texto duplicado
  - Normalização de abreviações
  - Stemming e lematização

---

## ⚡ **Instalação**

Instale o pacote diretamente do PyPI:

```bash
pip install text_cleaner_for_py
```

> O pacote depende de `nltk`, `beautifulsoup4`, `emoji` e `langdetect`.

---

## 💡 **Como Usar**

### 🧹 **Uso Básico:**
```python
from text_cleaner_for_py.cleaner import clean_text

text = "Olá, mundo! Bem-vindo ao Text Cleaner 🧹✨"
print(clean_text(text))  # Saída: ola mundo bem vindo ao text cleaner
```

### 🚀 **Uso Avançado:**
```python
from text_cleaner_for_py.advanced_cleaner import AdvancedTextCleaner

cleaner = AdvancedTextCleaner()

# Limpeza completa com opções padrão
text = "Olá! 👋 Visite https://exemplo.com ou envie email para teste@exemplo.com. Data: 25/12/2023. Preço: R$ 1.234,56. vc sabe pq?"
cleaned = cleaner.clean_advanced(text)
print(cleaned)

# Limpeza personalizada
options = {
    'remove_emojis': True,
    'remove_urls': False,
    'normalize_dates': True,
    'remove_typos': True
}
cleaned = cleaner.clean_advanced(text, options)
print(cleaned)
```

### 🔡 **Normalização de text:**
```python
from text_cleaner_for_py.cleaner_v1 import normalize_text

text = "<p>Olá, Mundo!</p> Bem-vindo ao /text-cleaner-for-py! 🧹✨"
texto_normalizado = normalize_text(text)

print(texto_normalizado)  # Saída: ola mundo bem vindo ao text cleaner for py
```

### 🌐 **Removendo HTML:**
```python
from text_cleaner_for_py.cleaner_v1 import remove_html_tags

html_text = "<div><p>Texto <b>importante</b></p></div>"
print(remove_html_tags(html_text))  # Saída: Texto importante
```

### 🧹 **Reduzindo espaços:**
```python
from text_cleaner_for_py.cleaner_v1 import clean_whitespace

text = "Texto   com   espaços    e  \n\n quebras."
print(clean_whitespace(text))  # Saída: Texto com espaços e quebras.
```

### 🔠 **Filtrando letras e números:**
```python
from text_cleaner_for_py.cleaner_v1 import filter_letters, filter_numbers

text = "Telefone: 123-456-789"
print(filter_letters(text))  # Saída: Telefone
print(filter_numbers(text))  # Saída: 123456789
```

### 📝 **Removendo stopwords:**
```python
from text_cleaner_for_py.cleaner_v1 import remove_stopwords

text = "Este é um text simples para teste de stopwords."
print(remove_stopwords(text, language='portuguese'))  # Saída: text simples teste stopwords.
```

### 🚀 **Funcionalidades Avançadas:**
```python
from text_cleaner_for_py.advanced_cleaner import AdvancedTextCleaner

cleaner = AdvancedTextCleaner()

# Detecção de idioma
print(cleaner.detect_language("Olá, como vai você?"))  # Saída: pt

# Remoção de emojis
text = "Olá! 👋 Como vai você? 😊"
print(cleaner.remove_emojis(text))  # Saída: Olá!  Como vai você? 

# Normalização de números
text = "1º lugar, 2º lugar, 3º lugar"
print(cleaner.normalize_numbers(text))  # Saída: primeiro lugar, segundo lugar, terceiro lugar

# Normalização de datas
text = "Data: 25/12/2023"
print(cleaner.normalize_dates(text))  # Saída: Data: 25 de dezembro de 2023

# Correção de erros comuns
text = "vc sabe pq isso aconteceu?"
print(cleaner.remove_typos(text))  # Saída: você sabe porque isso aconteceu?

# Stemming e lematização
text = "correndo pulando saltando"
print(cleaner.stem_text(text))  # Saída: corr pul salt
print(cleaner.lemmatize_text(text))  # Saída: correr pular saltar
```

---

## 🧪 **Testes**

Execute os testes com `pytest`:

```bash
pytest tests/
```

Para execução detalhada:
```bash
pytest -v
```

---

## 🏗 **Estrutura do Projeto**

```
text_cleaner_for_py/
│
├── text_cleaner_for_py/             # 📦 Código do pacote
│   ├── __init__.py
│   ├── cleaner_v1.py                # ⚡ Funções básicas de limpeza
│   ├── cleaner.py                   # ⚡ Funções principais de limpeza
│   └── advanced_cleaner.py          # 🚀 Funções avançadas de limpeza
│
├── tests/                           # 🧪 Testes unitários
│   ├── test_cleaner_v1.py
│   ├── test_cleaner.py
│   └── test_advanced_cleaner.py
│
├── setup.py                         # ⚙️ Configuração do pacote para PyPI
├── pyproject.toml                   # 📦 Configuração moderna
├── README.md                        # 📚 Documentação do pacote
├── LICENSE                          # 📜 Licença MIT
└── MANIFEST.in                      # 📋 Inclusão de arquivos extras
```

---

## 📝 **Licença**

Distribuído sob a **Licença MIT**. Veja o arquivo [LICENSE](LICENSE) para mais informações.

---

## 👨‍💻 **Autor**

Desenvolvido por **[Roberto Lima](https://robertolima-developer.vercel.app/)** 🚀✨

---

## 💬 **Contato**

- 📧 **Email**: robertolima.izphera@gmail.com
- 💼 **LinkedIn**: [Roberto Lima](https://www.linkedin.com/in/roberto-lima-01/)
- 💼 **Website**: [Roberto Lima](https://robertolima-developer.vercel.app/)
- 💼 **Gravatar**: [Roberto Lima](https://gravatar.com/deliciouslyautomaticf57dc92af0)

---

## ⭐ **Gostou do projeto?**

Deixe uma ⭐ no repositório e compartilhe com a comunidade! 🚀✨
