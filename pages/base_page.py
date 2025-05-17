import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from locators.base_page_locators import BasePageLocators
from data import TestData

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открытие страницы по URL: {url}")
    def open(self, url): # Открываем страницу по переданному URL
        self.driver.get(url)

    @allure.step("Поиск элемента по локатору: {locator}")
    def find_element(self, locator): # Ждём пока элемент появится в DOM и возвращаем его
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step("Клик по элементу: {locator}")
    def click_element(self, locator): #  Кликаем по элементу
        self.find_element(locator).click()

    @allure.step("Ввод текста: {text} в элемент: {locator}")
    def input_text(self, locator, text): # # Находим элемент, очищаем поле, вводим текст
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    @allure.step("Прокрутка до элемента")
    def scroll_to_element(self, element): # Скроллим страницу, чтобы элемент был виден
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Проверка видимости элемента по локатору: {locator}")
    def is_element_displayed(self, locator): # Проверяем, отображается ли элемент на странице, если нет — возвращаем False
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Закрытие попапа cookie")
    def close_cookie_popup(self): # Кликаем по кнопке закрытия попапа куки
        self.click_element(BasePageLocators.COOKIE_CLOSE_BUTTON)

    @allure.step("Клик по логотипу Самоката")
    def click_logo_scooter(self): # Кликаем по логотипу Самоката
        self.click_element(BasePageLocators.LOGO_SCOOTER)

    @allure.step("Ожидание загрузки страницы по адресу: {url}")
    def wait_for_load_url(self, url): # Ждём, пока URL страницы станет нужным, если таймаут — кидаем ошибку
        try:
            self.wait.until(EC.url_to_be(url))
        except TimeoutException:
            raise Exception(f"Страница {url} не загрузилась вовремя.")

    @allure.step("Получение текущего URL")
    def get_current_url(self): # Возвращаем текущий URL страницы
        return self.driver.current_url

    @allure.step("Ожидаем загрузку главной страницы")
    def wait_for_load_main_page(self): # Ждём загрузки главной страницы
        self.wait_for_load_url(TestData.SCOOTER_MAIN_PAGE)

    @allure.step("Ожидание загрузки страницы оформления")
    def wait_for_load_order_page(self): # Ждём загрузки страницы оформления заказа
        self.wait_for_load_url(TestData.SCOOTER_ORDER_PAGE)