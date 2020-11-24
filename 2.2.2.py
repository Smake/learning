from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:

    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/selects1.html'
    browser.get(link)

    sum = int(browser.find_element_by_css_selector('#num1').text) + int(browser.find_element_by_css_selector('#num2').text)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(sum))

    browser.find_element_by_css_selector('button').click()
    time.sleep(10)

finally:

    browser.quit()
