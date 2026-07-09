from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from math import log, sin

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока цена не станет равна $100
    title = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    buttonBook = browser.find_element(By.ID, "book")
    buttonBook.click()

    # считываем значение x
    x = int(browser.find_element(By.ID, "input_value").text)
    res = log(abs(12 * sin(x))).__str__()

    # заполняем поле вычисленным значением
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(res)

    # скролл к кнопке Submit и ее нажатие
    buttonSubmit = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", buttonSubmit)
    buttonSubmit.click()

    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
