// calculadora acima 100 + 10% de desconto, acima de 200 reais 20% de desconto
// preco * (desconto / 100 )
const prompt = require('prompt-sync')()

let valor = Number(prompt('digite o valor: '))

if (valor >= 200) {
  let desconto = valor * (20 / 100)
  console.log('Vc recebeu 20% de desconto. Valor da compra foi R$' + (valor - desconto))
} else if (valor >= 100) {
  let desconto = valor * (10 / 100)
  console.log('Vc recebeu 10% de desconto. Valor da compra foi R$' + (valor - desconto))
} else {
  console.log('Valor da compra foi R$' + valor)
}