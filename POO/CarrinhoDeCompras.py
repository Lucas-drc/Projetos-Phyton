class Produto:
    def __init__(self, nome, preco, setor):
        self.nome = nome
        self.preco = preco
        self.setor = setor
    def exibir(self):
        print(f"Nome: {self.nome} | Preço: {self.preco} | Setor: {self.setor}")

def exibir_menu():
    print("\n=====================")
    print("1 - Adicionar produto")
    print("2 - Listar itens e dar total")
    print("3 - Filtrar por setor")
    print("0 - Sair")
    print("=====================")

def adicionar_produto():
    print("\nCADASTRANDO PRODUTO...")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$"))
    setor = input("Digite o setor do produto: ")
    produto = Produto (nome,preco,setor)
    carrinho.append(produto)
    print(f"Produto {nome} adicionado ao carrinho!")

def listar_produtos():
    if not carrinho:
        print("Não há produtos no carrinho!")
        print("Total do carrinho: R$0.0")
        return
    total = 0
    print("Lista de compras...")
    for produto in carrinho:
        produto.exibir()
        total += produto.preco
    print(f"Valor total do seu carrinho: R$ {total}")

def filtrar_por_setor():
    setor = input("Setor para filtrar: ")
    encontrou = False
    for codigo_produto, produto in enumerate(carrinho, start=1):
        if setor == produto.setor:
            print(f"Código produto: {codigo_produto}")
            produto.exibir()
            encontrou = True
    if not encontrou:
        print(f"Nenhum produto do setor : {setor} foi encontrado no carrinho!")

carrinho = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "0":
        break
    elif opcao =="1":
        adicionar_produto()
    elif opcao =="2":
        listar_produtos()
    elif opcao =="3":
        filtrar_por_setor()
    else:
        print("Opção inválida.")