# Проверка перехода на Дзен в новой вкладке при клике по логотипу "Яндекс".

import allure
from pages.main_page import MainPage
from pages.yandex_page import YandexPage
from data import TestData

@allure.title("Проверка перехода на Dzen по клику на логотип Яндекса")
def test_yandex_logo_redirects_to_dzen(driver):
    driver.get(TestData.SCOOTER_ORDER_PAGE) # Переходим на страницу оформления заказа
    main_page = MainPage(driver)
    main_page.close_cookie_popup() # Закрываем попап с куками
    yandex_page = YandexPage(driver)
    yandex_page.click_logo_yandex() # Кликаем по логотипу Яндекса
    yandex_page.switch_to_new_tab() # Переключаемся на новую вкладку
    yandex_page.wait_for_load_dzen() # Ждём загрузки Dzen
    actual_url = yandex_page.get_current_url() # Проверяем URL
    assert "dzen.ru" in actual_url, f"Ожидался переход на Dzen, но текущий URL: {actual_url}"