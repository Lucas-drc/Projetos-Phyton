while True:
    menu = """

 === Calculdora ===

 1 - Soma             (+)
 2 - Subtração        (-)
 3 - Multiplicação    (x)
 4 - Divisão          (/)
 0 - Sair             

"""

    print(menu)


    escolha = (input(f"Escolha uma opção:"))
    if escolha == "0":
        print(f"\nSaindo...")
        break

    number1 = int(input(f"\nDigite o primeiro número: "))
    number2 = int(input(f"\nDigite o segundo número: "))

    
    if escolha == "1":
        print(f"\nVocê escolheu soma... Vamos lá!")
        soma = (number1 + number2)
        print(f"\nResultado da soma = {soma}")

    elif escolha == "2":
        print(f"\nVocê escolheu subtração... Vamos lá!")
        subtracao = (number1 - number2)
        print(f"\nResultado da subtração = {subtracao}")
    
    elif escolha == "3":
        print(f"Você escolheu multiplicação... Vamos lá!")
        multiplicacao = (number1 * number2)
        print(f"\nResultado da multiplicação = {multiplicacao}")

    elif escolha == "4":
        print(f"\nVocê escolheu divisão... Vamos lá!")
        if number2 == 0:
            print(f"Essa altura do campeonato, e você fazendo isso!?")
        else:
            divisao = number1 / number2
            print(f"\nResultado da divisão = {divisao}")
    else:
        print(f"\nEscolha inválida! Tente novamente")