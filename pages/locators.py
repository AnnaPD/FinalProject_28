from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локаторы для главной страницы
    MAIN_AUTH_TITLE = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    MAIN_LOGO = (By.XPATH, '//*[@id="page-left"]/div')
    MAIN_INFO = (By.XPATH, '//*[@id="app-footer"]/div[1]/div[2]')
    MAIN_PAGE_LEFT = (By.ID, "page-left")
    MAIN_PAGE_RIGHT = (By.ID, "page-right")


class AuthLocators:
    # Локаторы для блока авторизации.
    AUTH_EMAIL = (By.ID, "username")
    AUTH_PASS = (By.ID, "password")
    AUTH_BTN = (By.ID, "kc-login")
    AUTH_BTN_FORGOT_PASSWORD = (By.ID, "forgot_password")
    AUTH_BTN_REGISTER = (By.ID, "kc-register")
    AUTH_BTN_TAB_PHONE = (By.ID, "t-btn-tab-phone")
    AUTH_BTN_TAB_MAIL = (By.ID, "t-btn-tab-mail")
    AUTH_BTN_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    AUTH_BTN_TAB_LS = (By.ID, "t-btn-tab-ls")
    AUTH_ICON_VK = (By.ID, "oidc_vk")
    AUTH_ICON_OK = (By.ID, "oidc_ok")
    AUTH_ICON_MAIL = (By.ID, "oidc_mail")
    AUTH_ICON_GOOGLE = (By.ID, "oidc_google")
    AUTH_ICON_YA = (By.ID, "oidc_ya")
    AUTH_TAB_PLACEHOLDER = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    AUTH_TAB_FORM = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/input[1]')
    AUTH_TAB_LOGIN = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/input[2]')
    FORM_PASSWORD_RECOVERY = (By.XPATH, '//*[@id="page-right"]/div/div/h1')


class RegisterLocators:
    # Локаторы для страницы регистрации.
    REGISTER_FIRSTNAME = (By.NAME, "firstName")
    REGISTER_LASTNAME = (By.NAME, "lastName")
    REGISTER_REGION = (By.CLASS_NAME, "rt-input-container rt-select__input")
    REGISTER_ADDRESS = (By.ID, "address")
    REGISTER_PASSWORD = (By.ID, "password")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "password-confirm")
    REGISTER_BTN = (By.XPATH, "//button[@name='register']")