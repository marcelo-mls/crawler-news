## Desafio Lima Consulting Group
> Teste técnico referente à vaga de Engenheiro de Dados na [Lima](https://www.limaconsulting.com/).

<br />

# News Crawler

## Descrição:
Este repositório consiste em um desafio de codificação para a função de Engenharia de Dados. Aqui você encontrará uma solução que faz a raspagem dos dados de artigos de um site de notícias, limpa a resposta, armazena no `BigQuery` e os disponibiliza para pesquisa por meio de uma `API`.

<br />

## Desenvolvido com:

O crawler foi desenvolvido com [`Python`](https://www.python.org/) utilizando as bibliotecas [`requests`](), [`parsel`](), [`google-cloud-bigquery`]() e [`google-auth`]().

A API foi escrita em [`Node.js`](https://nodejs.org/en) com [`Express`](https://expressjs.com/) e [`@google-cloud/bigquery`]().
> O objetivo de desenvolver a API em outra linguagem e não em python (assim como o crawler), foi para demonstrar habilidades técnicas com uma tecnologia que representa um diferencial nos requisitos da vaga.

<br />

## Demonstração:

<details>
  <summary>
  </summary>
  
  - #### Raspando as noticias
  ![]()

  - #### Site de notícias
  ![]()

  - #### Inserindo no BigQuery
  ![]()
  
  - #### Consultando a API
  ![]()

</details>

<br />

## Como Instalar:

Estas instruções fornecerão a você uma cópia completa do projeto instalado e funcionando em sua máquina local para fins de teste e desenvolvimento.

1. Clone o repositório:
```sh
git clone git@github.com:marcelo-mls/crawler-news.git
```
2. Entre na pasta do repositório que você acabou de clonar:
```sh
cd crawler-news
```
3. Acesse as pastas de `crawler` e `api`, instale as dependências e inicie o projeto:
```sh
cd crawler
pip install -r requirements.txt
python3 -m ...
```
```sh
cd ..
```
```sh
cd api
npm install
npm run dev
```
4. Acesse o link abaixo em seu navegador para testar a api da ferramenta
[127.0.0.1:3001/articles?keywords=](http://127.0.0.1:3001/articles?keywords=)

> O servidor com a API irá rodar na porta **3001**.

<br />

## Credenciais:


<br />

## Rotas da API:

Você pode testar a API com softwares como [`Insomnia`](https://insomnia.rest/download), [`Postman`](https://www.postman.com/) ou [`Thunder Client`](https://www.thunderclient.com/)

  - GET: `'/articles?keywords='`
  > Este _endpoint_ ...


<br />

---

Desenvolvido por [Marcelo Marques](https://www.linkedin.com/in/marcelo-mls/), © 2023.

<div>
  <a href = "https://www.linkedin.com/in/marcelo-mls/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="Linkedin" />
  </a>
  <a href="mailto:marcelo-mls@hotmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Hotmail-0077B5?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
  </a>
</div>
