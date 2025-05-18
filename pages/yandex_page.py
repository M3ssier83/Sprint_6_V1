import allure
from locators.base_page_locators import BasePageLocators
from data import TestData
from pages.base_page import BasePage

class YandexPage(BasePage):

    @allure.step("Кликаем по логотипу Яндекса")
    def click_logo_yandex(self): # Скроллим вверх и кликаем по логотипу
        self.click_when_clickable(BasePageLocators.LOGO_YANDEX)

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_new_tab(self): # Переключаемся на новую вкладку после открытия
        super().switch_to_new_tab()

    @allure.step("Ожидаем загрузку Dzen")
    def wait_for_load_dzen(self): # Ждём появления dzen.ru в URL
        self.wait_for_url_contains(TestData.YANDEX_DOMAIN)