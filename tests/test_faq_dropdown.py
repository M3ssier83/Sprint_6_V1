# Проверка выпадающего списка в разделе «Вопросы о важном»: при нажатии на стрелочку должен открыться соответствующий текст.

import pytest
import allure
from data import TestData
from pages.main_page import MainPage

@allure.title("Проверка отображения текста ответа на вопрос в блоке FAQ")
@pytest.mark.parametrize("key, expected_text", TestData.get_faq_answers())
def test_faq(driver, key, expected_text):
    page = MainPage(driver)
    page.open()  # если этот метод есть, иначе просто открой через driver.get()
    actual_answer = page.open_question_and_get_answer(key)
    assert actual_answer == expected_text, (
        f"Для вопроса '{key}' ожидался ответ:\n'{expected_text}',\n"
        f"но получен:\n'{actual_answer}'"
    )