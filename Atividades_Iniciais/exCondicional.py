valor = float (input("Digite o valor do pedido: "))


"""

Regra de negócio:
==> Se a venda for até 100 reais, dê 5% de desconto.
==> Se a venda for entre 100,01 e 299 reais, dê 10% de desconto.
==> Se a venda for acima de 300 reais, dê 15% de desconto.

"""


if valor <= 100:
    desconto = 0.95

elif valor >100 and valor <299.99:
    desconto = 0.90

else:
    desconto = 0.85
   
total = valor * desconto

descontoPercentual = (1 - desconto) * 100
descontoPercentual = round(descontoPercentual, 0)
descontoValor = valor - total

#print ("Valor total foi de: R$",total, ". Seu desconto foi de: ", descontoPercentual, "%")

print (f"Sua compra deu R${valor}. Você ganhou {descontoPercentual}% de desconto. O total agora é R${total}. O valor do desconto é de R${descontoValor}")