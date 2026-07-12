import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestUniq(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.reg(link)

        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта, тест пройдет
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Registration failed")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.reg(link)

        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта, тест не пройдет
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Registration failed")

    def reg(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
        input1.send_keys("Alex")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
        input1.send_keys("St")
        input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
        input1.send_keys("s@s.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text


if __name__ == "__main__":
    unittest.main()
