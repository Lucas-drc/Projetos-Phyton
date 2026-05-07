frutas = ["maçã","banana","laranja","uva","tangerina"]

fruta_favorita = input ("Qual sua fruta favorita?: ")

if fruta_favorita not in frutas:
    print("Sua fruta favorita não está na lista!")
    exit()

#Para cada posição (índice) e fruta na lista numerada de frutas
for posicao, fruta in enumerate(frutas):
    if fruta == fruta_favorita:
        posicao_fruta_favorita = posicao
        break

print (f"Minha fruta favorita está na posição índice {posicao_fruta_favorita}")


