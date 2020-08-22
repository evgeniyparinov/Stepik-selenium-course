from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("//div/input[1]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//div/input[2]")
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_xpath("//div/input[3]")
    input3.send_keys("Ivan.ivanov@gmail.com")

    attach = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(""))
    text_path = os.path.join(current_dir, "text.txt")
    attach.send_keys(text_path)

    submit = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(5)
    browser.quit()
