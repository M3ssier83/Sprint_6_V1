import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
from pages.base_page import BasePage
from data import TestData
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Открываем страницу заказа самоката")
    def open_order_page(self): # Открываем страницу заказа самоката
        self.open(TestData.SCOOTER_ORDER_PAGE)

    @allure.step("Заполняем форму заказа: имя={first_name}, фамилия={second_name}, адрес={address}, метро={metro_station}, телефон={phone_number}")
    def fill_user_info(self, first_name, second_name, address, metro_station, phone_number): # Заполняем форму заказа
        self.input_text(OrderPageLocators.INPUT_NAME, first_name)
        self.input_text(OrderPageLocators.INPUT_SURNAME, second_name)
        self.input_text(OrderPageLocators.INPUT_ADDRESS, address)
        self.input_text(OrderPageLocators.INPUT_PHONE, phone_number)
        self.select_metro_station(metro_station) # Отдельная логика выбора станции метро

    @allure.step("Выбор станции метро: {metro_station}")
    def select_metro_station(self, metro_station): # Выбираем станцию метро
        self.input_text(OrderPageLocators.INPUT_METRO, metro_station)
        locator = (By.XPATH, OrderPageLocators.METRO_OPTION_TEMPLATE.format(metro_station))
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.scroll_to_element(element)
            element.click()
        except TimeoutException:
            raise Exception(f"Не удалось найти или кликнуть по станции метро: {metro_station}")

    @allure.step("Переход к следующему шагу")
    def go_to_next_step(self): # Кликаем по кнопке "Далее"
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Установка завтрашней даты аренды") # Вот эту конструкцию целиком и полностью написала GPT, ибо реализовать его самостоятельно я не смогла Т_Т
    def select_tomorrow_date(self): # Вычисляем завтрашнюю дату
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_day = tomorrow.day
        tomorrow_month = tomorrow.month
        self.click_element(OrderPageLocators.INPUT_DATE) # Нажимаем на поле выбора даты, чтобы открыть календарь
        current_month = datetime.now().month # Если завтрашний месяц отличается от текущего — нажимаем "вперёд"
        if tomorrow_month != current_month:
            next_button = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__navigation--next")))
            next_button.click()
        xpath_variants = [ # Пробуем кликнуть по нужному числу
            f"//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='{tomorrow_day}']",
            f"//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='{str(tomorrow_day).zfill(2)}']"
        ]
        for xpath in xpath_variants:
            try:
                locator = (By.XPATH, xpath)
                date_element = self.wait.until(EC.element_to_be_clickable(locator))
                self.scroll_to_element(date_element) # Прокручиваем до нужной даты
                date_element.click() # Кликаем по дате
                return
            except TimeoutException:
                continue
        raise Exception(f"Не удалось выбрать завтрашнюю дату: {tomorrow.strftime('%d %B %Y')}")


    @allure.step("Выбор срока аренды: {period}")
    def select_rent_period(self, period): # Нажимаем на выпадающий список срока аренды
        rent_element = self.wait.until(EC.element_to_be_clickable(OrderPageLocators.RENT_PERIOD))
        self.scroll_to_element(rent_element)
        rent_element.click()
        period_map = { # Находим нужный вариант и нажимаем на него
            "2 дня": "двое суток",
            "3 дня": "трое суток"
        }
        period_text = period_map.get(period, period)
        locator = (By.XPATH, OrderPageLocators.RENT_PERIOD_OPTION_TEMPLATE.format(period_text))
        option = self.wait.until(EC.element_to_be_clickable(locator))
        option.click()

    @allure.step("Выбор цвета самоката: {color}")
    def select_scooter_color(self, color):  # Выбираем цвет самоката: чёрный или серый
        locator = OrderPageLocators.COLOR_BLACK if color == "black" else OrderPageLocators.COLOR_GREY
        element = self.find_element(locator)
        self.scroll_to_element(element)
        element.click()

    @allure.step("Ввод комментария курьеру: {comment}")
    def input_comment(self, comment): # Вводим комментарий в поле для курьера
        self.input_text(OrderPageLocators.COMMENT_FIELD, comment)

    @allure.step("Подтверждение и оформление заказа")
    def confirm_order(self): # Подтверждение оформления заказа
        self.click_element(OrderPageLocators.ORDER_BUTTON) # Нажимаем кнопку "Заказать"
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON) # Подтверждаем оформление заказа во всплывающем окне
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE)) # Ждём, когда появится сообщение об успешном заказе

    @allure.step("Ожидаем появление окна об успешном заказе")
    def wait_for_load_successful_order(self): # Явно ждём появления окна успешного оформления
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE))

    @allure.step("Проверка отображения подтверждения успешного заказа")
    def successful_order_is_displayed(self): # Проверяем, что окно об успешном заказе действительно отображается
        return self.is_element_displayed(OrderPageLocators.SUCCESS_MESSAGE)