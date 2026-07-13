import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

res = []


@pytest.fixture(scope="function")
def browser():
    print('\nStart browser for test: ')
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
    print("SECRET FRASE IS:")
    print("".join(res))


lessons = ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905']


@pytest.mark.parametrize('lesson', lessons)
def test_1(browser, lesson):
    browser.get("https://stepik.org/lesson/{}/step/1".format(lesson))
    browser.implicitly_wait(5)
    try:
        # Ищем аватарку, чтобы понять, авторизованы ли мы
        img = browser.find_element(By.CSS_SELECTOR, ".navbar__profile-img")
    except:
        # Авторизация
        b = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button')))
        b.click()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".light-tabs.ember-view")))
        l = browser.find_element(By.ID, "id_login_email")
        l.send_keys("Stikhinsky@mail.ru")  # Ввести почту
        p = browser.find_element(By.ID, "id_login_password")
        p.send_keys("Offspring1")  # Ввести пароль
        submit_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader[type='submit']")))
        submit_button.click()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".navbar__profile-img"))
        )
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")))
        # Нажать на кнопку "Начать сначала" для очистки формы
        r = browser.find_element(By.CSS_SELECTOR, ".has-icon.attempt-wrapper-buttons__button.white")
        r.click()
    except:
        pass
    answer = math.log(int(time.time()))
    text_area = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, ".ember-text-area.ember-view.textarea.string-quiz__textarea")))
    text_area.send_keys(str(answer))
    b2 = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".attempt-wrapper-buttons__button")))
    b2.click()
    # Нажать на кнопку "Начать сначала" для очистки формы
    r = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".has-icon.attempt-wrapper-buttons__button.white")))
    r.click()
    ask = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    if ask.text != "Correct!":
        res.append(ask.text)
    assert ask.text == "Correct!", "is not correct"
