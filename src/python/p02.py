def mostrar_menu():
    menu = """
    ====================
       SISTEMA ESCOLAR
    ====================
    1. Cadastrar novo estudante
    2. Listar todos os estudantes
    3. Atualizar dados de um estudante
    4. Excluir um estudante
    5. Sair
    ====================
    """
    print(menu)

def opcao_invalida():
    print("Opção inválida, por favor selecione uma opção válida.")

def excluir():
    print('você escolheu excluir()')

def atualizar():
    print('você escolheu atualizar()')

def listar():
    print('você escolheu listar()')

def cadastrar():
    print('você escolheu cadastrar')

def main():
    entrada_usuario = 0
    while True:
        mostrar_menu()
        entrada_usuario = int(input())
        if entrada_usuario == 5:
            break
        elif entrada_usuario == 4:
            excluir()
            break
        elif entrada_usuario == 3:
            atualizar()
            break
        elif entrada_usuario == 2:
            listar()
            break
        elif entrada_usuario == 1:
            cadastrar()
            break
        else:
            opcao_invalida()
