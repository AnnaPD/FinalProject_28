import time

import pytest
from pytest_selenium import selenium
from selenium import webdriver
from settings import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By
from pages.locators import AuthLocators
driver = webdriver.Chrome()

# Запускаем в терминале команду:
# pytest -v -s --driver Chrome --driver-path /chromedriver.exe tests/test_auth_page.py


# Тест Кейс № TC-RT-001.
# Форма авторизации. Проверка переключения таба  при вводе эл.почты, логина или лицевого счёта в форме Телефон
@pytest.mark.positive
@pytest.mark.parametrize('phone', [valid_email_auth, generation_random_string(3,6), valid_personal_account_auth],
                         ids=["email", "login", "personal_account"])
def test_tab_phone(selenium, phone):
    time.sleep(2)
    page = AuthPage(selenium)
    page.btn_tab_phone.click()
    page.enter_email(phone)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    time.sleep(2)
    # находим значение аттрибута, соответствующее форме Телефон
    form_phone = page.tab_form.get_attribute('value')
    print('Значение таба формы ТЕЛЕФОН: ', form_phone)
   # таб выбора аутентификации меняется автоматически на форму Почта, Логин или Лицевой счёт.
    # Значение аттрибутов этих форм не соответствует значению аттрибута формы Телефон.
    assert form_phone != 'PHONE'


# Тест Кейс № TC-RT-002
# Форма авторизации. Проверка переключения таба  при вводе телефона, логина или лицевого счёта в форме Почта
@pytest.mark.positive
@pytest.mark.parametrize('mail', [valid_phone_auth, generation_random_string(3,6), valid_personal_account_auth],
                         ids=["phone", "login", "personal_account"])
def test_tab_email(selenium, mail):
    time.sleep(2)
    page = AuthPage(selenium)
    page.btn_tab_mail.click()
    page.enter_email(mail)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    time.sleep(2)
    # находим значение аттрибута, соответствующее форме Почта
    form_email = page.tab_form.get_attribute('value')
    print('Значение таба формы ПОЧТА: ', form_email)
    # таб выбора аутентификации меняется автоматически на форму Телефон, Логин или Лицевой счёт.
    # Значение аттрибутов этих форм не соответствует значению аттрибута формы Почта.
    assert form_email != 'EMAIL'


# Тест Кейс № TC-RT-003
# Форма авторизации. Проверка переключения таба  при вводе телефона, почты или лицевого счёта в форме Логин
@pytest.mark.positive
@pytest.mark.parametrize('login', [valid_phone_auth, valid_email_auth, valid_personal_account_auth],
                         ids=["phone", "email", "personal_account"])
def test_tab_login(selenium, login):
    time.sleep(2)
    page = AuthPage(selenium)
    page.btn_tab_login.click()
    page.enter_email(login)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    time.sleep(2)
    # находим значение аттрибута, соответствующее форме Логин
    form_login = page.tab_form.get_attribute('value')
    print('Значение таба формы ЛОГИН: ', form_login)
    # таб выбора аутентификации меняется автоматически на форму Телефон, Почта или Лицевой счёт.
    # Значение аттрибутов этих форм не соответствует значению аттрибута формы Логин.
    assert form_login != 'LOGIN'


# Тест Кейс № TC-RT-004
# Форма авторизации. Проверка переключения таба  при вводе телефона, почты или логина в форме Лицевой счёт
@pytest.mark.positive
@pytest.mark.parametrize('ls', [valid_phone_auth, valid_email_auth, generation_random_string(3,6)],
                         ids=["phone", "email", "login"])
def test_tab_ls(selenium, ls):
    time.sleep(2)
    page = AuthPage(selenium)
    page.btn_tab_ls.click()
    page.enter_email(ls)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    time.sleep(2)
    # находим значение аттрибута, соответствующее форме Лицевой счёт
    form_ls = page.tab_form.get_attribute('value')
    print('Значение таба формы ЛИЦЕВОЙ СЧЁТ: ', form_ls)
    # таб выбора аутентификации меняется автоматически на форму Телефон, Почта или Логин.
    # Значение аттрибутов этих форм не соответствует значению аттрибута формы Лицевой счёт.
    assert form_ls != 'LS'


# Тест Кейс № TC-RT-005
# Форма авторизации. Проверка ввода валидных и не валидных значений в поле Мобильный телефон в форме авторизации
@pytest.mark.positive
@pytest.mark.parametrize('number', [valid_phone_auth, generation_lower_string(11), generation_upper_string(11),
                                    generation_letters_string(11), generation_digits_string(9),
                                    generation_digits_string(10), generation_digits_string(11),
                                    generation_digits_string(12), generation_punctuation_string(10),
                                    generation_random_string(3, 6), generation_specific_string_сyrillic(11),
                                    generation_specific_string_сhinese_char(11)],
                         ids=["phone", "lower_string", "upper_string", "letters_string", "digits(9)", "digits(10)",
                              "digits(11)", "digits(12)", "punctuation_string", "random_string",
                              "specific_string_Cyrillic", "specific_string_Chinese_char"])
