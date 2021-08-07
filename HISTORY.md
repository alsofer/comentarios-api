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
- Utilizaremos um repositório de infra para versionar nosso código de terraform e rodaremos com atlantis nas pull requests, dando melhor visibilidade para qualquer alteração no ambiente.
- O 'tfstate' será armazenado em um bucket s3.

# A esteira de CI/CD foi desenvolvida com github actions, o workflow é o seguinte:
- Set up Python
- Install Python Virtual ENV
- Setup Virtual ENV
- Activate and Install Dependencies into Virtual ENV
- Activate venv
- Create Zipfile archive of Dependencies
- Add App to Zip file
- Upload zip file artifact

- Install AWS CLI
- Download Lambda api.zip
- Upload to S3
- Deploy new Lambda

Toda vez que um commit for feito na master, a esteira roda e entrega o aplicativo na estrutura.

# Escopo final
- Ao final teremos uma api completamente funcional e robusta, com capacidade de escalar em momentos críticos e manter o custo baixo que uma lambda function + api gateway podem nos proporcionar.