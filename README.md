# 📚 **/text-cleaner-for-py**

🧹 **/text-cleaner-for-py** é um pacote Python leve e eficiente para **limpeza** e **normalização de texto**. Ele oferece recursos para remoção de HTML, acentos, caracteres especiais, além de conversões para formatos como `snake_case`, `camelCase` e `PascalCase`.

---

## ✨ **Funcionalidades**
- 🔡 Remoção de **acentos** e **caracteres especiais**.
- 🌐 **Limpeza de HTML** e remoção de emojis.
- 🔄 Conversão para:
  - `snake_case`
  - `camelCase`
  - `PascalCase`
  - Letras **maiúsculas**, **minúsculas** e **capitalização**.
- 🔍 **Redução de espaços extras**.
- 🧹 **Limpeza completa** em uma única função (`clean_text`).

---

## ⚡ **Instalação**

Instale o pacote diretamente do PyPI:

```bash
pip install /text-cleaner-for-py
```

---

## 💡 **Como Usar**

### 🔡 **Importando e limpando texto:**

```python
from text_cleaner.cleaner import clean_text

texto = "<h1>Olá, Mundo!</h1>   Bem-vindo ao /text-cleaner-for-py! 🧹✨"
texto_limpo = clean_text(texto, case="snake")

print(texto_limpo)  # Saída: ola_mundo_bemvindo_ao_text_cleaner
```

### ✂ **Removendo acentos:**
```python
from text_cleaner.cleaner import remove_accents

print(remove_accents("Olá, você está bem?"))  # Saída: Ola, voce esta bem?
```

### 🌐 **Removendo HTML:**
```python
from text_cleaner.cleaner import remove_html

html_text = "<div><p>Texto <b>importante</b></p></div>"
print(remove_html(html_text))  # Saída: Texto importante
```

### 🔄 **Convertendo formatos:**
```python
from text_cleaner.cleaner import to_snake_case, to_camel_case, to_pascal_case

print(to_snake_case("Exemplo De Texto"))   # Saída: exemplo_de_texto
print(to_camel_case("Exemplo De Texto"))   # Saída: exemploDeTexto
print(to_pascal_case("Exemplo De Texto"))  # Saída: ExemploDeTexto
```

---

## 🧪 **Testes**

Execute os testes com `pytest`:

```bash
pytest tests/
```

---

## 🏗 **Estrutura do Projeto**

```
text_cleaner/
│
├── text_cleaner/             # 📦 Código do pacote
│   ├── __init__.py
│   └── cleaner.py            # ⚡ Funções principais de limpeza
│
├── tests/                    # 🧪 Testes unitários
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
```

---

## 🌟 **O que este README oferece?**
- 🎯 **Descrição clara** do projeto e seu propósito.  
- 🛠 **Instruções detalhadas de instalação** e **uso prático**.  
- 🧪 **Guia de testes** para garantir que o código funciona.  
- 🏗 **Estrutura do projeto** para facilitar a navegação.  
- 🔄 **Seção de contribuição** para quem deseja ajudar no desenvolvimento.  
- 📝 **Licença e informações do autor** para transparência.
