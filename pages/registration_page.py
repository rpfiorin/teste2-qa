import time
# Includes necessários para modelagem
from pages.base_page import BasePage
from playwright.sync_api import expect


class RegistrationPage(BasePage):
    def __init__(self, page):
        # Carrega mapeamento pelo arquivo base_page ao instanciar esta page.
        super().__init__(page)

        self.button_back = page.locator("#btnBackButton")
        # Mapeia todos os elementos a interagir.
        self.input_email = page.get_by_placeholder("Informe seu e-mail")
        self.input_name = page.get_by_placeholder("Informe seu Nome")
        self.input_password = page.get_by_placeholder("Informe sua senha")
        self.input_repeat_password = page.get_by_placeholder(
            "Informe a confirmação da senha")
        self.button_eye = page.get_by_alt_text("Icon Close Eye")
        self.button_eye_confirmation = page.locator(".login__eye")
        self.toggle_balance = page.locator("#toggleAddBalance")
        self.button_register = page.get_by_role("button", name="Cadastrar")
        self.text_modal = page.locator("#modalText")

    def create_account_without_money(self, email='', name='', password=''):
        expect(self.button_back).to_be_visible()
        # Preenche campos após verificar formulário e registra conta s/ saldo.
        self.input_email.last.fill(email)
        self.input_name.fill(name)
        self.input_password.last.fill(password)
        self.input_repeat_password.fill(password)

        self.button_eye.nth(1).click()
        self.button_register.click()

    def create_account_with_money(self, email='', name='', password=''):
        expect(self.button_back).to_be_visible()
        # Preenche campos após verificar formulário e registra conta c/ saldo.
        self.input_email.last.fill(email)
        self.input_name.fill(name)
        
        self.input_password.last.fill(password)
        self.input_repeat_password.fill(password)

        self.button_eye_confirmation.last.click()
        self.toggle_balance.click()
        self.button_register.click()

    def check_success_account_creation(self, message):
        # Ligeira pausa para constar exibição do modal na evidência em vídeo.
        time.sleep(0.5)

        expect(self.text_modal).to_contain_text(message)

    def check_failure_account_creation(self, page, message):
        # Ligeira pausa para constar exibição do alerta na evidência em vídeo.
        time.sleep(0.5)

        expect(page.get_by_text(message)).to_be_visible()
