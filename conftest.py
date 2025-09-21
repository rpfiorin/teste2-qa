# includes necessarios no projeto
import json
import os
import pytest
from dotenv import load_dotenv
from pages.base_page import BasePage
from playwright.sync_api import Page

# busca arquivo .env
load_dotenv()


@pytest.fixture
def context(browser):
    web_context = browser.new_context(base_url='https://bugbank.netlify.app',
        record_video_dir='videos'
    )
    # gera contexto para poder ser utilizado em todos os testes
    yield web_context
    web_context.close()


@pytest.fixture
def tab(context):
    pages = context.new_page()
    # gera criacao de pagina para ser utilizada em todos os testes
    yield pages

    pages.close()


@pytest.fixture
def web_page(page: Page):
    tab_page = BasePage(page)
    # este codigo serve como um gancho (hook)
    tab_page.access_home()

    yield tab_page


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
            "encontrada. Verifique o conteúdo do arquivo .env")

    return password
