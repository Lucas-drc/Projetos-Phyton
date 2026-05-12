produtos = ["Celular", "Computador", "Carregador", "Câmera", "Teclado"]
precos = [599, 1500, 150, 600, 90]
quantidade = [12, 3, 4, 21, 5]
posicao = [1, 2, 3, 4, 5]
subtotais = []

for indice, produto in enumerate(produtos):
    preco = precos[indice] 
    qtde = quantidade[indice] 
    lugar = posicao[indice] 
    subtotal = (preco * qtde)
    subtotais.append(subtotal)
    mensagem = f"""
    ---------------------//---------------------
    Produto: {produto}
    Quantidade = {qtde}
    Valor unitário = R${preco}
    Estante = {lugar}
    Subtotal = R${subtotal}
    ---------------------//---------------------
    """
    print (mensagem)

total = sum(subtotais)

print (f"O total de produtos é de R${total}.")

