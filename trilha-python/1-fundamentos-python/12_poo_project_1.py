# Enunciado - Projeto 1 de POO (Gestão de Clientes e LTV):
# [x] Criar a classe base `Pessoa` com os atributos `nome` e `idade`
# [x] Criar a classe `Cliente` herdando de `Pessoa`
# [x] Adicionar os atributos `email` e `ltv` (convertido para float) em `Cliente` usando `super().__init__`
# [x] Criar uma lista `clientes` e cadastrar instâncias de `Cliente`
# [x] Percorrer a lista exibindo o nome e o LTV de cada cliente
# [x] Calcular e exibir a soma do LTV total de todos os clientes
# [x] Criar getter e setter para o atributo `ltv` da classe `Cliente`, garantindo que o valor seja sempre positivo


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, email, ltv):
        super().__init__(nome, idade)
        self.email = email
        self.ltv = ltv  # Passa pelo @ltv.setter para validar já na criação!

    # GETTER: Permite LER o atributo privado (__ltv) usando cliente.ltv
    @property
    def ltv(self):
        return self.__ltv

    # SETTER: Permite ALTERAR o atributo privado (__ltv) com regra de validação
    @ltv.setter
    def ltv(self, value):
        if float(value) < 0:
            raise ValueError("LTV deve ser um valor positivo.")
        self.__ltv = float(value)


clientes = []

clientes.append(Cliente("Pedro", 20, "pedro@pedro.com", 1300))
clientes.append(Cliente("Gohan", 12, "gohan@gohan.com", 14950))

ltv_total = 0
for cliente in clientes:
    print(f"Nome: {cliente.nome}, LTV de R$ {cliente.ltv}")
    ltv_total += cliente.ltv

print(f"LTV Total: R$ {ltv_total}")
