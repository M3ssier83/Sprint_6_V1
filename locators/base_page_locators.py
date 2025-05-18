from selenium.webdriver.common.by import By

class BasePageLocators:

    LOGO_SCOOTER = (By.XPATH, './/a[@class="Header_LogoScooter__3lsAR"]')  # Логотип Самоката в шапке
    COOKIE_CLOSE_BUTTON = (By.XPATH, "//button[text()='да все привыкли']") # Кнопка закрытия попапа cookies
    LOGO_YANDEX = (By.XPATH, './/a[@class="Header_LogoYandex__3TSOI"]')  # Логотип Яндекса в шапке страницы
