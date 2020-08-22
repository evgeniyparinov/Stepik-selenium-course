from selenium import webdriver
import time
import math
import pyperclip


def calc(x_):
    return math.log(abs(12 * math.sin(int(x_))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    push = browser.find_element_by_css_selector(".trollface.btn").click()
    # switch to a new tab
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    # calculate x and insert it into input field
    element_x = browser.find_element_by_css_selector("#input_value")
    x = element_x.text
    input_x = browser.find_element_by_css_selector("#answer")
    input_x.send_keys(str(calc(x)))
    submit = browser.find_element_by_css_selector("button.btn").click()
    # copy answer to clipboard
    alert = browser.switch_to.alert
    answer = alert.text.split(":")[1]
    pyperclip.copy(answer)

finally:
    time.sleep(5)
    browser.quit()
