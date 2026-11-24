def calc_imc(peso,altura):
    return peso / (altura * altura)

altura = float(input("altura: "))
peso = float(input("peso: "))
imc = calc_imc(peso,altura)
if imc < 19.1:
    print('abaixo do peso')
elif imc >= 19.1 and imc <= 25.8:
    print('normal')
elif imc >= 25.9 and imc <= 27.3:
    print("pouco acima do peso")
elif imc >= 27.4 and imc <= 32.3:
    print("Acima do peso")
else:
    print("Obesidade")