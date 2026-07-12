"""
поиск сокровища с помощью get_attribute
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск на странице числа для расчета
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # заполнение формы вычисленным значением
    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(str(y))

    # отметить чекбокс "I'm the robot"
    chbx = browser.find_element(By.ID, "robotCheckbox")
    chbx.click()

    # выбрать радиобаттон "People rule"
    rdbtn = browser.find_element(By.ID, "robotsRule")
    rdbtn.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
