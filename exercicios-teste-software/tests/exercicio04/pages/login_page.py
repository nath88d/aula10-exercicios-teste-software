from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage

class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")

    def abrir(self):
        self.abrir_url(self.URL)

    def preencher_usuario(self, usuario):
        self.digitar(self.USERNAME_INPUT, usuario)

    def preencher_senha(self, senha):
        self.digitar(self.PASSWORD_INPUT, senha)

    def clicar_login(self):
        self.clicar(self.SUBMIT_BUTTON)

    def fazer_login(self, usuario, senha):
        self.preencher_usuario(usuario)
        self.preencher_senha(senha)
        self.clicar_login()
        return DashboardPage(self.driver)

    def obter_mensagem_erro(self):
        return self.obter_texto(self.ERROR_MESSAGE)
