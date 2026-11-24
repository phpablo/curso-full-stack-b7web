let form = document.querySelector('form')
let input = document.querySelector("#input");
let botao = document.querySelector("#btn");

function sendMessage(text) {
  let textSanitized = text.trim();
  if (textSanitized.length > 0) {
    console.log(textSanitized);
  }
}

form.addEventListener('submit', (e)=> {
  e.preventDefault()
  sendMessage(input.value)
  input.value = ''
  input.focus()
})  