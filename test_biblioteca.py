import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

# Importando as funções de validação do módulo biblioteca
from biblioteca import validar_titulo_livro, validar_autor_livro, validar_nome_usuario

# Testes para as funções de validação
def test_validar_titulo_livro():
    assert validar_titulo_livro("O Senhor dos Anéis") == "O Senhor dos Anéis"
    with pytest.raises(ValueError):
        validar_titulo_livro("")
    with pytest.raises(ValueError):
        validar_titulo_livro("A")
        
def test_validar_autor_livro():
    assert validar_autor_livro("JRR Tolkien") == "JRR Tolkien"
    with pytest.raises(ValueError):
        validar_autor_livro("")
    with pytest.raises(ValueError):
        validar_autor_livro("A")
        
def test_validar_nome_usuario():
    assert validar_nome_usuario("João Silva") == "João Silva"
    with pytest.raises(ValueError):
        validar_nome_usuario("")
    with pytest.raises(ValueError):
        validar_nome_usuario("A")
    with pytest.raises(ValueError):
        validar_nome_usuario("João123")
    with pytest.raises(ValueError):
        validar_nome_usuario("João@Silva")
        
if __name__ == "__main__":
    pytest.main()
    