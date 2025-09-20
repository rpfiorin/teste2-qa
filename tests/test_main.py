from pages.register_page import RegisterPage

""""
    Caso de teste da reproducao valida no cadastro de conta do cliente, apos
    invocar POM definido
"""
def test_valid_registers(page, test_data: dict, user_password: str):
    register = RegisterPage(page)

    register.access_home()
    register.access_register()

    valid_user_data = test_data["valid_user"]

    register.create_account_without_balance(
        email=valid_user_data["email"],
        name=valid_user_data["fullName"],
        password=user_password
    )
    #page.pause()
    
    register.check_success_account_creation('criada com sucesso')