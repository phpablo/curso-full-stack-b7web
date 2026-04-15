const http = require('http');
const server = http.createServer((req, res) => {
  res.end('Docker rodando Node.js FUNCIONA TREM');
});

server.listen(3000);