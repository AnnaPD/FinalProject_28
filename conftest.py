import pytest
from selenium import webdriver


driver = webdriver.Chrome()

@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")

    # Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/')
    # Добавляем ожидание
    driver.implicitly_wait(5)

    yield driver
    driver.quit()
