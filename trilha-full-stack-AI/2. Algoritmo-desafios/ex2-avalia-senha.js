const prompt = require('prompt-sync')()

let senha = prompt('Digite uma senha: ')

if (senha.length >= 8) {
  console.log('Senha forte.')
} else {
  console.log('Senha fraca.')
}
