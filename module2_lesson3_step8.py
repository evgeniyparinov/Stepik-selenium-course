from selenium import webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pyperclip
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x_):
    return math.log(abs(12 * math.sin(int(x_))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    # waiting until the price falls to $100
    price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    browser.find_element_by_css_selector("#book").click()
    # calculate the equation and submit the answer
    element_x = browser.find_element_by_css_selector("#input_value")
    x = element_x.text
    ans = calc(x)
    input_x = browser.find_element_by_css_selector("#answer")
    input_x.send_keys(str(ans))
    submit_x = browser.find_element_by_css_selector("#solve").click()
    # copy answer to clipboard
    alert = browser.switch_to.alert
    ans = alert.text.split(":")[1]
    pyperclip.copy(ans)

finally:
    time.sleep(5)
    browser.quit()
