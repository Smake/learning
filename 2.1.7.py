import math
import time
from selenium import webdriver

try:

    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    x = browser.find_element_by_css_selector('#treasure').get_attribute('valuex')

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    input_value = browser.find_element_by_css_selector('#answer')
    input_value.send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button').click()
    time.sleep(10)

finally:

    browser.quit()
