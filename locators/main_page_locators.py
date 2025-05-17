from selenium.webdriver.common.by import By

class MainPageLocators:

    BUTTON_ORDER_TOP = (By.XPATH, './/button[@class="Button_Button__ra12g"]') # Кнопка "Заказать" в верхней части страницы
    BUTTON_ORDER_BOTTOM = (By.XPATH, './/button[contains(@class, "Button_Middle__1CSJM")]') # Кнопка "Заказать" внизу страницы

    # Локаторы для блока с вопросами и ответами (FAQ)
    QUESTIONS = {
        "price_payment": {
            "question": (By.ID, "accordion__heading-0"),  # Вопрос: Сколько это стоит? И как оплатить?
            "answer":   (By.ID, "accordion__panel-0")     # Ответ: Сутки — 400 рублей. Оплата курьеру — наличными или картой.
        },
        "multiple_scooters": {
            "question": (By.ID, "accordion__heading-1"),  # Вопрос: Хочу сразу несколько самокатов! Так можно?
            "answer":   (By.ID, "accordion__panel-1")     # Ответ: Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.
        },
        "rental_duration": {
            "question": (By.ID, "accordion__heading-2"),  # Вопрос: Как рассчитывается время аренды?
            "answer":   (By.ID, "accordion__panel-2")     # Ответ: Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.
        },
        "order_today": {
            "question": (By.ID, "accordion__heading-3"),  # Вопрос: Можно ли заказать самокат прямо на сегодня?
            "answer":   (By.ID, "accordion__panel-3")     # Ответ: Только начиная с завтрашнего дня. Но скоро станем расторопнее.
        },
        "extension": {
            "question": (By.ID, "accordion__heading-4"),  # Вопрос: Можно ли продлить заказ или вернуть самокат раньше?
            "answer":   (By.ID, "accordion__panel-4")     # Ответ: Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.
        },
        "charger_included": {
            "question": (By.ID, "accordion__heading-5"),  # Вопрос: Вы привозите зарядку вместе с самокатом?
            "answer":   (By.ID, "accordion__panel-5")     # Ответ: Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.
        },
        "order_cancellation": {
            "question": (By.ID, "accordion__heading-6"),  # Вопрос: Можно ли отменить заказ?
            "answer":   (By.ID, "accordion__panel-6")     # Ответ: Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.
        },
        "delivery_outside_mkad": {
            "question": (By.ID, "accordion__heading-7"),  # Вопрос: Я живу за МКАДом, привезёте?
            "answer":   (By.ID, "accordion__panel-7")     # Ответ: Да, обязательно. Всем самокатов! И Москве, и Московской области.
        }
    }