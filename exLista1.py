produtos = ["Celular", "Computador", "Carregador", "Câmera", "Teclado"]

#print(produtos)

#print(produtos[0])

#print(produtos[-1])

#print(len(produtos))

precosProdutos = [599, 1500, 150, 600, 90]

print (f"O primeiro produto é:{produtos[0]}, e o valor dele é R${precosProdutos[0]}")

produtos.remove("Teclado")
precosProdutos.remove(90)

print(f"A lista de produtos atualizada é:{produtos}. E seus respectivos valores são:{precosProdutos}")

totalProdutos = sum (precosProdutos)

print(f"O valor total dos produtos é de R${totalProdutos}.")

print ("Coloque o produto que você quer comprar.")
print ("Para Celular, digite 1. Para Comuputador, digite 2. Para Carregador, digite 3. Para Câmera, digite 4")

pedido = int (input("Digite o código do produto:"))

if pedido == 1:
    pedido = [produtos[0]]
    preco = [precosProdutos[0]]

elif pedido == 2:
    pedido = [produtos[1]]
    preco = [precosProdutos[1]]

elif pedido == 3:
    pedido = [produtos[2]]
    preco = [precosProdutos[2]]

elif pedido == 4:
    pedido = [produtos[3]]
    preco = [precosProdutos[3]]

else:
    print("Produto não encontrado")
    exit()

print(f"Você selecionou o produto {pedido}, e o valor dele é R${preco}")


valor = float (input("Valor total da compra: R$"))

if valor >100:
    desconto = 0.95

else:
    desconto = 1
   
total = valor * desconto

descontoPercentual = (1 - desconto) * 100
descontoPercentual = round(descontoPercentual, 0)
descontoValor = valor - total

print (f"Sua compra deu R${valor}. Você ganhou {descontoPercentual}% de desconto. O total agora é R${total}. O valor do desconto é de R${descontoValor}")