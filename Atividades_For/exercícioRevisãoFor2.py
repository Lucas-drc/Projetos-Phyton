produtos = ["computador", "teclado","mouse", "cadeira"]
precos = [1800, 400, 50, 700]

for preco, produto in enumerate(produtos):
    if precos[preco] < 500:
        preco_ajustado = round(precos[preco] * 1.10,2)
        print(f"Produto: {produto} custava R${precos[preco]} e subiu para R${preco_ajustado}")
    else:
        print(f"Produto: {produto} custa R${precos[preco]}.")