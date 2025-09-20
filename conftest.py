import pytest
import json
import os
from dotenv import load_dotenv

# buscar arquivo .env
load_dotenv()


@pytest.fixture
def context(browser):
    web_context = browser.new_context(
        base_url='https://bugbank.netlify.app',
        record_video_dir='videos'
    )
    # gera contexto para poder ser utilizado em todos os testes
    yield web_context
    web_context.close()


@pytest.fixture
def page(context):
    web_page = context.new_page()
    # gera criacao de pagina para ser utilizada em todos os testes
    yield web_page
    web_page.close()


"""
    com scope='session', os arquivos abaixo sao lidos apenas uma vez para todas 
    as execucoes dos testes
"""


@pytest.fixture(scope="session")
def test_data():
    # carrega dados do arquivo JSON para testa-los.
    with open("data/user.json", encoding="utf-8") as f:
        data = json.load(f)

    # retorna os dados carregados como um dicionario
    return data


@pytest.fixture(scope="session")
def user_password():
    password = os.getenv("PASSWORD_TO_REGISTER")
    # valida busca da senha a cadastrar por meio da variavel de ambiente
    if not password:
        pytest.fail(
            "Erro: A variável de ambiente 'PASSWORD_TO_REGISTER' não foi "
            "encontrada. Verifique o arquivo .env")

    return password
