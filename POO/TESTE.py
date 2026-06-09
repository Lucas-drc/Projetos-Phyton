class Produto:
    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
    def exibir(self):
        print(f"Produto: {self.nome} | Preço: R${self.preco} | Quantidade: {self.qtd}x ")

produto_1 = Produto("Arroz", 7.99, 20)

produto_2 = Produto("Feijão",
                    10.00,
                      20)
produto_1.exibir()