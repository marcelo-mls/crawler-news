# Crawler News

## Descrição:
Este repositório consiste em um desafio de codificação para a função de Engenharia de Dados. Aqui você encontrará uma solução que faz a raspagem dos dados de artigos de um site de notícias, limpa a resposta, armazena no `BigQuery` e os disponibiliza para pesquisa por meio de uma `API`.

<br />

## Desenvolvido com:

- O crawler foi desenvolvido com [`Python`](https://www.python.org/) utilizando as bibliotecas [`requests`](https://pypi.org/project/requests/) e [`parsel`](https://pypi.org/project/parsel/), enquanto para integração com o BigQuery, foram utilizadas as bibliotecas [`google-cloud-bigquery`](https://pypi.org/project/google-cloud-bigquery/) e [`google-auth`](https://pypi.org/project/google-auth/).

- A `API` foi escrita em [`Node.js`](https://nodejs.org/en) com [`Express`](https://expressjs.com/) e [`@google-cloud/bigquery`](https://www.npmjs.com/package/@google-cloud/bigquery) para a parte de integração com o BigQuery.
> O objetivo de desenvolver a API em outra linguagem e não em python (assim como o crawler), foi para demonstrar habilidades técnicas, já que este projeto foi desenvolvido para uma oportunidade de Engenharia de Dados, e `Node.js` representava um diferencial nos requisitos da vaga.

<br />

## Credenciais:
> Na proxíma seção, você encontrará um passo-a-passo de como testar o projeto, porém, antes, é necessário realizar a seguinte preparação:

- Para que tudo funcione corretamente, é necessário ter uma [***Conta de Serviço***](https://cloud.google.com/iam/docs/service-account-overview?hl=pt-br) do `Google Cloud` com as permissões necessárias para leitura e escrita de dados em projeto do `BigQuery`.
- Tendo a [***Conta de Serviço***](https://cloud.google.com/iam/docs/service-account-overview?hl=pt-br), você pode criar uma [***chave de autenticação***](https://cloud.google.com/iam/docs/keys-create-delete?hl=pt-br), que é um arquivo `.json`, no seguinte formato:
```json
{
  "type": "service_account",
  "project_id": "PROJECT_ID",
  "private_key_id": "KEY_ID",
  "private_key": "-----BEGIN PRIVATE KEY-----\nPRIVATE_KEY\n-----END PRIVATE KEY-----\n",
  "client_email": "SERVICE_ACCOUNT_EMAIL",
  "client_id": "CLIENT_ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://accounts.google.com/o/oauth2/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/SERVICE_ACCOUNT_EMAIL"
}
```
- Assim que fizer o download da sua [***chave de autenticação***](https://cloud.google.com/iam/docs/keys-create-delete?hl=pt-br) com as permissões necessárias, você deve renomea-lá para **`sa_gbq_crawler_credentials.json`** (esse, é o nome de arquivo que o crawler espera encontrar quando tentar localizar as credenciais).
- Por fim, insira sua [***chave de autenticação***](https://cloud.google.com/iam/docs/keys-create-delete?hl=pt-br) dentro da pasta ```/crawler/src/credentials``` (é nessa pasta que o crawler espera encontrar as credenciais).

<br />

## Como Instalar:
> ⚠️ Para prosseguir, é necessário ter concluído as etapas da seção **Credenciais**.

Estas instruções fornecerão a você uma cópia completa do projeto instalado e funcionando em sua máquina local, para fins de testes e desenvolvimento.

1. Clone o repositório:
```sh
git clone git@github.com:marcelo-mls/crawler-news.git
```
2. Entre na pasta do repositório que você acabou de clonar:
```sh
cd crawler-news
```
3. Acesse a pasta do `crawler`, instale as dependências e execute o projeto:
```sh
cd crawler
pip install -r requirements.txt
```
**🚀 Agora basta executar o arquivo [`main.py`](./crawler/src/main.py)! 🚀**

<br />

4. Acesse a pasta da `API`, instale as dependências e ligue o servidor:
```sh
cd ../api
npm install
npm run dev
```
5. Acesse o link abaixo em seu navegador para testar a `API` da ferramenta:
> O servidor com a `API` irá rodar na porta **3001**.

[127.0.0.1:3001/articles?keywords=](http://127.0.0.1:3001/articles?keywords=)


<br />


## Rotas da API:

Você pode testar a API com softwares como [`Insomnia`](https://insomnia.rest/download), [`Postman`](https://www.postman.com/) ou [`Thunder Client`](https://www.thunderclient.com/).

  - GET: `'/articles?keywords='`
  > Este _endpoint_ retorna todas as notícias encontradas que possuem a palavra-chave especificada na url.
  > 
  > A busca pela palavra-chave é feita no título, no subtítulo e no conteúdo das notícias.
  >   
  > Para pesquisar por um termo específico, basta inseri-lo no final da url. Neste link de exemplo, a palavara-chave pesquisada foi **China**: [`/articles?keywords=china`](http://127.0.0.1:3001/articles?keywords=china)

<br />

## Demonstração:

<details>
  <summary>
  </summary>
  
  1. #### Projeto do BigQuery vazio
  ![bigquery_vazio](https://github.com/marcelo-mls/crawler-news/assets/102492818/f9df1d25-09e3-4753-8865-ed29de2f3d0f)
  
  2. #### Página da [BBC](https://www.bbc.com/news) no momento em que o crawler foi executado
  ![bbc_news](https://github.com/marcelo-mls/crawler-news/assets/102492818/808e3f57-74bd-4741-8866-730b5e62f662)

  3. #### Crawler rodando e projeto do BigQuery após a execução do Crawler, com a tabela populada.
  ![crawler](https://github.com/marcelo-mls/crawler-news/assets/102492818/53256025-d455-4333-b68b-02d05e20d04b)
  
  4. #### Resultado da API ao buscar pela [notícia que estava em destaque na página da BBC](https://www.bbc.com/news/world-us-canada-65651998)
  ![API](https://github.com/marcelo-mls/crawler-news/assets/102492818/473099c0-1e78-478e-8027-cb1bd4859629)

</details>

<br />

---

Desenvolvido por [Marcelo Marques](https://www.linkedin.com/in/marcelo-mls/), © 2023.
> Teste técnico referente à vaga de Engenheiro de Dados Pleno na [Lima Consulting Group](https://www.limaconsulting.com/).
<div>
  <a href = "https://www.linkedin.com/in/marcelo-mls/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" />
  </a>
  <a href="mailto:marcelo-mls@hotmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Hotmail-0077B5?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</div>
