class Aluno:
    def __init__(self, nome, notas=[]):
        self.nome = nome
        self.notas = notas
   
    def exibir(self):
        print(f"Nome do aluno: {self.nome}")
#        if self.notas:
#           for ordem_nota, nota in enumerate(self.notas,1):
#               print(f"Nota nº {ordem_nota}: {nota}")

#     def situacao(self):
#        self.situacao = sum(self.notas)
#        if self.situacao>= 6:
#            print("Aluno aprovado!")
#        elif self.situacao < 6:
#           print("Aluno reprovado")






def exibir_menu():
    print("=====================")
    print("1 - Cadastrar aluno")
    print("2 - Lançar nota")
    print("3 - Ver situação")
    print("4 - Listar alunos")
    print("0 - Sair")
    print("=====================")

def cadastrar_aluno():
    print("\nCADASTRANDO ALUNO...")
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome)
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

def cadastrar_notas():
    print("\nCADASTRANDO NOTAS..")
    indice = int(input("Digite o código do aluno: "))
    aluno = alunos[indice]
    nota = float(input("Digite a nota: "))
    aluno.notas.append(nota)
    print(f"Nota {nota} lançada para o aluno {aluno.nome}")




def exibir_alunos():
    if not alunos:
        print("Não há alunos cadastrados!")
        return
    for aluno in alunos:
        aluno.exibir()

        
alunos = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        break
    elif opcao =="1":
        cadastrar_aluno()
    elif opcao =="2":
        cadastrar_notas()
    elif opcao =="3":
        exibir_diario()
    elif opcao =="4":
        exibir_alunos()
    else:
        print("Opção inválida.")