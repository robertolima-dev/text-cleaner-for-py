# 📚 **/text-cleaner-for-py**

🧹 **/text-cleaner-for-py** é um pacote Python leve e eficiente para **limpeza** e **normalização de texto**. Ele oferece recursos para remoção de HTML, acentos, caracteres especiais, além de filtros, normalização e remoção de stopwords.

---

## ✨ **Funcionalidades**
- 🔡 **Normalização de texto:**
  - Conversão para minúsculas.
  - Remoção de acentos e caracteres especiais.
- 🧹 **Limpeza avançada:**
  - Remoção de HTML e tags indesejadas.
  - Redução de múltiplos espaços e quebras de linha.
- 🔍 **Filtros de texto:**
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

### 🔡 **Normalização de texto:**
```python
from text_cleaner_for_py.cleaner_v1 import normalize_text

texto = "<p>Olá, Mundo!</p> Bem-vindo ao /text-cleaner-for-py! 🧹✨"
texto_normalizado = normalize_text(texto)

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

texto = "Texto   com   espaços    e  \n\n quebras."
print(clean_whitespace(texto))  # Saída: Texto com espaços e quebras.
```

### 🔠 **Filtrando letras e números:**
```python
from text_cleaner_for_py.cleaner_v1 import filter_letters, filter_numbers

texto = "Telefone: 123-456-789"
print(filter_letters(texto))  # Saída: Telefone
print(filter_numbers(texto))  # Saída: 123456789
```

### 📝 **Removendo stopwords:**
```python
from text_cleaner_for_py.cleaner_v1 import remove_stopwords

texto = "Este é um texto simples para teste de stopwords."
print(remove_stopwords(texto, language='portuguese'))  # Saída: texto simples teste stopwords.
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

---

## ⭐ **Gostou do projeto?**

Deixe uma ⭐ no repositório e compartilhe com a comunidade! 🚀✨
