import re
import time

import pytest
from pytest_selenium import selenium
from selenium import webdriver
from settings import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.auth_page import AuthPage
from selenium.webdriver.common.by import By
from pages.locators import AuthLocators, RegisterLocators
driver = webdriver.Chrome()

# Запускаем в терминале команду:
# pytest -v -s --driver Chrome --driver-path /chromedriver.exe tests/test_registr_page.py


# Тест Кейс № TC-RT-001.
# Форма регистрации. Проверка ввода валидных значений в поля формы регистрации и
# регистрация нового пользователя по email
@pytest.mark.positive
def test_registr_page_valid_email(driver):
    time.sleep(2)
    page = AuthPage(driver)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    time.sleep(2)
    # Заполняем поле "Имя" валидным значением
    page.input_keys(RegisterLocators.REGISTER_FIRSTNAME, valid_firstname)
    # Заполняем поле "Фамилия" валидным значением
    page.input_keys(RegisterLocators.REGISTER_LASTNAME, valid_lastname)
    # Заполняем поле "E-mail или мобильный телефон" валидным значением
    page.input_keys(RegisterLocators.REGISTER_ADDRESS, valid_email_reg)
    # Заполняем поле "Пароль" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD, valid_password_reg)
    # Заполняем поле "Подтверждение пароля" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD_CONFIRM, valid_password_reg_repeat)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(RegisterLocators.REGISTER_BTN)
    time.sleep(2)
    # Определяем элемент, соответствующий форме подтверждения email для регистрации
    email_confirmation = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    time.sleep(2)
    assert email_confirmation.text == 'Подтверждение email', 'Ошибка ввода'
    print(email_confirmation.text)


# Тест Кейс № TC-RT-002.
# Форма регистрации. Проверка ввода валидных значений в поля формы регистрации и
# регистрация нового пользователя по номеру телефона
@pytest.mark.positive
def test_registr_page_valid_phone(driver):
    time.sleep(2)
    page = AuthPage(driver)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    time.sleep(2)
    # Заполняем поле "Имя" валидным значением
    page.input_keys(RegisterLocators.REGISTER_FIRSTNAME, valid_firstname)
    # Заполняем поле "Фамилия" валидным значением
    page.input_keys(RegisterLocators.REGISTER_LASTNAME, valid_lastname)
    time.sleep(2)
    # Заполняем поле "E-mail или мобильный телефон" валидным значением
    page.input_keys(RegisterLocators.REGISTER_ADDRESS, valid_phone_reg)
    # Заполняем поле "Пароль" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD, valid_password_reg)
    # Заполняем поле "Подтверждение пароля" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD_CONFIRM, valid_password_reg_repeat)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(RegisterLocators.REGISTER_BTN)
    # Определяем элемент, соответствующий форме подтверждения email для регистрации
    phone_confirmation = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    time.sleep(2)
    assert phone_confirmation.text == 'Подтверждение телефона', 'Ошибка ввода'
    print(phone_confirmation.text)


# Тест Кейс № TC-RT-003.
# Форма регистрации. Проверка ввода валидных значений в поля формы регистрации и
# регистрация нового пользователя по уже зарегистрированному email
@pytest.mark.negative
def test_registr_page_invalid_email(driver):
    time.sleep(2)
    page = AuthPage(driver)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    time.sleep(2)
    # Заполняем поле "Имя" валидным значением
    page.input_keys(RegisterLocators.REGISTER_FIRSTNAME, valid_firstname)
    # Заполняем поле "Фамилия" валидным значением
    page.input_keys(RegisterLocators.REGISTER_LASTNAME, valid_lastname)
    # Заполняем поле "E-mail или мобильный телефон" не валидным значением
    page.input_keys(RegisterLocators.REGISTER_ADDRESS, invalid_email_reg)
    # Заполняем поле "Пароль" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD, valid_password_reg)
    # Заполняем поле "Подтверждение пароля" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD_CONFIRM, valid_password_reg_repeat)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(RegisterLocators.REGISTER_BTN)
    # Определяем элемент, соответствующий форме подтверждения email для регистрации
    phone_confirmation = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2')
    time.sleep(2)
    assert phone_confirmation.text == 'Учётная запись уже существует'
    print(phone_confirmation.text)


