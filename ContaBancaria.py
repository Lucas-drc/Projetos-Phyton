saldo = float(0)

def menu():
    print("\n===================")
    print("Menu:")
    print("[1] - Depositar.")
    print("[2] - Sacar.")
    print("[3] - Ver saldo.")
    print("[0] - Sair.")
    print("===================")

def depositar(saldo):
    deposito = float(input("Digite o valor a ser depositado: R$"))
    saldo = saldo + deposito
    print(f"Novo saldo: R${saldo:.2f}")

def sacar(saldo):
    saque = float(input("Digite o valor que será sacado: R$"))
    saldo = saldo - saque
    print(f"Novo saldo: R${saldo:.2f}")


while True:
    menu()
    opcao = input("Escolha a opção: ") 

    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1":
        depositar(saldo)
    elif opcao == "2":
        sacar(saldo)
    elif opcao == "3":
        exibir(saldo)
    else:
        print("Opção inválida!")