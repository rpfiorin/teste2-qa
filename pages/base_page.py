class BasePage:
    def __init__(self, page):
        # define elementos ao instanciar page
        self.page = page
        self.button_go_to_register = page.get_by_text("Registrar")


    """"
        Metodos para acesso dos conteudos presentes antes da autenticacao no 
        BugBank
    """
    def access_home(self):
        self.page.goto('/#')

    def access_registration(self):
        self.button_go_to_register.click()
