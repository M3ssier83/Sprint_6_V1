# Проверка оформления заказа с двумя наборами данных, проверка всплывающего окна с сообщением об успешном создании заказа.

import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import TestData
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC


@allure.title("Проверки оформления заказа с валидными данными через обе кнопки заказа и всплывающего окна с сообщением об успешном создании заказа")
# Параметризируем тест: top и bottom кнопки + данные заказа
@pytest.mark.parametrize('order_data', TestData.get_order_data())
def test_order_form_submission(driver, order_data):
    main_page = MainPage(driver) # Создаём экземпляр главной страницы
    order_page = OrderPage(driver) # Создаём экземпляр страницы оформления заказа
    main_page.open() # Открываем главную страницу
    main_page.close_cookie_popup() # Закрываем попап cookies

    if order_data['location'] == 'top':
        main_page.click_top_order_button() # Кликаем по верхней кнопке «Заказать»
    elif order_data['location'] == 'bottom':
        main_page.click_bottom_order_button() # Кликаем по нижней кнопке «Заказать»
    else:
        raise ValueError(f"Неизвестное значение location: {order_data['location']}")

    order_page.fill_user_info( # Заполняем поля формы: имя, фамилия, адрес, метро, телефон
        order_data['first_name'],
        order_data['second_name'],
        order_data['address'],
        order_data['metro_station'],
        order_data['phone_number']
    )
    order_page.go_to_next_step() # Переходим на следующий шаг

    order_page.select_tomorrow_date() # Выбираем дату "завтра"
    order_page.select_rent_period(order_data['rental_period']) # Выбираем срок аренды
    order_page.select_scooter_color(order_data['scooter_color']) # Выбираем цвет самоката
    order_page.input_comment(order_data['courier_comment']) # Пишем комментарий курьеру
    order_page.confirm_order() # Подтверждаем заказ

    order_page.wait_for_load_successful_order() # Ждём появления сообщения об успешном заказе
    assert order_page.successful_order_is_displayed() is True, \
        'Окно с сообщением об успешном создании заказа не отобразилось.'  # Проверяем наличие сообщения
