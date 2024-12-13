# 🧪 Hiring Challenge

## 👨🏻‍💻 Arquitetura

- Api processa o arquivo e dispara para a fila do rabbitMQ as linhas para ser processadas
- Workers recebem a linha e fazem o processo necessário

Com essa arquitetura conseguimos escalar individualmente tanto a API como os Workers

## ⬆️ Fluxo do upload

- Upload do arquivo
- Leitura do arquivo e inserção no rabbitMQ
- O worker processa as messagens do rabbitMQ
- Cada linha é processada
  - Verifica se ja esta no banco de dados
    - Caso ja esteja e marcada como processada, apenas ignora a linha
    - Caso ja estiver porem marcada que nao foi processada, faz o pocessamento
    - Salva no banco de dados

## 📌 Proximos passos

Como é apenas um pequeno projeto oque faria para melhorar

- Controle dos arquivos que foram feito upload (CRUD dos arquivos feito upload)
- Relatório de todas as linhas que foram processadas de um arquivo, quais foram importadas com sucesso e quais não, com a possibilidade de reprocessar as com erro
- Melhorar gestão dos erros (fiz o basico apenas)
- O Arquivo seria salvo num bucket para depois iniciar o processamento passando por status como (Na fila de processamento, Processando (XX%), Finalizado)

## 🔄 Como rodar

No Terminal: `docker compose up -d postgres rabbitmq`

Espere uns 10 segundos para o postgres e rabbitmq dar start nos serviços

Depois: `docker compose up -d app worker` para iniciar a API e os Workers

Acesse `localhost:8080/docs` para acessar o swagger e fazer upload do arquivo

Feito o upload, pode acessar os logs do container do worker para ver o processamento sendo feito

## 📝 Testes

Testes na pasta `/tests`

Foram feitos testes de integração e testes unitários
