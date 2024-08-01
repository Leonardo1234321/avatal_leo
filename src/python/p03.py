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

novo_estudante = Estudante('Pedrinho Certezas', '20221144012220', Data(22,1,1999))

while True:
    solicitacao = input(f'Solicitar dados do estudante (opcoes: nome, matricula, data_nascimento, 0 (sair)) ')
    if solicitacao == "0":
        break
    elif solicitacao == "nome":
        print(f'Nome: {novo_estudante.nome}')
    elif solicitacao == "matricula":
        print(f'Matricula: {novo_estudante.matricula}')
    elif solicitacao == "data_nascimento":
        print(f'Data de nascimento: {novo_estudante.data_nascimento.dia}/{novo_estudante.data_nascimento.mes}/{novo_estudante.data_nascimento.ano}')
    else:
        print('opcao invalida')
