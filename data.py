from datetime import datetime, timedelta

# Вспомогательные функции форматирования дат
def format_date_str(date_obj): # Форматирует дату в строку формата 'дд.мм.гггг', например '10.05.2025'
    return date_obj.strftime("%d.%m.%Y")

def format_date_human(date_obj): # Форматирует дату в читаемый формат с названием месяца на русском, например '10 мая 2025'.
    months = {
        1: "января", 2: "февраля", 3: "марта", 4: "апреля",
        5: "мая", 6: "июня", 7: "июля", 8: "августа",
        9: "сентября", 10: "октября", 11: "ноября", 12: "декабря"
    }
    return f"{date_obj.day} {months[date_obj.month]} {date_obj.year}"

# Текущая дата и дата завтрашнего дня
today = datetime.now().date()
tomorrow = today + timedelta(days=1)

class TestData:
    # Основные URL'ы проекта в двух форм-факторах (вместо корректировки методов реила пойти немного по другому пути, и добавила дублирующий словарь с юрлами)
    SCOOTER_MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    YANDEX_MAIN_PAGE = 'https://dzen.ru/?yredirect=true'
    SCOOTER_ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'

    URLS = {
        'SCOOTER_MAIN_PAGE': SCOOTER_MAIN_PAGE,
        'YANDEX_MAIN_PAGE': YANDEX_MAIN_PAGE,
        'SCOOTER_ORDER_PAGE': SCOOTER_ORDER_PAGE,
    }

    # Тестовые данные для оформления заказа
    order_data = [
        {
            'first_name': 'Марьям',  # Имя пользователя
            'second_name': 'Кондратьева',  # Фамилия пользователя
            'address': 'Москва',  # Адрес доставки
            'metro_station': 'Лубянка',  # Станция метро (отображаемое значение)
            'metro_selection': 'Лубянка',  # Текст кнопки выбора станции
            'phone_number': '+79811226622',  # Номер телефона
            'delivery_date': format_date_str(today),  # Дата доставки (строкой)
            'date_selection': format_date_human(today),  # Отображаемое значение даты
            'rental_period': 'двое суток',  # Срок аренды (текстовое значение)
            'scooter_color': 'black',  # Цвет самоката
            'courier_comment': 'Подъезд со стороны двора',  # Комментарий для курьера
            'location': 'top'
        },
        {
            'first_name': 'Александр',  # Имя пользователя
            'second_name': 'Кондратьев',  # Фамилия пользователя
            'address': 'Москва',  # Адрес доставки
            'metro_station': 'Фрунзенская',  # Станция метро (отображаемое значение)
            'metro_selection': 'Фрунзенская',  # Текст кнопки выбора станции
            'phone_number': '+79811227755',  # Номер телефона
            'delivery_date': format_date_str(today),  # Дата доставки (строкой)
            'date_selection': format_date_human(today),  # Отображаемое значение даты
            'rental_period': 'трое суток',  # Срок аренды (текстовое значение)
            'scooter_color': 'grey',  # Цвет самоката
            'courier_comment': 'Привезти вкусняшки',  # Комментарий для курьера
            'location': 'bottom'
        }
    ]

    @classmethod
    def get_order_data(cls):
        return cls.order_data