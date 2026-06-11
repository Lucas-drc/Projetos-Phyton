class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    def situacao(self):
        self.situacao = self.nota
        if self.situacao>= 6:
            print("Aluno aprovado!")
        elif self.situacao < 6:
            print("Aluno reprovado")

    def exibir(self):
        print(f"Nome do aluno: {self.nome} | Nota do aluno: {self.nota}")


def exibir_menu():
    print("=====================")
    print("1 - Cadastrar diário")
    print("2 - Visualizar diário")
    print("0 - Sair")
    print("=====================")

def cadastrar_diario():
    print("\nCADASTRANDO DIÁRIO...")
    nome = input("Digite o nome do aluno: ")
    nota = float (input("Digite a nota do aluno: "))
    aluno = Aluno(nome, nota)
    alunos.append(aluno)


def exibir_diario():
    if not alunos:
        print("Não há alunos cadastrados!")
        return
    for aluno in alunos:
        aluno.exibir()
        aluno.situacao()
        
alunos = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        break
    elif opcao =="1":
        cadastrar_diario()
    elif opcao =="2":
        exibir_diario()
    else:
        print("Opção inválida.")