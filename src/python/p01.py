
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

def main():
    entrada_usuario = 0
    while True:
        mostrar_menu()
        entrada_usuario = int(input())
        if entrada_usuario == 5:
            break
        else:
            opcao_invalida()


if __name__ == "__main__":
    main()
