from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse
from termcolor import colored


class BasePage(object):
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    #найти элемент и кликнуть по нему
    def find_click(self, by_locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).click()

    # Проверить видимость элемента
    def is_visible(self, by_locator) -> bool:
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    #Ввод данных в строку ввода
    def input_keys(self, by_locator, text):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    #Получить заголовок окна
    def get_windows_title(self, text) -> bool:
        windows_title = WebDriverWait(self.driver, 5).until(EC. title_contains(text))
        return bool(windows_title)

    #Получить  атрибут текст элемента
    def get_text_of_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    #Найти элемент
    def find_one_element(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element

    def find(self, timeout=10):
        """ Find element on the page. """
        element = None
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.by_locator)
            )
        except:
            print(colored('Element not found on the page!', 'red'))
        return element
