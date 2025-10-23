import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

@pytest.fixture
def chrome_driver():
    options = Options()
    options.add_argument("--headless")
    service = Service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


# Teste 1: Login correto
def test_login_sucesso(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.abrir()
    dashboard = login_page.fazer_login("student", "Password123")

    mensagem = dashboard.obter_mensagem_boas_vindas()
    print("\n🔹 Resposta (login correto):")
    print(mensagem)

    assert "Congratulations" in mensagem or "successfully logged in" in mensagem
    assert dashboard.esta_logado()


# Teste 2: Usuário incorreto
def test_login_usuario_invalido(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.abrir()
    login_page.fazer_login("incorrectUser", "Password123")
    mensagem = login_page.obter_mensagem_erro()

    print("\n🔹 Resposta (usuário incorreto):")
    print(mensagem)
    assert "Your username is invalid!" in mensagem


# Teste 3: Senha incorreta
def test_login_senha_invalida(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.abrir()
    login_page.fazer_login("student", "incorrectPassword")
    mensagem = login_page.obter_mensagem_erro()

    print("\n🔹 Resposta (senha incorreta):")
    print(mensagem)
    assert "Your password is invalid!" in mensagem


# Teste 4: Campos vazios
def test_login_campos_vazios(chrome_driver):
    login_page = LoginPage(chrome_driver)
    login_page.abrir()
    login_page.clicar_login()
    mensagem = login_page.obter_mensagem_erro()

    print("\n🔹 Resposta (campos vazios):")
    print(mensagem)
    assert "Your username is invalid!" in mensagem or "Your password is invalid!" in mensagem
