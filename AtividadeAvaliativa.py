#### Cenário: Loja automotiva, com venda de produtos e serviços. 
#### Quando usuário entrar, perguntar serviço ou produto?
#### Mostrar lista de produtos conforme solicitação do usuário
#### Mensagem final do que o usuário quer

produtos = ["Shampoo", "Cera", "Pretinho"]
precosProdutos = [40, 35, 20]

######

servicos = ["Troca de óleo", "Troca de Pneu", "Limpeza AC"]
precosServicos = [120, 400, 80]
##### 

codigoItem = []
pedidoItem = []
itemPreco = []

print("Bem vindo à nossa loja!")

##### 
ordemServico = (input(f"""
O que você deseja?
Digite 1 para produtos e 2 para serviços! 
"""))

if ordemServico == "1":
    for indiceProduto, produto in enumerate(produtos):
        precoProduto = precosProdutos[indiceProduto] 
        print(f"""
Produto: {produto} 
Código: {indiceProduto}
Valor: R${precoProduto:.2f}""")    

elif ordemServico == "2":
    for indiceServico, servico in enumerate(servicos):
        precoServico = precosServicos[indiceServico] 
        print(f"Serviço: {servico} custa R${precoServico}")
        print(f"""
Produto: {servico} 
Código: {indiceServico}
Valor: R${precoServico:.2f}

""")
        

else:
    print("Opção inválida! Selecione novamente!")
    exit()

codigoItem = int(input(f"Digite o código do que você deseja:"))

if ordemServico == "1":
    pedidoItem = produtos[codigoItem]
    itemPreco = precosProdutos[codigoItem]
    print(f"""
Produto escolhido: {pedidoItem}
Subtotal: R${itemPreco:.2f}
""")
        
elif ordemServico == "2":
    pedidoItem = servicos[codigoItem]
    itemPreco = precosServicos[codigoItem]
    print(f"""
Produto escolhido: {pedidoItem}
Subtotal: R${itemPreco:.2f}
""")


if itemPreco >= 300:
    itemPreco = round(itemPreco * 0.90,2)

mensagem = f"""
===============================================
Item:{pedidoItem}
Total:R${itemPreco:.2f}
===============================================
"""

print(mensagem)