import random
numero_secreto = random.randint(1,10)
palpite = 0 #precisou colocar uma variável 0 para inicializar o while
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número (1 a 10): "))
    if palpite != numero_secreto:
         print("Errou! Tente novamente")
    
       
    tentativas = tentativas + 1


if tentativas == 1:
    print(f"Acertou! Você acertou de primeira!.")
else:
    print(f"Acertou! Você tentou {tentativas} vezes.")