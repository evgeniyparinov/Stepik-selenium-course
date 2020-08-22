from selenium import webdriver
import math
import time
import pyperclip

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x_):
    return math.log(abs(12 * math.sin(int(x_))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_mgc_jrny = browser.find_element_by_css_selector("button.btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    element_x = browser.find_element_by_css_selector("#input_value")
    x = element_x.text
    ans = calc(x)
    input_x = browser.find_element_by_css_selector("#answer")
    input_x.send_keys(str(ans))
    submit_x = browser.find_element_by_css_selector("button.btn").click()
    # copy the answer to the ClipBoard
    browser.implicitly_wait(5)
    alert = browser.switch_to.alert
    copied_ans = alert.text.split(":")[-1]
    pyperclip.copy(copied_ans)
    alert.accept()
    # Log in stepik.org and input the answer
    log_in = browser.get("https://stepik.org/login?next=catalog")
    browser.implicitly_wait(5)
    browser.find_element_by_css_selector("a.btn.btn-block.btn-social.btn-google").click()
    input_email = browser.find_element_by_css_selector("#identifierId")
    # enter your email
    input_email.send_keys("your email")
    browser.implicitly_wait(5)
    browser.find_element_by_css_selector("#identifierNext").click()
    time.sleep(5)
    input_password = browser.find_element_by_css_selector("[type=password]")
    # enter your password
    input_password.send_keys("your password")
    browser.implicitly_wait(5)
    browser.find_element_by_css_selector("#passwordNext").click()
    time.sleep(10)
    # complete the task
    task = browser.get("https://stepik.org/lesson/184253/step/4?unit=158843")
    browser.implicitly_wait(5)
    input_ans = browser.find_element_by_css_selector("textarea.textarea.string-quiz__textarea")
    input_ans.send_keys(copied_ans)
    time.sleep(10)
    browser.find_element_by_css_selector("button.submit-submission").click()

finally:
    time.sleep(5)
    browser.quit()
