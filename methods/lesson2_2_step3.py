from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.ID, "num1")
    input2 = browser.find_element(By.ID, "num2")
    res = int(input1.text) + int(input2.text)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(res))  # ищем элемент со значением "res"

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