# Тест Кейс № TC-RT-004.
# Форма регистрации. Проверка ввода валидных значений в поля формы регистрации и
# регистрация нового пользователя по уже зарегистрированному номеру телефона
@pytest.mark.negative
def test_registr_page_invalid_phone(driver):
    time.sleep(2)
    page = AuthPage(driver)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    time.sleep(2)
    # Заполняем поле "Имя" валидным значением
    page.input_keys(RegisterLocators.REGISTER_FIRSTNAME, valid_firstname)
    # Заполняем поле "Фамилия" валидным значением
    page.input_keys(RegisterLocators.REGISTER_LASTNAME, valid_lastname)
    # Заполняем поле "E-mail или мобильный телефон" не валидным значением
    page.input_keys(RegisterLocators.REGISTER_ADDRESS, invalid_phone_reg)
    # Заполняем поле "Пароль" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD, valid_password_reg)
    # Заполняем поле "Подтверждение пароля" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD_CONFIRM, valid_password_reg_repeat)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(RegisterLocators.REGISTER_BTN)
    # Определяем элемент, соответствующий форме подтверждения email для регистрации
    phone_confirmation = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div/div/h2')
    time.sleep(2)
    assert phone_confirmation.text == 'Учётная запись уже существует'
    print(phone_confirmation.text)


# Тест Кейс № TC-RT-005.
# Форма регистрации. Проверка ввода не валидных и пограничных значений в поле "Имя" в форме регистрации
@pytest.mark.negative
@pytest.mark.parametrize('firstname', [generation_lower_string(11), generation_upper_string(11),
                                       generation_letters_string(11), generation_digits_string(11),
                                       generation_punctuation_string(11), generation_random_string(5, 6),
                                       generation_specific_string_сyrillic(1), generation_specific_string_сyrillic(2),
                                       generation_specific_string_сyrillic(30), generation_specific_string_сyrillic(31),
                                       generation_specific_string_сhinese_char(11)],
                         ids=["lower_string(11)", "upper_string(11)", "letters_string_11", "digits",
                              "punctuation_string", "random_string", "specific_string_Cyrillic(1)", "specific_string_Cyrillic(2)",
                              "specific_string_Cyrillic(30)", "specific_string_Cyrillic(31)", "specific_string_Chinese_char"])
def test_registr_page_invalid_firstname(selenium, firstname):
    time.sleep(2)
    page = AuthPage(selenium)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    # Заполняем поле "Имя" не валидным значением
    page.input_keys(RegisterLocators.REGISTER_FIRSTNAME, firstname)
    # Заполняем поле "Фамилия" валидным значением
    page.input_keys(RegisterLocators.REGISTER_LASTNAME, valid_lastname)
    time.sleep(2)
    # находим условия, при которых значения поля "Имя" будут не валидными
    if (1 >= len(firstname) <= 30) or (firstname != re.search(r'^[а-яА-ЯеЁ]+$', firstname)):
        incorrect_format = selenium.find_element(By.XPATH,
                                                    '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/span')
        print('Формат заполнения поля "Имя": ', incorrect_format.text)
        assert incorrect_format.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест Кейс № TC-RT-006.
# Форма регистрации. Проверка ввода не валидных и пограничных значений в поле "Фамилия" в форме регистрации
@pytest.mark.negative
@pytest.mark.parametrize('lastname', [generation_lower_string(11), generation_upper_string(11),
                                       generation_letters_string(11), generation_digits_string(11),
                                       generation_punctuation_string(11), generation_random_string(5, 6),
                                       generation_specific_string_сyrillic(1), generation_specific_string_сyrillic(2),
                                       generation_specific_string_сyrillic(30), generation_specific_string_сyrillic(31),
                                       generation_specific_string_сhinese_char(11)],
                         ids=["lower_string(11)", "upper_string(11)", "letters_string_11", "digits",
                              "punctuation_string", "random_string", "specific_string_Cyrillic(1)", "specific_string_Cyrillic(2)",
                              "specific_string_Cyrillic(30)", "specific_string_Cyrillic(31)", "specific_string_Chinese_char"])
def test_registr_page_invalid_lastname(selenium, lastname):
    time.sleep(2)
    page = AuthPage(selenium)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    # Заполняем поле "Фамилия" не валидным значением
    page.input_keys(RegisterLocators.REGISTER_LASTNAME, lastname)
    time.sleep(2)
    # Заполняем поле "Имя" валидным значением
    page.input_keys(RegisterLocators.REGISTER_FIRSTNAME, valid_firstname)
    # находим условия, при которых значения поля "Фамилия" будут не валидными
    if (1 >= len(lastname) <= 30) or (lastname != re.search(r'^[а-яА-ЯеЁ]+$', lastname)):
        incorrect_format = selenium.find_element(By.XPATH,
                                                    '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span')
        print('Формат заполнения поля "Фамилия": ', incorrect_format.text)
        assert incorrect_format.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест Кейс № TC-RT-007.
# Форма регистрации. Проверка ввода не валидных и пограничных значений в поле "Email или телефон" в форме регистрации
@pytest.mark.negative
@pytest.mark.parametrize('login', [generation_lower_string(11), generation_upper_string(11), generation_letters_string(11),
                                   f'{generation_letters_string(260)}@mail.ru', generation_digits_string(11),
                                   generation_punctuation_string(11), generation_random_string(5, 6),
                                   generation_specific_string_сyrillic(1), f'{generation_specific_string_сyrillic(8)}@mail.ru',
                                   generation_specific_string_сyrillic(30), generation_specific_string_сhinese_char(11),
                                   "denis_anna_p@mailru"],
                         ids=["lower_string(11)", "upper_string(11)", "letters_string_11", "mail_260", "digits",
                              "punctuation_string", "random_string", "specific_string_Cyrillic(1)", "mail_Cyrillic",
                              "specific_string_Cyrillic(30)", "specific_string_Chinese_char", "emailru"])
