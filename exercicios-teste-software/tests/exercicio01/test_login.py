import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def chrome_driver():
    options = Options()
    options.add_argument("--headless")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


from selenium.webdriver.support import expected_conditions as EC

def test_login_sucesso(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    wait = WebDriverWait(driver, 40)
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("student")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Password123")
    wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
    
    # Espera o URL mudar para indicar login bem-sucedido
    wait.until(EC.url_contains("logged-in-successfully"))
    
    logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Log out']")))
    assert logout_button.is_displayed()



def test_login_usuario_invalido(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    wait = WebDriverWait(driver, 40)
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("incorrectUser")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("Password123")
    wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
    
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "error"))).text
    print("\n🔹 Resposta do site (usuário incorreto):")
    print(error_message)
    
    assert "Your username is invalid!" in error_message


def test_login_senha_invalida(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    wait = WebDriverWait(driver, 40)
    wait.until(EC.presence_of_element_located((By.ID, "username"))).send_keys("student")
    wait.until(EC.presence_of_element_located((By.ID, "password"))).send_keys("incorrectPassword")
    wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
    
    # Espera a mensagem de erro ficar visível
    error_message = wait.until(EC.visibility_of_element_located((By.ID, "error"))).text
    print("\n🔹 Resposta do site (senha incorreta):")
    print(error_message)
    
    assert "Your password is invalid!" in error_message



def test_login_campos_vazios(chrome_driver):
    driver = chrome_driver
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    wait = WebDriverWait(driver, 40)
    wait.until(EC.element_to_be_clickable((By.ID, "submit"))).click()
    
    page_text = wait.until(EC.presence_of_element_located((By.TAG_NAME, "body"))).text
    print("\n🔹 Resposta do site (campos vazios):")
    print(page_text)
    
    assert "Your username is invalid!" in page_text or "Your password is invalid!" in page_text
