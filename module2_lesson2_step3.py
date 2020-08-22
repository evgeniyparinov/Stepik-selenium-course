from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = " http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_css_selector("#num1")
    first_number = int(num1.text)
    num2 = browser.find_element_by_css_selector("#num2")
    second_number = int(num2.text)
    sum_ = first_number + second_number
    # ищем в выпадающем спике сумму (sum_) чисел с id num1 и num2
    dropdown = Select(browser.find_element_by_tag_name("select"))
    dropdown.select_by_value(str(sum_))
    submit = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
