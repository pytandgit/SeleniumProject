from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Закрываем модальное окно
    confirm = browser.switch_to.alert
    confirm.accept()

    # считываем значение x
    x = int(browser.find_element(By.ID, "input_value").text)
    res = log(abs(12 * sin(x))).__str__()

    # заполняем поле вычисленным значением
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(res)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