def test_registr_page_invalid_login(selenium, login):
    time.sleep(2)
    page = AuthPage(selenium)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    # Заполняем поле "Email или телефон" не валидным значением
    page.input_keys(RegisterLocators.REGISTER_ADDRESS, login)
    time.sleep(2)
    # Заполняем поле "Пароль" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD, valid_password_reg)
    # находим условия, при которых значения поля "Email или телефон" будут не валидными
    if (login != re.search(r"^\+7 \(\d{3}\) \d{3}-?\d{2}-?\d{2}$", login)) or \
            (login != re.search(r"^\+375 \(\d{3}\) \d{3}-?\d{3}$", login)) or \
            login != re.match(r"[a-zA-Z0-9][a-zA-Z0-9_.-]{1,63}?@[a-zA-Z0-9_.-]{2,63}\.[a-zA-Z]+", login):
        incorrect_format = selenium.find_element(By.XPATH,
                                                    '//*[@id="page-right"]/div/div/div/form/div[3]/span')
        print('Формат заполнения поля "Email или телефон": ', incorrect_format.text)
        assert incorrect_format.text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"


# Тест Кейс № TC-RT-008.
# Форма регистрации. Проверка ввода не валидных и пограничных значений в поле "Пароль" в форме регистрации
@pytest.mark.negative
@pytest.mark.parametrize('password', [generation_lower_string(11), generation_upper_string(11), generation_letters_string(11),
                                      generation_digits_string(11), generation_punctuation_string(11), generation_random_string(4, 3),
                                      generation_random_string(5, 3), generation_random_string(9, 11), generation_random_string(10, 11),
                                      generation_specific_string_сyrillic(11), generation_specific_string_сhinese_char(11)],
                         ids=["lower_string(11)", "upper_string(11)", "letters_string_11", "digits", "punctuation_string",
                              "random_string_7", "random_string_8", "random_string_20", "random_string_21",
                              "specific_string_Cyrillic", "specific_string_Chinese_char"])
def test_registr_page_invalid_password(selenium, password):
    time.sleep(2)
    page = AuthPage(selenium)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    # Заполняем поле "Пароль" не валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD, password)
    time.sleep(2)
    # Заполняем поле "Email или телефон" валидным значением
    page.input_keys(RegisterLocators.REGISTER_ADDRESS, valid_phone_reg)
    # находим условия, при которых значения поля "Пароль" будут не валидными
    if password != re.search(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
        incorrect_format = selenium.find_element(By.XPATH,
                                                    '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span')
        print('Формат заполнения поля "Пароль": ', incorrect_format.text)
        assert incorrect_format.text == "Длина пароля должна быть не менее 8 символов" or \
               "Пароль должен содержать хотя бы одну заглавную букву" or \
               "Пароль должен содержать хотя бы одну строчную букву" or \
               "Длина пароля должна быть не более 20 символов" or \
               "Пароль должен содержать только латинские буквы" or \
               "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"



# Тест Кейс № TC-RT-009.
# Форма регистрации. Проверка ввода не валидного значения в поле "Подтверждение пароля" в форме регистрации
@pytest.mark.negative
def test_registr_page_invalid_pass_repeat(driver):
    time.sleep(2)
    page = AuthPage(driver)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(AuthLocators.AUTH_BTN_REGISTER)
    time.sleep(2)
    # Заполняем поле "Имя" валидным значением
    page.input_keys(RegisterLocators.REGISTER_FIRSTNAME, valid_firstname)
    # Заполняем поле "Фамилия" валидным значением
    page.input_keys(RegisterLocators.REGISTER_LASTNAME, valid_lastname)
    # Заполняем поле "E-mail или мобильный телефон" валидным значением
    page.input_keys(RegisterLocators.REGISTER_ADDRESS, valid_phone_reg)
    # Заполняем поле "Пароль" валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD, valid_password_reg)
    # Заполняем поле "Подтверждение пароля" не валидным значением
    page.input_keys(RegisterLocators.REGISTER_PASSWORD_CONFIRM, invalid_pass_repeat)
    # Находим кнопку "Зарегистрироваться" и кликаем по ней
    page.find_click(RegisterLocators.REGISTER_BTN)
    time.sleep(2)
    # находим условия, при которых значения поля "Подтверждение пароля" будут не валидными
    pass_repeat = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[4]/div[2]/span')
    time.sleep(2)
    assert pass_repeat.text == 'Пароли не совпадают'
    print(pass_repeat.text)

