// Receber uma lista de notas de números inteiros
// calcular e retornar a média das notas
// classificar as notas: 0-4 - ruim; 5-7 - bom; 8-10 - ótimo

const minhasNotas = [7, 5, 5]

// Retorna a média das notas. Lista vazia devolve 0 (evita 0/0 = NaN).
function media(notas) {
    if (notas.length === 0) return 0

    let i = 0
    let soma = 0
    while (i < notas.length) {
        soma = soma + notas[i]
        i = i + 1
    }
    return soma / notas.length
}

// Faixas sem buraco: em cadeia de if, o limite inferior já está
// garantido pelo teste anterior. Serve para nota inteira e para média decimal.
function classificar(nota) {
    if (nota < 0 || nota > 10) return 'nota inválida'
    if (nota < 5) return 'ruim'
    if (nota < 8) return 'bom'
    return 'ótimo'
}

// Classifica cada nota individualmente, devolvendo um rótulo por nota.
function classificarTodas(notas) {
    const rotulos = []
    let i = 0
    while (i < notas.length) {
        rotulos.push(classificar(notas[i]))
        i = i + 1
    }
    return rotulos
}

// A exibição decide o formato; o cálculo devolve o valor cheio.
// Arredondar antes de classificar mudaria o resultado.
function relatorio(notas) {
    if (notas.length === 0) {
        console.log('Nenhuma nota informada.')
        return
    }

    const resultadoMedia = media(notas)

    console.log(`Notas: ${notas.join(', ')}`)
    console.log(`A média das notas é: ${resultadoMedia.toFixed(1)}`)
    console.log(`A classificação é: ${classificar(resultadoMedia)}`)
    console.log(`Classificação de cada nota: ${classificarTodas(notas).join(', ')}`)
}

relatorio(minhasNotas)

// Casos de teste dos limites: decimal na antiga faixa vazia,
// lista vazia, decimal isolado e nota fora do intervalo válido.
const casosDeTeste = [[8, 7, 7], [], [4.5], [11]]

let c = 0
while (c < casosDeTeste.length) {
    console.log('---')
    relatorio(casosDeTeste[c])
    c = c + 1
}
