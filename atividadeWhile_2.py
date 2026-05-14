idade = int (input("Digite uma idade entre 0 e 120 anos: "))

while idade <0 or idade >120:
    idade = int(input("""
Idade inválida! 
Digite novamente:"""))

print("Idade válida!")