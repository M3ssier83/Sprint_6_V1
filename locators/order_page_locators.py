from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Локаторы блока "Для кого самокат"
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']") # Поле ввода имени пользователя
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']") # Поле ввода фамилии пользователя
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # Поле ввода адреса доставки
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']") # Поле ввода станции метро
    METRO_OPTION_TEMPLATE = "//div[text()='{}']" # Шаблон выбора станции метро из выпадающего списка
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # Поле ввода номера телефона
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']") # Кнопка перехода к следующему шагу оформления заказа

    # Локаторы блока "Про аренду"
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # Поле для выбора даты аренды
    NEXT_MONTH_BUTTON = (By.CLASS_NAME, "react-datepicker__navigation--next")
    DATE_OPTION_TEMPLATE = "//div[contains(@class,'react-datepicker__day--') and text()='{}']" # Шаблон локатора дня в календаре (тут очень сильно помог ChatGPT)
    DATE_PICKER_DAY_XPATH = "//div[contains(@class, 'react-datepicker__day') and not(contains(@class, 'outside-month')) and text()='{}']"
    RENT_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder") # Выпадающий список срока аренды
    RENT_PERIOD_OPTION_TEMPLATE = "//div[@class='Dropdown-menu']//div[text()='{}']" # Шаблон локатора пункта в выпадающем списке срока аренды
    COLOR_BLACK = (By.ID, "black") # Чекбокс выбора чёрного цвета самоката
    COLOR_GREY = (By.ID, "grey") # Чекбокс выбора серого цвета самоката
    COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']") # Поле ввода комментария курьеру
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']") # Кнопка подтверждения оформления заказа
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']") # Кнопка подтверждения в модальном окне (Да)
    SUCCESS_MESSAGE = (By.XPATH, './/div[@class="Order_ModalHeader__3FDaJ"]') # Заголовок окна об успешном оформлении заказа