from typing import List
import re

#Definição de classes para representar livros e usuários
class Livro:
    def __init__(self, titulo: str, autor: str, disponibilidade: bool):
        self.titulo = titulo
        self.autor = autor
        self.disponibilidade = disponibilidade
        
class Usuario:
    def __init__(self, nome: str, livros_emprestados: List[Livro] = []):
        self.nome = nome
        self.livros_emprestados = livros_emprestados

#Declarando as listas para armazenar os livros e usuários da biblioteca
biblioteca_livros: List[Livro] = []
biblioteca_usuarios: List[Usuario] = []

#Declarando as funções para tratamentos de erros e validação de dados
def validar_titulo_livro(titulo: str) -> str:
    if not titulo.strip():
        raise ValueError("O título do livro não pode ser vazio.")
    return titulo

def validar_autor_livro(autor: str) -> str:
    if len(autor) < 3:
        raise ValueError("O nome do autor deve conter pelo menos 3 caracteres.")
    if not autor.strip():
        raise ValueError("O nome do autor não pode ser vazio.")
    if any(char.isdigit() for char in autor):
        raise ValueError("O nome do autor não pode conter números.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', autor):
        raise ValueError("O nome do autor não pode conter símbolos.")
    return autor

def validar_nome_usuario(nome: str) -> str:
    if len(nome) < 3:
        raise ValueError("O nome do usuário deve conter pelo menos 3 caracteres.")
    if not nome.strip():
        raise ValueError("O nome do usuário não pode ser vazio.")
    if any(char.isdigit() for char in nome):
        raise ValueError("O nome do usuário não pode conter números.")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', nome):
        raise ValueError("O nome do usuário não pode conter símbolos.")
    return nome


#Declarando as funções para as operações da biblioteca
def adicionar_novos_livros_a_biblioteca():
    titulo = input("Digite o título do livro: ")
    titulo = validar_titulo_livro(titulo)
    autor = input("Digite o autor do livro: ")
    autor = validar_autor_livro(autor)
    livro = Livro(titulo, autor, True)
    biblioteca_livros.append(livro)
    print(f"Livro '{titulo}' adicionado à biblioteca com sucesso!")
    
def remover_livros_da_biblioteca():
    titulo = input("Digite o título do livro a ser removido: ")
    titulo = validar_titulo_livro(titulo)
    for livro in biblioteca_livros:
        if livro.titulo == titulo:
            biblioteca_livros.remove(livro)
            print(f"Livro '{titulo}' removido da biblioteca com sucesso!")
            return
    print(f"Livro '{titulo}' não encontrado na biblioteca.")
    
def listar_todos_os_livros_disponiveis():
    print("Livros disponíveis na biblioteca:")
    for livro in biblioteca_livros:
        if livro.disponibilidade:
            print(f"- {livro.titulo} por {livro.autor}")
            
def registrar_usuarios():
    nome = input("Digite o nome do usuário: ")
    nome = validar_nome_usuario(nome)
    usuario = Usuario(nome)
    biblioteca_usuarios.append(usuario)
    print(f"Usuário '{nome}' cadastrado na biblioteca com sucesso!")
    
def registrar_emprestimos_de_livros():
    nome_usuario = input("Digite o nome do usuário: ")
    nome_usuario = validar_nome_usuario(nome_usuario)
    titulo_livro = input("Digite o título do livro a ser emprestado: ")
    titulo_livro = validar_titulo_livro(titulo_livro)

    usuario_encontrado = None
    for usuario in biblioteca_usuarios:
        if usuario.nome == nome_usuario:
            usuario_encontrado = usuario
            break
            
    if not usuario_encontrado:
        print(f"Usuário '{nome_usuario}' não encontrado.")
        return
    
    livro_encontrado = None
    for livro in biblioteca_livros:
        if livro.titulo == titulo_livro and livro.disponibilidade:
            livro_encontrado = livro
            break
            
    if not livro_encontrado:
        print(f"Livro '{titulo_livro}' não disponível para empréstimo.")
        return
    
    livro_encontrado.disponibilidade = False
    print(f"Livro '{titulo_livro}' emprestado para usuário '{nome_usuario}' com sucesso!")
    
def consultar_livros_emprestados_e_disponiveis():
    print("Livros emprestados:")
    for livro in biblioteca_livros:
        if not livro.disponibilidade:
            print(f"- {livro.titulo} por {livro.autor}")
    
    print("\nLivros disponíveis:")
    for livro in biblioteca_livros:
        if livro.disponibilidade:
            print(f"- {livro.titulo} por {livro.autor}")
  
  
#Menu do sistema de biblioteca para interação com o usuário          
while True:
    print("\nMenu da Biblioteca:")
    print("1. Adicionar novos livros à biblioteca")
    print("2. Remover livros da biblioteca")
    print("3. Listar todos os livros disponíveis")
    print("4. Registrar usuários")
    print("5. Registrar empréstimos de livros")
    print("6. Consultar livros emprestados e disponíveis")
    print("7. Sair")
    
    escolha = input("Digite o número da opção desejada: ")
    
    if escolha == '1':
        try:
            adicionar_novos_livros_a_biblioteca()
        except ValueError as e:
            print(f"Erro: {e}")
    elif escolha == '2':
        try:
            remover_livros_da_biblioteca()
        except ValueError as e:
            print(f"Erro: {e}")
    elif escolha == '3':
        try:
            listar_todos_os_livros_disponiveis()
        except ValueError as e:
            print(f"Erro: {e}")
    elif escolha == '4':
        try:
            registrar_usuarios()
        except ValueError as e:
            print(f"Erro: {e}")
    elif escolha == '5':
        try:
            registrar_emprestimos_de_livros()
        except ValueError as e:
            print(f"Erro: {e}")
    elif escolha == '6':
        try:
            consultar_livros_emprestados_e_disponiveis()
        except ValueError as e:
            print(f"Erro: {e}")
    elif escolha == '7':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")