# Проверка оформления заказа с двумя наборами данных, проверка всплывающего окна с сообщением об успешном создании заказа.

import pytest
import allure
from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import TestData

@allure.title("Проверки оформления заказа с валидными данными через обе кнопки заказа и всплывающего окна с сообщением об успешном создании заказа")
# Параметризируем тест: передаём пары (данные заказа, позиция кнопки "Заказать")
@pytest.mark.parametrize("order_data, button_position", TestData.get_order_button_data())
def test_order_form_submission(driver, order_data, button_position):
    main_page = MainPage(driver) # Создаём экземпляр главной страницы
    order_page = OrderPage(driver) # Создаём экземпляр страницы оформления заказа
    main_page.open() # Открываем главную страницу
    main_page.close_cookie_popup() # Закрываем попап cookies

    click_method = main_page.get_click_method_map().get(button_position)  # Получаем метод клика по кнопке в зависимости от её положения (верхняя или нижняя)
    assert click_method, f"Нет метода для позиции кнопки: {button_position}" # Проверяем, что метод найден. Если нет — выводим сообщение об ошибке с указанием позиции
    click_method()  # Кликаем по соответствующей кнопке "Заказать"

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
