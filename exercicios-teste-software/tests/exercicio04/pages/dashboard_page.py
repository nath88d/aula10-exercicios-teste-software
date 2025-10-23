from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    LOGOUT_BUTTON = (By.XPATH, "//a[text()='Log out']")
    BODY = (By.TAG_NAME, "body")

    def esta_logado(self):
        return self.esta_visivel(self.LOGOUT_BUTTON)

    def obter_mensagem_boas_vindas(self):
        return self.obter_texto(self.BODY)
