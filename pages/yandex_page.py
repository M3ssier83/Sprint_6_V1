import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage

class YandexPage(BasePage):

    @allure.step("Кликаем по логотипу Яндекса")
    def click_logo_yandex(self): # Скроллим вверх и кликаем по логотипу
        self.driver.execute_script("window.scrollTo(0, 0);")
        logo = self.wait.until(EC.element_to_be_clickable(BasePageLocators.LOGO_YANDEX))
        self.scroll_to_element(logo)
        logo.click()

    @allure.step("Переключаемся на новую вкладку")
    def switch_to_new_tab(self): # Переключаемся на новую вкладку после открытия
        self.wait.until(lambda driver: len(driver.window_handles) > 1)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    @allure.step("Ожидаем загрузку Dzen")
    def wait_for_load_dzen(self): # Ждём появления dzen.ru в URL
        self.wait.until(EC.url_contains("dzen.ru"))