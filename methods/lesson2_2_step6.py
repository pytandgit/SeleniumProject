from selenium import webdriver
from selenium.webdriver.common.by import By
from  math import log, sin
import time

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    # считываем значение x
    x = int(browser.find_element(By.ID, "input_value").text)
    res = log(abs(12*sin(x))).__str__()

    # заполнение поля результатом вычисления
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(res)

    # отметить чекбокс "I'm the robot"
    chbx = browser.find_element(By.ID, "robotCheckbox")
    chbx.click()

    browser.execute_script("window.scrollBy(0, 40);")
    # выбрать радиобаттон "People rule"
    rdbtn = browser.find_element(By.ID, "robotsRule")
    rdbtn.click()

    # скролл к нужной кнопке
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # ждем загрузки страницы
    time.sleep(1)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()