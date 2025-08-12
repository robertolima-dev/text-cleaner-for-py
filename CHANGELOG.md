# 📜 Changelog


## [1.5.0] - 2024-12-19
### Adicionado
- Sistema de exceções customizadas (`exceptions.py`) com:
  - `TextCleanerError`: Exceção base para todos os erros
  - `ValidationError`: Para erros de validação de entrada
  - `ConfigurationError`: Para erros de configuração
  - `ProcessingError`: Para erros durante processamento
  - `UnsupportedFormatError`: Para formatos não suportados
  - `LanguageNotSupportedError`: Para idiomas não suportados
  - `FileProcessingError`: Para erros de processamento de arquivos
  - `CacheError`: Para erros relacionados ao cache
  - `PerformanceError`: Para erros de performance
- Sistema de configuração centralizado (`config.py`) com:
  - `CleanerConfig`: Configurações para processamento de texto
  - `RedisConfig`: Configurações para conexão com Redis
  - `LoggingConfig`: Configurações para logging
  - `ConfigManager`: Gerenciador centralizado de configurações
  - Suporte a variáveis de ambiente para configuração
- Type hints completos em todas as funções principais
- Validação robusta de entrada em todas as funções
- Documentação de docstrings seguindo padrão Google
- Configurações modernas no `pyproject.toml` com:
  - Configurações para pytest, black, isort, mypy e coverage
  - Dependências de desenvolvimento organizadas
  - Configurações de build otimizadas

### Changed
- Versão atualizada para 1.5.0 em todos os arquivos
- Migração completa para `pyproject.toml` como configuração principal
- Tratamento de erros melhorado com exceções customizadas
- Validação de entrada mais robusta e informativa
- Documentação de funções padronizada e completa

### Fixed
- Inconsistências de versão entre arquivos
- Configuração duplicada entre `setup.py` e `pyproject.toml`
- Falta de type hints em funções principais
- Tratamento básico de erros

## [1.4.0] - 2024-05-29
### Adicionado
- Novo módulo de correção ortográfica (`spell_checker.py`) com:
  - Detecção de erros ortográficos
  - Correção automática de texto
  - Sugestões de correção
  - Suporte a abreviações comuns do português (ex: 'vc' → 'você')
- Novo módulo de processamento de documentos (`document_processor.py`) com:
  - Leitura de arquivos `.txt`, `.pdf` e `.docx`
  - Extração de metadados de documentos
  - Extração de tabelas de arquivos `.docx`
  - Estrutura pronta para extração de imagens
- Testes automatizados para ambos os módulos

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

