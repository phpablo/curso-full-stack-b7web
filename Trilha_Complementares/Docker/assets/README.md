# Módulo Introdução ao Docker

## Imagens

- Imagem estática, buildou, tem que rm e buildar denovo pra atualizar, não só restartar
- Ordem no Dockerfile importa
  - Incluir comando para baixar dependencias
- Incluir o .dockerignore ( arquivos pesados ou que quer baixar no container apenas)
- Dá pra tagar a versão da sua imagem

## Volumes
  - Nomeado - Gerenciado pelo próprio docker, banco de dados,uploads
  - Bind Mount, compartilha uma pasta com o host
