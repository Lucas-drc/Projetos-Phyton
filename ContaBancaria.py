def menu():
    print("\n===================")
    print("Menu:")
    print("[1] - Depositar.")
    print("[2] - Sacar.")
    print("[3] - Ver saldo.")
    print("[0] - Sair.")
    print("===================")

def exibir(saldo):
    print(f"Seu saldo é: R${saldo:.2f}")

def depositar(saldo):
    dep = float(input("Digite o valor a ser depositado: R$"))
    saldo = saldo + dep #dep = variável depósito
    print(f"Depósito de R${dep:.2f} realizado com sucesso!")
    return saldo

def sacar(saldo):
    saque = float(input("Digite o valor que será sacado: R$"))
    if saque > saldo:
        print("Saldo insuficiente!")
        return saldo
    
    saldo = saldo - saque
    print(f"Saque de R${saque:.2f} realizado com sucesso!")
    return saldo

saldo = 0.0

while True:
    menu()
    opcao = input("Escolha a opção: ") 

    if opcao == "0":
        print("Saindo...")
        break
    elif opcao == "1":
        saldo = depositar(saldo)
    elif opcao == "2":
        saldo = sacar(saldo)
    elif opcao == "3":
        exibir(saldo)
    else:
        print("Opção inválida!")