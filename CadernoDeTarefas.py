
def menu():
    print("\n===================")
    print("Menu:")
    print("[1] - Adicionar tarefas à lista.")
    print("[2] - Exibir tarefas da lista.")
    print("[3] - Remover tarefas da lista.")
    print("[0] - Sair.")
    print("===================")

def adicionar_lista(tarefas):
    add = (input("Adiciona uma tarefa na sua lista: "))
    tarefas.append(add)
    print("Adicionando tarefa...")
    
    

def exibir_lista(tarefas):
    if not tarefas:
        print("Não há tarefas!")
    else:
        print("Suas tarefas:")
        for posicao_tarefa, tarefa in enumerate(tarefas, start=1):
            print(f"{posicao_tarefa} - {tarefa}")

def remover_lista(tarefas):
    if not tarefas:
        print("Não há tarefas para remover!")
    else:
        tarefa = int(input("Digite o número da tarefa que deseja remover: "))
        if tarefa > 0 and tarefa <= len(tarefas):
            tarefas_removida = tarefas.pop(tarefa - 1)
            print(f"Removendo tarefa: {tarefas_removida}.")
        else:
            print("Tarefa não existe, digite um número válido!")

tarefas = []

while True:
    menu()
    opcao = input("Escolha a opção: ") 

    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1":
        adicionar_lista(tarefas)
    elif opcao == "2":
        exibir_lista(tarefas)
    elif opcao == "3":
        remover_lista(tarefas)
    else:
        print("Opção inválida!")