def test_tab_phone_user(selenium, number):
    time.sleep(2)
    page = AuthPage(selenium)
    page.btn_tab_phone.click()
    page.enter_email(number)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    time.sleep(2)
    # находим значение аттрибута, соответствующее форме Телефон
    form_phone = page.tab_form.get_attribute('value')
    print('Значение таба формы ТЕЛЕФОН: ', form_phone)
    # находим условия, при которых цифровые значения будут не валидными
    if (0 < len(number) < 10 and number.isdigit()) or len(number) == 0:
        incorrect_format_number = selenium.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
        print('Формат телефона: ', incorrect_format_number.text)
        assert incorrect_format_number.text == "Неверный формат телефона"
    # находим валидные значения для поля Мобильный телефон
    assert form_phone == 'PHONE'


# Тест Кейс № TC-RT-006
# Форма авторизации. Проверка ввода валидных и не валидных значений в поле Электронная почта в форме авторизации
@pytest.mark.positive
@pytest.mark.parametrize('email', [valid_email_auth, f'{generation_lower_string(8)}@mail.ru', generation_lower_string(11),
                                   f'{generation_upper_string(8)}@mail.ru', generation_upper_string(11),
                                   f'{generation_letters_string(8)}@mail.ru', f'{generation_letters_string(255)}@mail.ru',
                                   generation_letters_string(11), generation_digits_string(10), generation_punctuation_string(8),
                                   generation_random_string(3, 6), generation_specific_string_сyrillic(8),
                                   generation_specific_string_сhinese_char(8)],
                             ids=["email", "lower_string@mail.ru", "lower_string", "upper_string@mail.ru", "upper_string",
                                  "letters_string@mail.ru", "letters_string-255", "letters_string", "digits(10)",
                                  "punctuation_string", "random_string", "specific_string_Cyrillic", "specific_string_Chinese_char"])
def test_tab_email_user(selenium, email):
    time.sleep(2)
    page = AuthPage(selenium)
    page.btn_tab_mail.click()
    page.enter_email(email)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    time.sleep(2)
    # находим значение аттрибута, соответствующее форме Почта
    form_email = page.tab_form.get_attribute('value')
    print('Значение таба формы ПОЧТА: ', form_email)
    # находим валидные значения для поля Электронная почта
    assert form_email == 'EMAIL'


# Тест Кейс № TC-RT-007
# Форма авторизации. Проверка ввода валидных и не валидных значений в поле Логин в форме авторизации
@pytest.mark.positive
@pytest.mark.parametrize('login', [valid_email_auth, generation_lower_string(11), generation_upper_string(11),
                                   generation_letters_string(255), generation_letters_string(11), generation_digits_string(15),
                                   generation_punctuation_string(8), generation_random_string(5, 6),
                                   generation_specific_string_сyrillic(7), generation_specific_string_сhinese_char(9)],
                         ids=["email", "lower_string", "upper_string", "letters_string_255", "letters_string", "digits",
                              "punctuation_string", "random_string", "specific_string_Cyrillic", "specific_string_Chinese_char"])
def test_tab_login_user(selenium, login):
    time.sleep(2)
    page = AuthPage(selenium)
    page.btn_tab_login.click()
    page.enter_email(login)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    time.sleep(2)
    # находим значение аттрибута, соответствующее форме Логин
    form_login = page.tab_form.get_attribute('value')
    print('Значение таба формы ЛОГИН: ', form_login)
    # находим валидные значения для поля Логин
    assert form_login == 'LOGIN'


# Тест Кейс № TC-RT-008
# Форма авторизации. Проверка ввода валидных и не валидных значений в поле Лицевой счёт в форме авторизации
@pytest.mark.positive
@pytest.mark.parametrize('ls', [valid_email_auth, generation_lower_string(11), generation_upper_string(11),
                                generation_letters_string(255), generation_letters_string(11),
                                generation_digits_string(11), generation_digits_string(12),
                                generation_digits_string(13), generation_punctuation_string(8),
                                generation_random_string(5, 6), generation_specific_string_сyrillic(7),
                                generation_specific_string_сhinese_char(9)],
                         ids=["email", "lower_string", "upper_string", "letters_string_255", "letters_string",
                              "digits_string(11)", "digits_string(12)", "digits_string(13)", "punctuation_string",
                              "random_string", "specific_string_Cyrillic", "specific_string_Chinese_char"])
def test_tab_ls_user(selenium, ls):
    time.sleep(2)
    page = AuthPage(selenium)
    page.btn_tab_ls.click()
    page.enter_email(ls)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    time.sleep(2)
    # находим значение аттрибута, соответствующее форме Лицевой счёт
    form_ls = page.tab_form.get_attribute('value')
    print('Значение таба формы ЛИЦЕВОЙ СЧЁТ: ', form_ls)
    # находим условия, при которых цифровые значения будут не валидными
    if (0 < len(ls) < 12 and ls.isdigit()) or len(ls) == 0:
        incorrect_format_ls = selenium.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
        print('Формат лицевого счёта: ', incorrect_format_ls.text)
        assert incorrect_format_ls.text == "Проверьте, пожалуйста, номер лицевого счета"
    # находим валидные значения для поля Лицевой счёт
    assert form_ls == 'LS'


