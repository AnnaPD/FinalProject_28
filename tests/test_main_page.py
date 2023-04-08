import pages.auth_page
from pages.auth_page import MainPage
from pages.auth_page import AuthPage
# from pages.elements import WebElement
from pages.locators import MainPageLocators
from pages.locators import AuthLocators
import time
import pytest

# Запускаем в терминале команду:
# pytest -v --driver Chrome --driver-path /chromedriver.exe tests/test_main_page.py

# Тест Кейс № TC-RT-001
# Продуктовый слоган и логотип Ростелеком отображается на странице авторизации
@pytest.mark.positive
def test_logo_on_page(driver):
    # Разворачиваем окно браузера
    driver.maximize_window()
    page = MainPage(driver)
    # Устанавливаем видимость слогана на странице авторизации
    logotip = page.is_visible(MainPageLocators.MAIN_LOGO)
    assert logotip == True


# Тест Кейс № TC-RT-002
# Вспомогательная информация для клиента отображается на странице авторизации
@pytest.mark.positive
def test_info_on_page(driver):
    # Разворачиваем окно браузера
    driver.maximize_window()
    page = MainPage(driver)
    # Устанавливаем видимость информации на странице авторизации
    info = page.is_visible(MainPageLocators.MAIN_INFO)
    assert info == True


# Тест Кейс № TC-RT-003
# Форма авторизации отображается на странице авторизации
@pytest.mark.positive
def test_title_auth_on_page(driver):
    # Разворачиваем окно браузера
    driver.maximize_window()
    main_page = MainPage(driver)
    auth_page = AuthPage(driver)
    # Устанавливаем видимость формы авторизации на странице авторизации
    title_auth = main_page.get_text_of_element(MainPageLocators.MAIN_AUTH_TITLE)
    assert title_auth == 'Авторизация'
    assert auth_page.btn_tab_phone.get_attribute("id") == "t-btn-tab-phone"
    assert auth_page.btn_tab_mail.get_attribute("id") == "t-btn-tab-mail"
    assert auth_page.btn_tab_login.get_attribute("id") == "t-btn-tab-login"
    assert auth_page.btn_tab_ls.get_attribute("id") == "t-btn-tab-ls"
    assert auth_page.email.get_attribute("id") == "username"
    assert auth_page.password.get_attribute("id") == "password"


# Тест Кейс № TC-RT-004
# Проверяем корректность отображения элементов авторизации на странице браузера
@pytest.mark.negative
def test_correct_visible_of_elements_auth(driver):
    # Разворачиваем окно браузера
    driver.maximize_window()
    page = MainPage(driver)
    # Получаем атрибут текста левой части страницы (должна отображаться форма авторизации)
    title_auth = page.get_text_of_element(MainPageLocators.MAIN_PAGE_LEFT)
    # Определяем, соответствует ли текст формы авторизации тексту, расположенному в левой части страницы
    assert title_auth == 'Авторизация'


# Тест Кейс № TC-RT-005
# Проверяем корректность отображения элементов слогана компании на странице браузера
@pytest.mark.negative
def test_correct_visible_of_elements_logo(driver):
    # Разворачиваем окно браузера
    driver.maximize_window()
    page = MainPage(driver)
    # Получаем атрибут текста правой части страницы (должен отображаться слоган)
    title_logo = page.get_text_of_element(MainPageLocators.MAIN_PAGE_RIGHT)
    # Определяем, соответствует ли текст формы слогана компании тексту, расположенному в правой части страницы
    assert title_logo == 'Личный кабинет'


# Тест Кейс № TC-RT-006
# Проверяем корректность отображения элементов вспомогательной информации на странице браузера
@pytest.mark.negative
def test_correct_visible_of_elements_info(driver):
    # Разворачиваем окно браузера
    driver.maximize_window()
    page = MainPage(driver)
    # Получаем атрибут текста правой части страницы (должна отображаться информация для клиента)
    title_info = page.get_text_of_element(MainPageLocators.MAIN_PAGE_RIGHT)
    # Определяем, соответствует ли текст информации для клиента тексту, расположенному в правой части страницы
    assert title_info == 'Продолжая использовать наш сайт, вы даете согласие на обработку файлов'


