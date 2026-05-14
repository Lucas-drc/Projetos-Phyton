import random
numero_secreto = random.randint(0,999999999)
palpite = 0 #precisou colocar uma variável 0 para inicializar o while
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Digite um número: "))
       
    tentativas = tentativas + 1


print(f"Você digitou {tentativas} números.")