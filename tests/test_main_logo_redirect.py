# Проверка перехода на главную страницу "Самоката" при клике по логотипу "Самокат".

import allure
from data import TestData

@allure.title('Проверка перехода на главную страницу "Самоката" при клике по логотипу "Самокат"')
def test_scooter_logo_redirects_to_home_page(open_order_page):
    open_order_page.click_logo_scooter()  # Кликаем по логотипу "Самокат" на странице заказа
    open_order_page.wait_for_load_main_page()  # Ждём загрузки главной страницы
    actual_result = open_order_page.get_current_url() # Получаем текущий URL
    expected_result = TestData.SCOOTER_MAIN_PAGE  # Ожидаемый URL — главная страница
    assert actual_result == expected_result, (f"Ожидали URL: {expected_result}, но получили: {actual_result}") # Проверяем URL