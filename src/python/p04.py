from dataclasses import dataclass
@dataclass
class Data:
    dia: int
    mes: int
    ano: int

@dataclass
class Estudante:
    nome: str # Com no mínimo, nome e sobrenome
    matricula: str
    data_nascimento: Data

class SistemaEscolar:
    def __init__(self):
        # exemplo ficticio
        self.estudantes = [Estudante('Pedrinho Certezas', '20221144012220', Data(22,1,1999)), Estudante('Pedrinho desCertezas', '20221144012221', Data(22,1,2000))]
    def mostrar_menu(self):
        menu = """
        ====================
        SISTEMA ESCOLAR
        ====================
        1. Cadastrar novo estudante
        2. Listar todos os estudantes
        3. Atualizar dados de um estudante
        4. Excluir um estudante
        5. Solicitar dados de um estudante
        6. Sair
        ====================
        """
        print(menu)

    def opcao_invalida(self):
        print("Opção inválida, por favor selecione uma opção válida.")

    def excluir(self):
        print('você escolheu excluir')
        estudante_exclu = input('Informe a Matricula do estudante que deseja excluir ')
        for alunos in self.estudantes:
            if alunos.matricula == estudante_exclu:
                confirm = input('Confirma a exclusão (sim ou nao) ')
                if confirm == "sim":
                    return self.estudantes.pop(self.estudantes.index(alunos))
                elif confirm == "nao":
                    return
        print('matricula nao encontrada')
        return self.excluir()
        
    def atualizar(self):
        print('você escolheu atualizar')
        estudante_att = input('Informe a Matricula do estudante ')
        for alunos in self.estudantes:
            if alunos.matricula == estudante_att:
                print(f'atualize a nova matricula, nome ou data de nascimento de {alunos.nome}')
                nome = input("nome: ")
                matricula = input("matricula: ")
                data = [int(i) for i in input('data de nascimento (separe os numeros com um espaço) ').split()]
                if 1 > data[1] or data[1] > 12 or data[2] < 0 or 1 > data[0] or data[0] > 31:
                    print('data Inválida')
                    return self.atualizar()
    
                elif nome == "" or matricula == "" or data == "":
                    print('Preencha todos os campos devidamente')
                    return self.atualizar()
            
                alunos.nome = nome
                alunos.matricula = matricula
                alunos.data_nascimento = Data(data[0], data[1], data[2])
                return print('Dados Atualizados!')
        print('Matricula não encontrada')
        return self.atualizar()

    def listar(self):
        print("você escolheu listar")
        print('LISTA DE ESTUDANTES: ')
        for aluno in self.estudantes:
            print(f'nome: {aluno.nome} matricula: {aluno.matricula} data de nascimento: {aluno.data_nascimento.dia}/{aluno.data_nascimento.mes}/{aluno.data_nascimento.ano}')

    def cadastrar(self):
        print('você escolheu cadastrar')
        print('Informe o nome, matricula e data de nascimento a seguir: ')
        nome = input("nome: ")
        matricula = input("matricula: ")
        data = [int(i) for i in input('data de nascimento (separe os numeros com um espaço)').split()]
        if 1 > data[1] or data[1] > 12 or data[2] < 0 or 1 > data[0] or data[0] > 31:
            print('data Inválida')
            return self.cadastrar()
        elif nome == "" or matricula == "" or data == "":
            print('Preencha todos os campos devidamente')
            return self.cadastrar()
        novo_estudante = Estudante(nome, matricula, Data(data[0], data[1], data[2]))
        self.estudantes.append(novo_estudante)
        return print('Estudante Cadastrado!')
    
    def solicitar_dados(self):
        print('você escolheu solicitar dados')
        estudante_sol = input('Informe a Matricula do estudante solicitado ')
        for alunos in self.estudantes:
            if alunos.matricula == estudante_sol:
                solicitacao = input(f'Solicitar dados do estudante (opcoes: nome, matricula, data_nascimento, 0 (sair)) ')
                if solicitacao == "0":
                    break
                elif solicitacao == "nome":
                    print(f'Nome: {alunos.nome}')
                elif solicitacao == "matricula":
                    print(f'Matricula: {alunos.matricula}')
                elif solicitacao == "data_nascimento":
                    print(f'Data de nascimento: {alunos.data_nascimento.dia}/{alunos.data_nascimento.mes}/{alunos.data_nascimento.ano}')
                else:
                    print('opcao invalida')
                    self.solicitar_dados()
    def main(self):
        entrada_usuario = 0
        while True:
            self.mostrar_menu()
            entrada_usuario = int(input())
            if entrada_usuario == 6:
                break
            elif entrada_usuario == 5:
                self.solicitar_dados()
                break
            elif entrada_usuario == 4:
                self.excluir()
                break
            elif entrada_usuario == 3:
                self.atualizar()
                break
            elif entrada_usuario == 2:
                self.listar()
                break
            elif entrada_usuario == 1:
                self.cadastrar()
                break
            else:
                self.opcao_invalida()
                  
ifPAR = SistemaEscolar()
ifPAR.main()