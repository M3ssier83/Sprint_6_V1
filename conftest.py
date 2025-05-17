import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import TestData

@allure.step("Открытие браузера Firefox")
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 820)
    yield driver
    driver.quit()

@allure.step("Создание экземпляра главной страницы")
@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@allure.step("Создание экземпляра страницы оформления заказа")
@pytest.fixture
def order_page(driver):
    return OrderPage(driver)

@allure.step("Открытие главной страницы")
@pytest.fixture
def open_main_page(main_page):
    main_page.open(TestData.SCOOTER_MAIN_PAGE)
    main_page.wait_for_load_main_page()
    return main_page

@allure.step("Открытие страницы оформления заказа")
@pytest.fixture
def open_order_page(order_page):
    order_page.open_order_page()
    order_page.wait_for_load_order_page()
    return order_page
