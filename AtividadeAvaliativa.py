#### Cenário: Loja automotiva, com venda de produtos e serviços. 
#### Quando usuário entrar, perguntar serviço ou produto?
#### Mostrar lista de produtos conforme solicitação do usuário
#### Mensagem final do que o usuário quer

produtos = ["Shampoo", "Cera", "Pretinho"]
precosProdutos = [40, 35, 20]
######

servicos = ["Troca de óleo", "Troca de Pneu", "Limpeza AC"]
precosServicos = [120, 150, 80]
##### 


print("Bem vindo à nossa loja!")

##### 
ordemServico = (input(f"""O que você deseja? Produtos ou Serviços? 
Digite 1 para produtos e 2 para serviços! 
"""))

if ordemServico == "1":
    for indiceProduto, produto in enumerate(produtos):
        precoProduto = precosProdutos[indiceProduto] 
        print(f"Produto: {produto} custa R${precoProduto}")
elif ordemServico == "2":
    for indiceServico, servico in enumerate(servicos):
        precoServico = precosServicos[indiceServico] 
        print(f"Serviço: {servico} custa R${precoServico}")
else:
    print("Opção inválida! Selecione novamente!")



