from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"


def calc(x_):
    return math.log(abs(12 * math.sin(int(x_))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # ищем значение элемента х в htnl
    element_x = browser.find_element_by_css_selector("#input_value")
    # вытаскиваем х как текст
    x = element_x.text
    # ищем поле для ввода х
    input_ans = browser.find_element_by_css_selector("#answer")
    # считаем функцию от х и ввод в поле ответа
    input_ans.send_keys(str(calc(x)))
    # ищем кнопу submit
    submit_button = browser.find_element_by_css_selector("button.btn")
    # скроллим вниз пока submit не будет полностью виден
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    # ищем чекбокс и нажимаем на него
    checkbox = browser.find_element_by_css_selector("#robotCheckbox").click()
    # ищем radio button со значением robotRule и нажинамем на него
    radio_button = browser.find_element_by_css_selector("#robotsRule").click()
    # сабмитим все
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
