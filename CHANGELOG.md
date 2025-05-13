# 📜 Changelog


## [1.3.0] - 2024-05-13
### Adicionado
- Novo módulo `performance_cleaner` com:
  - Processamento paralelo de textos (`clean_texts_parallel`)
  - Processamento de texto grande em chunks (`clean_large_text`)
  - Cache local de limpeza (`clean_text_cached`)
  - Remoção de ruído de OCR (`remove_ocr_noise`)
  - Normalização de unidades de medida (`normalize_measurements`)
  - Remoção de conteúdo duplicado (`remove_duplicates`)
  - Normalização de nomes próprios (`normalize_proper_names`)
  - Limpeza assíncrona (`clean_texts_async`)
  - Limpeza com opções específicas (`clean_text_with_options`)
  - Suporte a cache distribuído com Redis (`clean_text_distributed_cache`)
  - Suporte a processamento com GPU (PyTorch)
- Testes automatizados para todas as novas funcionalidades


## [1.2.0] - 2025-04-29
### Adicionado
- Processamento paralelo para múltiplos textos usando ProcessPoolExecutor
- Processamento de Textos Grandes

## [1.1.7] - 2025-04-17
### Adicionado
- Novas funcionalidades e normalização

## [1.1.6] - 2025-03-20
### Adicionado
- Ajuste na documentação

## [1.1.5] - 2025-03-19
### Adicionado
- Clean code

## [1.1.4] - 2025-03-19
### Adicionado
- Instalação de pacotes

## [1.1.3] - 2025-03-19
### Adicionado
- Ajustes no install_requires

## [1.1.2] - 2025-02-25
### Adicionado
- Novas funções de normalização

## [0.1.2] - 2025-02-24
### Adicionado
- Normalized name

## [0.1.1] - 2025-02-24
### Adicionado
- 🚀 Ajuste README

## [0.1.0] - 2025-02-24
### Adicionado
- 🚀 Primeira versão com limpeza de textos com text cleaner.

## [0.2.0] - 2024-04-16
### Added
- Nova classe `AdvancedTextCleaner` com funcionalidades avançadas:
  - Detecção automática de idioma
  - Remoção de emojis e emoticons
  - Remoção de URLs e emails
  - Normalização de números, datas e valores monetários
  - Correção de erros comuns de digitação
  - Remoção de texto duplicado
  - Normalização de abreviações
  - Stemming e lematização
- Novas dependências: `emoji` e `langdetect`
- Documentação atualizada com exemplos das novas funcionalidades
- Testes unitários para as novas funcionalidades

### Changed
- Atualização da versão do pacote para 0.2.0
- Melhoria na estrutura do projeto
- Atualização do README.md com novas seções

## [0.1.0] - 2024-03-21
### Added
- Funcionalidades básicas de limpeza de texto
- Suporte para remoção de HTML
- Normalização de texto
- Filtros de texto
- Remoção de stopwords
- Documentação inicial
- Testes unitários básicos

