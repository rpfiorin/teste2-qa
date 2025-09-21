from pages.registration_page import RegistrationPage


def test_valid_register_without_money(page, web_page, test_data, user_password):
    """"
        CT-01: Validar cadastro de conta sem saldo 
        
        Objetivo
            Verificar se o sistema permite o cadastro de um novo cliente com
            dados válidos mas sem saldo, resultando em uma mensagem de sucesso.

        Pre-condições:
        - Acessar tela de registro.

        Resultado esperado:
        - Um modal de sucesso deve aparecer informando que a conta foi criada.
    """
    web_page = RegistrationPage(page)
    web_page.access_registration()

    valid_user_data = test_data["valid_user"]

    web_page.create_account_without_money(
        email=valid_user_data["email"],
        name=valid_user_data["fullName"],
        password=user_password
    )
    web_page.check_success_account_creation('criada com sucesso')

def test_valid_register_with_money(page, web_page, test_data, user_password):
    """"
        CT-02: Validar cadastro de conta com saldo 
        
        Objetivo
            Verificar se o sistema permite o cadastro de um novo cliente com
            dados válidos e saldo, resultando em uma mensagem de sucesso.

        Pré-condições:
        - Acessar tela de registro.

        Resultado esperado:
        - Um modal de sucesso deve aparecer informando que a conta foi criada.
    """
    web_page = RegistrationPage(page)
    web_page.access_registration()

    valid_user_data = test_data["valid_user"]

    web_page.create_account_with_money(
        email=valid_user_data["email"],
        name=valid_user_data["fullName"],
        password=user_password
    )
    web_page.check_success_account_creation('criada com sucesso')

def test_invalid_register(page, web_page, test_data, user_password):
    """"
        CT-03: Validar cadastro de conta invalida
        
        Objetivo
            Verificar se o sistema permite o cadastro de um novo cliente com
            dados inválidos, resultando em uma mensagem de sucesso.

        Pre-condições:
        - Acessar tela de registro.

        Resultado esperado:
        - Um alerta de erro deve aparecer na página.
    """
    web_page = RegistrationPage(page)
    web_page.access_registration()

    valid_user_data = test_data["invalid_user"]

    web_page.create_account_without_money(
        email=valid_user_data["email"],
        name=valid_user_data["fullName"],
        password=user_password
    )
    web_page.check_failure_account_creation(page, 'Formato inválido')
