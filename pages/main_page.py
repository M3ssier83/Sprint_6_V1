import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data import TestData
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open(self, url=None): #Открываем главную страницу
        if url is None:
            url = TestData.SCOOTER_MAIN_PAGE
        super().open(url)

    @allure.step("Кликаем по верхней кнопке «Заказать»")
    def click_top_order_button(self): # Кликаем по кнопке "Заказать" вверху страницы
        self.click_element(MainPageLocators.BUTTON_ORDER_TOP)

    @allure.step("Кликаем по нижней кнопке «Заказать»")
    def click_bottom_order_button(self): # Скроллим до нижней кнопки и кликаем по ней
        self.scroll_to_element(self.find_element(MainPageLocators.BUTTON_ORDER_BOTTOM))
        self.click_element(MainPageLocators.BUTTON_ORDER_BOTTOM)

    @allure.step("Открываем вопрос FAQ и получаем ответ: {question_key}")
    def open_question_and_get_answer(self, question_key): # Открываем вопрос FAQ и получаем ответ
        locators = MainPageLocators.QUESTIONS.get(question_key)  # Получаем локаторы вопроса и ответа из словаря
        if not locators:
            raise ValueError(f"Вопрос с ключом '{question_key}' не найден.")
        question_locator = locators["question"]
        answer_locator = locators["answer"]
        question_element = self.find_element(question_locator) # Находим элемент вопроса и скроллим к нему
        self.scroll_to_element(question_element)
        self.wait.until(EC.element_to_be_clickable(question_locator)).click() # Кликаем по вопросу, чтобы открыть ответ
        self.wait.until( # Ждём, пока появится текст ответа
            EC.visibility_of_element_located(answer_locator),
            message=f"Ответ для '{question_key}' не появился")
        return self.find_element(answer_locator).text.strip() # Возвращаем текст ответа, убирая пробелы по краям