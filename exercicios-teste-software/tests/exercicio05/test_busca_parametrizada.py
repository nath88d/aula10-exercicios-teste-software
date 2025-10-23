import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("termo_busca", [
    "Python",
    "Selenium",
    "Pytest",
    "API Testing",
    "Automation"
])
def test_busca_google(chrome_driver, termo_busca):
    driver = chrome_driver
    driver.get("https://www.google.com")

    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    search_box.clear()
    search_box.send_keys(termo_busca)
    search_box.submit()

    wait.until(EC.presence_of_element_located((By.ID, "search")))

    assert termo_busca.lower() in driver.page_source.lower()