def somar(number1, number2):
    total = number1 + number2
    print(f"{number1} + {number2} = {total}")

def subtrair(number1, number2):
    total = number1 - number2
    print(f"{number1} - {number2} = {total}")

def multiplicar(number1, number2):
    total = number1 * number2
    print(f"{number1} x {number2} = {total}")

def dividir(number1, number2):
    if number2 == 0:
            print(f"""
Essa altura do campeonato, e você fazendo isso!? 
Não é possivel realizar essa operação!
                  """)
    else:
        total = number1 / number2
        print(f"{number1} / {number2} = {total}")

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
    
    if escolha not in ["1", "2", "3", "4", "0"]:
        print(f"\nEscolha inválida! Tente novamente")
        continue

    number1 = int(input(f"\nDigite o primeiro número: "))
    number2 = int(input(f"\nDigite o segundo número: "))

    
    if escolha == "1": somar(number1, number2)
    elif escolha == "2": subtrair(number1, number2)
    elif escolha == "3": multiplicar(number1, number2)
    elif escolha == "4": dividir(number1, number2)

        