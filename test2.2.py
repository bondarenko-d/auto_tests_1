from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

    img = browser.find_element_by_css_selector("#treasure")
    img.click()

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('[valuex]')
    x = x_element.get_attribute('valuex')
    y = calc(x)

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()

    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(10)
    browser.quit()