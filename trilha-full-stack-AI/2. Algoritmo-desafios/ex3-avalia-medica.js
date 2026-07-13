const prompt = require('prompt-sync')()

let pontuacao = 0

console.log('Responda as perguntas com "sim" ou "não".')
const pergunta1 = prompt('Você sente dor no peito? ')
const pergunta2 = prompt('Você sente falta de ar? ')
const pergunta3 = prompt('Você sente tontura? ')
const pergunta4 = prompt('Você sente palpitações? ')
const pergunta5 = prompt('Você sente cansaço extremo? ')

if (pergunta1.toLowerCase() === 'sim') {
    pontuacao += 2
}
if (pergunta2.toLowerCase() === 'sim') {
    pontuacao += 2
}
if (pergunta3.toLowerCase() === 'sim') {
    pontuacao += 1
}
if (pergunta4.toLowerCase() === 'sim') {
    pontuacao += 1
}
if (pergunta5.toLowerCase() === 'sim') { 
    pontuacao += 1
}

console.log(`Sua pontuação é: ${pontuacao}`)
if (pontuacao >= 5) {
    console.log('Você deve procurar um médico imediatamente.')
}else if (pontuacao >= 3) {
    console.log('Você deve procurar um médico em breve.')
}