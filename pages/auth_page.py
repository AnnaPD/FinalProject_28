from .base_page import BasePage
from .locators import MainPageLocators
from .locators import AuthLocators
from .locators import RegisterLocators

import os

class MainPage(BasePage):

    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
        driver.get(url)
# находим элементы на странице
        self.auth_title = driver.find_element(*MainPageLocators.MAIN_AUTH_TITLE)
        self.logo = driver.find_element(*MainPageLocators.MAIN_LOGO)
        self.info = driver.find_element(*MainPageLocators.MAIN_INFO)
        self.page_left = driver.find_element(*MainPageLocators.MAIN_PAGE_LEFT)
        self.page_right = driver.find_element(*MainPageLocators.MAIN_PAGE_RIGHT)


class AuthPage(BasePage):

    def __init__(self, driver,timeout=10):
        super().__init__(driver, timeout)
        url = os.getenv("LOGIN_URL") or "https://b2c.passport.rt.ru/"
        driver.get(url)
#находим элементы на странице
        self.email = driver.find_element(*AuthLocators.AUTH_EMAIL)
        self.password = driver.find_element(*AuthLocators.AUTH_PASS)
        self.btn = driver.find_element(*AuthLocators.AUTH_BTN)
        self.btn_forgot_password = driver.find_element(*AuthLocators.AUTH_BTN_FORGOT_PASSWORD)
        self.btn_register = driver.find_element(*AuthLocators.AUTH_BTN_REGISTER)
        self.btn_tab_phone = driver.find_element(*AuthLocators.AUTH_BTN_TAB_PHONE)
        self.btn_tab_mail = driver.find_element(*AuthLocators.AUTH_BTN_TAB_MAIL)
        self.btn_tab_login = driver.find_element(*AuthLocators.AUTH_BTN_TAB_LOGIN)
        self.btn_tab_ls = driver.find_element(*AuthLocators.AUTH_BTN_TAB_LS)
        self.icon_vk = driver.find_element(*AuthLocators.AUTH_ICON_VK)
        self.icon_ok = driver.find_element(*AuthLocators.AUTH_ICON_OK)
        self.icon_mail = driver.find_element(*AuthLocators.AUTH_ICON_MAIL)
        self.icon_google = driver.find_element(*AuthLocators.AUTH_ICON_GOOGLE)
        self.icon_ya = driver.find_element(*AuthLocators.AUTH_ICON_YA)
        self.tab_placeholder = driver.find_element(*AuthLocators.AUTH_TAB_PLACEHOLDER)
        self.tab_form = driver.find_element(*AuthLocators.AUTH_TAB_FORM)
        self.tab_login = driver.find_element(*AuthLocators.AUTH_TAB_LOGIN)
        self.password_recovery = driver.find_element(*AuthLocators.FORM_PASSWORD_RECOVERY)

    # ввод данных в поле username
    def enter_email(self, value):
        self.email.send_keys(value)
    # ввод данных в поле Пароль
    def enter_pass(self, value):
        self.password.send_keys(value)
    # кликнуть кнопку Войти
    def btn_click(self):
        self.btn.click()
    # кликнуть ссылку Забыл пароль
    def btn_forgot_password_click(self):
        self.btn_forgot_password.click()
    # кликнуть ссылку Зарегистрироваться
    def btn_register_click(self):
        self.btn_register.click()
    # кликнуть вкладку Телефон в форме авторизации
    def btn_tab_phone_click(self):
        self.btn_tab_phone.click()
    # кликнуть вкладку Почта в форме авторизации
    def btn_tab_mail_click(self):
        self.btn_tab_mail.click()
    # кликнуть вкладку Логин в форме авторизации
    def btn_tab_login_click(self):
        self.btn_tab_login.click()
    # кликнуть вкладку Лицевой счёт в форме авторизации
    def btn_tab_ls_click(self):
        self.btn.click()

    def icon_vk_click(self):
        self.icon_vk.click()

    def icon_ok_click(self):
        self.icon_ok.click()

    def icon_mail_click(self):
        self.icon_mail.click()

    def icon_google_click(self):
        self.icon_google.click()

    def icon_ya_click(self):
        self.icon_ya.click()