# Тест Кейс № TC-RT-009
# Форма авторизации. Авторизация по валидному номеру телефона, валидной электронной почте и валидному паролю.
# (проверить авторизацию по логину и лицевому счёту нет возможности из-за отсутствия данных)
@pytest.mark.positive
@pytest.mark.parametrize('authpositive', [valid_phone_auth, valid_email_auth],
                         ids=['valid_phone', 'valid_email'])
def test_auth_page_valid_data(selenium, authpositive):
    time.sleep(2)
    page = AuthPage(selenium)
    page.enter_email(authpositive)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    page.btn_click()
    time.sleep(2)
    assert page.get_relative_link() == '/account_b2c/page', "Ошибка ввода"
    print(page.get_relative_link())


# Тест Кейс № TC-RT-010
# Форма авторизации. Авторизация по не валидному номеру телефона, не валидной электронной почте и валидному паролю.
@pytest.mark.negative
@pytest.mark.parametrize('authnegative', [generation_digits_string(11), f'{generation_letters_string(8)}@mail.ru'],
                         ids=['invalid_phone', 'invalid_email'])
def test_auth_page_invalid_data(selenium, authnegative):
    time.sleep(2)
    page = AuthPage(selenium)
    page.enter_email(authnegative)
    time.sleep(2)
    page.enter_pass(valid_password_auth)
    page.btn_click()
    time.sleep(2)
    incorrect_data = selenium.find_element(By.ID, 'form-error-message')
    assert incorrect_data.text == 'Неверный логин или пароль' or 'Неверно введен текст с картинки'
    print(incorrect_data.text)


# Тест Кейс № TC-RT-011
# Форма авторизации. Переход по кнопке "Забыл пароль"

@pytest.mark.positive
def test_auth_page_forgot_password(driver):
    time.sleep(2)
    page = AuthPage(driver)
    time.sleep(2)
    # Находим кнопку "Забыл пароль" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_FORGOT_PASSWORD)
    time.sleep(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/reset-credentials'
    print(page.get_relative_link())


# Тест Кейс № TC-RT-012
# Форма авторизации. Переход на форму авторизации через социальную сеть "ВКонтакте"
@pytest.mark.positive
def test_auth_page_vk(driver):
    time.sleep(2)
    page = AuthPage(driver)
    time.sleep(2)
    # Находим кнопку "ВКонтакте" и кликаем по ней
    page.find_click(AuthLocators.AUTH_ICON_VK)
    time.sleep(2)
    assert page.get_relative_link() == '/authorize'
    print(page.get_relative_link())


# Тест Кейс № TC-RT-013
# Форма авторизации. Переход на форму авторизации через социальную сеть "Одноклассники"
@pytest.mark.positive
def test_auth_page_ok(driver):
    time.sleep(2)
    page = AuthPage(driver)
    time.sleep(2)
    # Находим кнопку "Одноклассники" и кликаем по ней
    page.find_click(AuthLocators.AUTH_ICON_OK)
    time.sleep(2)
    assert page.get_relative_link() == '/dk'
    print(page.get_relative_link())


# Тест Кейс № TC-RT-014
# Форма авторизации. Переход на форму авторизации через социальную сеть "Мой мир"
@pytest.mark.positive
def test_auth_page_mail(driver):
    time.sleep(2)
    page = AuthPage(driver)
    time.sleep(2)
    # Находим кнопку "Мой мир" и кликаем по ней
    page.find_click(AuthLocators.AUTH_ICON_MAIL)
    time.sleep(2)
    assert page.get_relative_link() == '/oauth/authorize'
    print(page.get_relative_link())


# Тест Кейс № TC-RT-015
# Форма авторизации. Переход на форму авторизации через социальную сеть "GOOGLE"
@pytest.mark.positive
def test_auth_page_google(driver):
    time.sleep(2)
    page = AuthPage(driver)
    time.sleep(2)
    # Находим кнопку "GOOGLE" и кликаем по ней
    page.find_click(AuthLocators.AUTH_ICON_GOOGLE)
    time.sleep(2)
    assert page.get_relative_link() == '/o/oauth2/auth/identifier'
    print(page.get_relative_link())


# Тест Кейс № TC-RT-016
# Форма авторизации. Переход на форму регистрации по кнопке "Зарегистрироваться"
@pytest.mark.positive
def test_regist_btn(driver):
    time.sleep(2)
    page = AuthPage(driver)
    time.sleep(2)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    time.sleep(2)
    assert page.get_relative_link() == '/auth/realms/b2c/login-actions/registration'
    print(page.get_relative_link())