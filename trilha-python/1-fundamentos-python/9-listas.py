# lista com string

# lista = ['gohan','goku','vegeta','bulma']
# lista = [
#     'gohan',
#     'goku',
#     'vegeta',
#     'bulma'
# ]

usuarios = [
    {"nome": "Gohan","idade":90},
    {"nome":"Goku","idade":80}
]

for usuario in usuarios:
    print(f"Nome dele é {usuario["nome"]} e tem {usuario["idade"]} anos.")

refeicao = {
    "Café": "Pao com ovo",
    "fruta": "banana"
},
{
    "Almoço": "Arroz com feijão",
    "fruta": "maçã"
}

for refeicao in refeicao:
    print(f"Para o café da manhã tenho o {refeicao["Café"]} e a fruta do dia é {refeicao["fruta"]}") 

