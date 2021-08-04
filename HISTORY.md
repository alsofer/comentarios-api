# Requisitos
- A api precisa ser performática
- Simples
- Fácil gerenciamento, features

# Qual linguagem se encaixa melhor?
- Python

# Em qual ambiente rodaria
- Lambda function hospedando o código puro, API Gateway na frente para lidar com as requests.

# Porque?
- O Lambda function é uma solução simples, barata e robusta, lidaria com essa necessidade tranquilamente e aguenta altas cargas de trabalho em horário de pico de uso da API. Sem contar que o billing é feito por 'Milhões de requests'.

# Como construiremos?
- Utilizaremos um repositório de infra para versionar nosso código de terraform e rodaremos com atlantis & infracost nas pull requests, dando melhor visibilidade para qualquer alteração no ambiente.
- O 'tfstate' será armazenado em um bucket s3.

# Segurança
- A api terá autenticação e toda vez que o código for alterado, passará pelo scan do SonarQube para análise de código.
- Conta da AWS para gerenciamento possuirá acesso por IAM, sem contas genéricas.

# A esteira
- A esteira de CI/CD será desenvolvida totalmente pelo github, deixando nosso projeto leve e sem dependências de servidor durante o processo.

# Escopo final
- Ao final teremos uma api completamente funcional e robusta, com capacidade de escalar em momentos críticos e manter o custo baixo que uma lambda function + api gateway podem nos proporcionar.