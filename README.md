<p align="center">
  <img src="./.github/logo.png" alt="poster">
</p>

# Teste prático - Automação Web com Playwright em Python

## Preparação 📍
1. Primeiramente, clone este projeto com opção HTTPS ou SSH.
2. A automação foi desenvolvida em cima da versão 3.10 do python, logo, certifique-se de estar com esta versão em seu SO ou instale-a pelo diretório 'py' (caso utilize Windows). Para linux, consulte o respectivo procedimento de acordo com a distribuição utilizada.

## Configuração 🏁
3. Considerando ambiente Windows, após instalado, abra o projeto no CMD e execute: python -m venv .venv, seguido de: .venv\Scripts\activate

 E depois de ativado o ambiente virtual: _pip install -r requirementes.txt_ (para baixar o playwright pra python) 
                                         seguido de _playwright install_ (para configurar as dependências do playwright).

## Execução ⚡
4. Confira a massa de teste que deseja ser utilizada (com os dados do cliente), no arquivo data/user.json 

   Para executar de forma assistida: _pytest --browser=nome-browser-suportado_
   
   Para executar em modo headless: _pytest -o "addopts=" --browser=nome-browser-suportado_

OBS: na pasta 'videos' temos as evidências dos casos de teste executados.
Toda a codificação do projeto foi comentada para fácil compreensão e documentação (exceto arquivos gerados automaticamente), de acordo com boas práticas da PEP 8. 


Enjoy it!
