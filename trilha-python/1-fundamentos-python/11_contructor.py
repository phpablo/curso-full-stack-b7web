class Product:
    def __init__(self,name,preco):
        self.nome = name
        self.preco = preco
    def resumir(self):
        print(f"O produto {self.nome} custa R${self.preco}")


p1 = Product('Coca', 2)
p1.resumir()
