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

---

## ⚡ **Instalação**

Instale o pacote diretamente do PyPI:

```bash
pip install text_cleaner_for_py
```

> O pacote depende de `nltk`, `beautifulsoup4` e `nltk stopwords` (com download automático).

---

## 💡 **Como Usar**

### 🧹 **Remover acentos:**
```python
from text_cleaner_for_py.cleaner import remove_accents

text = "Olá, você está em São Paulo?"
print(remove_accents(text))  # Saída: Ola, voce esta em Sao Paulo?
```

### 🧹 **✂️ Removendo Espaços Extras:**
```python
from text_cleaner_for_py.cleaner import remove_extra_spaces

text = "Texto   com   muitos    espaços   extras."
print(remove_extra_spaces(text))  # Saída: Texto com muitos espaços extras.
```

### 🧹 **🔠 Removendo Caracteres Especiais:**
```python
from text_cleaner_for_py.cleaner import remove_special_characters

text = "Olá, mundo! Bem-vindo ao Text Cleaner 🧹✨"
print(remove_special_characters(text))  # Saída: Ola mundo Bemvindo ao Text Cleaner
```

### 🧹 **🏷 Convertendo para camelCase:**
```python
from text_cleaner_for_py.cleaner import to_camel_case

text = "exemplo de conversão de text"
print(to_camel_case(text))  # Saída: exemploDeConversaoDeTexto
```

### 🧹 **🏷 Convertendo para PascalCase:**
```python
from text_cleaner_for_py.cleaner import to_pascal_case

text = "exemplo de conversão de text"
print(to_pascal_case(text))  # Saída: ExemploDeConversaoDeTexto
```

### 🧹 **🏷 Convertendo para snake_case:**
```python
from text_cleaner_for_py.cleaner import to_snake_case

text = "exemplo de conversão de text"
print(to_snake_case(text))  # Saída: exemplo_de_conversao_de_texto
```

### 🧹 **Limpando o Texto:**
```python
from text_cleaner_for_py.cleaner_v1 import clean_text

text = "Olá, mundo! Bem-vindo ao Text Cleaner 🧹✨"
print(clean_text(text))  # Saída: ola mundo bem vindo ao text cleaner
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
│   └── cleaner_v1.py  
│   └── cleaner.py            # ⚡ Funções principais de limpeza e normalização
│
├── tests/                    # 🧪 Testes unitários
│   └── test_cleaner_v1.py
│   └── test_cleaner.py
│
├── setup.py                  # ⚙️ Configuração do pacote para PyPI
├── pyproject.toml            # 📦 Configuração moderna
├── README.md                 # 📚 Documentação do pacote
├── LICENSE                   # 📜 Licença MIT
└── MANIFEST.in               # 📋 Inclusão de arquivos extras
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
