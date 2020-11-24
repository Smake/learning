from selenium import webdriver
import time, math

try:

    browser = webdriver.Chrome()
    browser.get('https://SunInJuly.github.io/execute_script.html')
    x_element = browser.find_element_by_css_selector('#input_value')

    x = x_element.text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)
    input_value = browser.find_element_by_css_selector('#answer')
    input_value.send_keys(y)
    robotCheckbox = browser.find_element_by_id('robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotCheckbox)
    robotCheckbox.click()

    robotsRule = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
    robotsRule.click()

    button = browser.find_element_by_css_selector('button').click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    time.sleep(10)

finally:
    browser.quit()
