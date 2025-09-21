from pages.registration_page import RegistrationPage


""""
    Caso de teste da reproducao valida no cadastro de conta sem saldo, apos 
    acessar formulario de registro, carregando fixtures como parametro
"""

def test_valid_register_without_money(page, web_page, test_data, user_password):
    web_page = RegistrationPage(page)
    web_page.access_registration()

    valid_user_data = test_data["valid_user"]

    web_page.create_account_without_money(
        email=valid_user_data["email"],
        name=valid_user_data["fullName"],
        password=user_password
    )
    # page.pause()
    web_page.check_success_account_creation('criada com sucesso')


""""
    Caso de teste da reproducao valida no cadastro de conta com saldo, apos 
    acessar formulario de registro, carregando fixtures como parametro
"""

def test_valid_register_with_money(page, web_page, test_data, user_password):
    web_page = RegistrationPage(page)
    web_page.access_registration()

    valid_user_data = test_data["valid_user"]

    web_page.create_account_with_money(
        email=valid_user_data["email"],
        name=valid_user_data["fullName"],
        password=user_password
    )
    # page.pause()
    web_page.check_success_account_creation('criada com sucesso')


""""
    Caso de teste da reproducao invalida no cadastro de conta (sem saldo), apos 
    acessar formulario de registro, carregando fixtures como parametro
"""

def test_invalid_register(page, web_page, test_data, user_password):
    web_page = RegistrationPage(page)
    web_page.access_registration()

    valid_user_data = test_data["invalid_user"]

    web_page.create_account_without_money(
        email=valid_user_data["email"],
        name=valid_user_data["fullName"],
        password=user_password
    )
    # page.pause()
    web_page.check_failure_account_creation(page, 'Formato inválido')
