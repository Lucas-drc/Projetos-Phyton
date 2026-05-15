
"""
# MINHA RESOLUÇÃO:
palpite = []
tentativas = 0

while palpite != 0:
    palpite = int(input("Digite um número: "))
    if palpite == 0:
     tentativas = tentativas 
    else:
       tentativas = tentativas + 1
     

if tentativas == 0:
    print(f"Você digitou o número 0 de primeira!.")
else:
    print(f"Você digitou {tentativas} vezes até digitar o número 0.")
"""



# RESOLUÇÃO DO PROFESSOR:
# variável contador recebe 0
# numero recebe -1
#
# enquanto numero for diferente de 0:
#   pergunte "digite um número" e converta para inteiro
#   numero recebe o que o usuário digitou
#   se numero for igual a 0:
#      contador recebe contadora
#   senao:
#       contador recebe contador +1
#exibe tentativas de contagens, contador

contador = 0
numero = -1
numeros = []

while numero != 0:
    numero = int(input("Digite um número: "))
    if numero != 0:
        contador = contador + 1
    numeros.append(numero)

if contador == 0:
    print(f"Você digitou o número 0 de primeira!.")
else:
    print(f"Você digitou {contador} vezes até digitar o número 0.")

print(f"Os número digitados foram:{numeros}.")