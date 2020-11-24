import math
import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/math.html')

x_element = browser.find_element_by_css_selector('#input_value')

x = x_element.text

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

y = calc(x)

input_value = browser.find_element_by_css_selector('#answer')
input_value.send_keys(y)

browser.find_element_by_id('robotCheckbox').click()
browser.find_element_by_id('robotsRule').click()
browser.find_element_by_css_selector('button').click()

time.sleep(10)
