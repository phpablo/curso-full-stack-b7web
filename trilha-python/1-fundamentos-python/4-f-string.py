# =====================================================
# F-STRINGS (Formatted String Literals) - Python 3.6+
# =====================================================

# 1. BÁSICO - Interpolação de Variáveis
# =====================================================
print("=" * 50)
print("1. BÁSICO - Interpolação de Variáveis")
print("=" * 50)

name = "Alice"
age = 30
city = "São Paulo"

print(f"Hello, {name}! You are {age} years old.")
print(f"I live in {city}.")

# 2. EXPRESSÕES DENTRO DE F-STRINGS
# =====================================================
print("\n" + "=" * 50)
print("2. EXPRESSÕES E CÁLCULOS")
print("=" * 50)

x = 10
y = 5

print(f"x = {x}, y = {y}")
print(f"x + y = {x + y}")
print(f"x * y = {x * y}")
print(f"x / y = {x / y}")
print(f"x > y? {x > y}")

# 3. FORMATAÇÃO DE NÚMEROS
# =====================================================
print("\n" + "=" * 50)
print("3. FORMATAÇÃO DE NÚMEROS")
print("=" * 50)

price = 19.99
discount = 0.15

# Casas decimais
print(f"Preço: R$ {price:.2f}")

# Inteiro (sem casas decimais)
print(f"Quantidade: {int(price)}")

# Notação científica
large_number = 1234567.89
print(f"Número grande: {large_number:.2e}")

# Porcentagem
percentage = 0.85
print(f"Taxa de sucesso: {percentage:.1%}")

# 4. PREENCHIMENTO E ALINHAMENTO
# =====================================================
print("\n" + "=" * 50)
print("4. PREENCHIMENTO E ALINHAMENTO")
print("=" * 50)

# Alinhado à esquerda
product = "Notebook"
print(f"|{product:<15}|")

# Alinhado à direita
print(f"|{product:>15}|")

# Centralizado
print(f"|{product:^15}|")

# Preenchimento com zeros
code = 42
print(f"Código: {code:05d}")

# 5. MÉTODOS E FUNÇÕES DENTRO DE F-STRINGS
# =====================================================
print("\n" + "=" * 50)
print("5. MÉTODOS E FUNÇÕES")
print("=" * 50)

text = "python"
print(f"Minúscula: {text}")
print(f"Maiúscula: {text.upper()}")
print(f"Capitalizada: {text.capitalize()}")
print(f"Comprimento: {len(text)}")

lista = [1, 2, 3, 4, 5]
print(f"Soma: {sum(lista)}")
print(f"Média: {sum(lista) / len(lista):.2f}")

# 6. DICIONÁRIOS EM F-STRINGS
# =====================================================
print("\n" + "=" * 50)
print("6. DICIONÁRIOS E OBJETOS")
print("=" * 50)

person = {
    "name": "Bob",
    "age": 25,
    "profession": "Developer"
}

print(f"Nome: {person['name']}")
print(f"Idade: {person['age']}")
print(f"Profissão: {person['profession']}")

# 7. DEBUG COM F-STRINGS (Python 3.8+)
# =====================================================
print("\n" + "=" * 50)
print("7. DEBUG COM F-STRINGS (Python 3.8+)")
print("=" * 50)

user = "Carlos"
score = 95

# O especificador '=' mostra a expressão e o valor
print(f"{user=}")
print(f"{score=}")
print(f"{x + y=}")

# 8. EXEMPLOS PRÁTICOS
# =====================================================
print("\n" + "=" * 50)
print("8. EXEMPLOS PRÁTICOS")
print("=" * 50)

# Tabela de preços
products = [
    {"name": "Mouse", "price": 50.00},
    {"name": "Teclado", "price": 150.00},
    {"name": "Monitor", "price": 800.00}
]

print(f"{'Produto':<15} {'Preço':>10}")
print("-" * 25)
for product in products:
    print(f"{product['name']:<15} R$ {product['price']:>8.2f}")

# Informações pessoais
print("\n" + "=" * 50)
email = "alice@example.com"
birth_year = 1994
current_year = 2026

print(f"Email: {email}")
print(f"Idade: {current_year - birth_year} anos")
print(f"Usuário: {email.split('@')[0]}")

# 9. COMPARAÇÃO COM OUTROS MÉTODOS
# =====================================================
print("\n" + "=" * 50)
print("9. COMPARAÇÃO COM OUTROS MÉTODOS")
print("=" * 50)

name = "Diana"
age = 28

# F-string (moderno e eficiente)
print(f"F-string: {name} tem {age} anos")

# .format() (método antigo)
print(".format(): {} tem {} anos".format(name, age))

# String concatenation (lento e verboso)
print("Concatenação: " + name + " tem " + str(age) + " anos")