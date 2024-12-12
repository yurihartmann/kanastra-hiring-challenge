# Hiring Challenge

## Fluxo do upload

- Upload do arquivo
- Leitura do arquivo e inserção no rabbitMQ
- A Thread da task para processar as messagens do rabbitMQ processa as linhas
- Cada linha é processada
  - Verifica se ja esta no banco de dados
    - Caso ja esteja e marcada como processada, apenas ignora a linha
    - Caso ja estiver porem marcada que nao foi processada, faz o pocessamento
    - Salva no banco de dados


## Proximos passos

Como é apenas um pequeno projeto oque faria para melhorar

- Controle dos arquivos que foram feito upload (CRUD dos arquivos feito upload)
- Relatorio de todas as linhas que foram processadas de um arquivo, quais foram importadas com sucesso e quais não, com a possibilidade de reprocessar as com erro
- Melhorar gestão dos erros (fiz o basico apenas)
- O Arquivo seria salvo num bucket
- A API seria rodada em um container e os workers para processar as linhas em outro container (para ter a possibilidade de escalar)


## Como rodar

No Terminal: `docker compose up -d`

Acesse `localhost:8080/docs` para acessar o swagger e fazer upload do arquivo

Feito o upload, pode acessar os logs do container da aplicação para ver o processamento sendo feito
