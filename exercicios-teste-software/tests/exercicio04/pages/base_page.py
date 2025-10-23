import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def abrir_url(self, url):
        self.driver.get(url)
        time.sleep(1)

    def encontrar_elemento(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def digitar(self, locator, texto):
        elemento = self.encontrar_elemento(locator)
        elemento.clear()
        elemento.send_keys(texto)
        time.sleep(0.3)

    def clicar(self, locator):
        elemento = self.wait.until(EC.element_to_be_clickable(locator))
        elemento.click()
        time.sleep(0.5)

    def obter_texto(self, locator):
        try:
            elemento = self.wait.until(EC.visibility_of_element_located(locator))
            return elemento.text
        except:
            return ""

    def esta_visivel(self, locator):
        try:
            elemento = self.wait.until(EC.visibility_of_element_located(locator))
            return elemento.is_displayed()
        except:
            return False
