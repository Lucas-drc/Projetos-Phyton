class Aluno:
    def __init__(self, nome: str, notas: list):
        self.nome = nome
        self.notas = notas if notas is not None else []
   
    def exibir(self):
        print(f"Nome: {self.nome}")
        if not self.notas:
            print(f"Não possui notas lançadas")
            return
        
        for ordem_nota, nota in enumerate(self.notas, start=1):
                print(f"Nota nº {ordem_nota}: {nota}")

    def situacao(self):
        self.situacao = sum(self.notas)
        media = sum(self.notas) / len(self.notas)
        if media >= 6:
            print(f"Aluno aprovado!Com média {media}")
        elif media < 6:
           print(f"Aluno reprovado!Com média {media}")






def exibir_menu():
    print("\n=====================")
    print("1 - Cadastrar aluno")
    print("2 - Lançar nota")
    print("3 - Ver situação")
    print("4 - Listar alunos")
    print("0 - Sair")
    print("=====================")

def cadastrar_aluno():
    print("\nCADASTRANDO ALUNO...")
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome, [])
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")


def cadastrar_notas():
    print("\nCADASTRANDO NOTAS..")
    codigo_aluno = int(input("Digite o código do aluno: ")) - 1
    aluno = alunos[codigo_aluno]
    nota = float(input("Digite a nota: "))
    aluno.notas.append(nota)
    print(f"Nota {nota} lançada para o aluno {aluno.nome}")

def exibir_diario():
    codigo_aluno = int(input("Digite o código do aluno: ")) - 1
    aluno = alunos[codigo_aluno]
    aluno.situacao()


def listar_alunos():
    if not alunos:
        print( "Não há alunos!")
        return
    for codigo_aluno, aluno in enumerate (alunos, start=1):
        print(f"\nCódigo aluno: {codigo_aluno}")
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
        listar_alunos()
    else:
        print("Opção inválida.")

