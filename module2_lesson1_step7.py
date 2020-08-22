from selenium import webdriver
import math
import time


def calc(x_):
    return str(math.log(abs(12*math.sin(int(x_)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#treasure")
    value_x = x_element.get_attribute("valuex")
    y = calc(value_x)
    input_ = browser.find_element_by_css_selector("#answer")
    input_.send_keys(y)
    robot_checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    robot_checkbox.click()
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    radiobutton.click()
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
