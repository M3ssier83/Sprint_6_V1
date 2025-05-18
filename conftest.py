import pytest
import allure
from selenium import webdriver
from pages.order_page import OrderPage
from data import TestData
from pages.main_page import MainPage

@allure.step("Открытие браузера Firefox")
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1280, 820)
    yield driver
    driver.quit()

@allure.step("Открытие главной страницы")
@pytest.fixture
def open_main_page(driver):
    driver.get(TestData.SCOOTER_MAIN_PAGE)
    return MainPage(driver)

@allure.step("Открытие страницы оформления заказа")
@pytest.fixture
def open_order_page(driver):
    driver.get(TestData.SCOOTER_ORDER_PAGE)
    return OrderPage(driver)
