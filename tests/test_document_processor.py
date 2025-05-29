import pytest
import os
from pathlib import Path
from text_cleaner_for_py.document_processor import DocumentProcessor

@pytest.fixture
def processor():
    return DocumentProcessor()

@pytest.fixture
def test_files_dir(tmp_path):
    # Criar diretório temporário para testes
    return tmp_path

@pytest.fixture
def sample_txt_file(test_files_dir):
    file_path = test_files_dir / "test.txt"
    content = "Este é um arquivo de teste.\nSegunda linha."
    file_path.write_text(content, encoding='utf-8')
    return str(file_path)

@pytest.fixture
def sample_docx_file(test_files_dir):
    # TODO: Criar arquivo DOCX de teste
    return None

@pytest.fixture
def sample_pdf_file(test_files_dir):
    # TODO: Criar arquivo PDF de teste
    return None

def test_read_txt_file(processor, sample_txt_file):
    content = processor.read_document(sample_txt_file)
    assert "Este é um arquivo de teste" in content
    assert "Segunda linha" in content

def test_file_not_found(processor):
    with pytest.raises(FileNotFoundError):
        processor.read_document("arquivo_inexistente.txt")

def test_unsupported_format(processor, test_files_dir):
    file_path = test_files_dir / "test.xyz"
    file_path.write_text("teste")
    with pytest.raises(ValueError):
        processor.read_document(str(file_path))

def test_extract_metadata_txt(processor, sample_txt_file):
    metadata = processor.extract_metadata(sample_txt_file)
    assert metadata['filename'] == "test.txt"
    assert metadata['extension'] == ".txt"
    assert metadata['size'] > 0
    assert 'created' in metadata
    assert 'modified' in metadata

@pytest.mark.skipif(True, reason="Necessário implementar criação de arquivos de teste")
def test_read_docx_file(processor, sample_docx_file):
    content = processor.read_document(sample_docx_file)
    assert content

@pytest.mark.skipif(True, reason="Necessário implementar criação de arquivos de teste")
def test_read_pdf_file(processor, sample_pdf_file):
    content = processor.read_document(sample_pdf_file)
    assert content

@pytest.mark.skipif(True, reason="Necessário implementar criação de arquivos de teste")
def test_extract_tables(processor, sample_docx_file):
    tables = processor.extract_tables(sample_docx_file)
    assert isinstance(tables, list)

@pytest.mark.skipif(True, reason="Necessário implementar criação de arquivos de teste")
def test_extract_images(processor, sample_docx_file):
    images = processor.extract_images(sample_docx_file)
    assert isinstance(images, list) 