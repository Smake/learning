from selenium import webdriver
import time, os

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")

    firstname = browser.find_element_by_css_selector('input[name="firstname"]')
    firstname.send_keys('Benis')

    lastname = browser.find_element_by_css_selector('input[name="lastname"]')
    lastname.send_keys('Petrov')

    email = browser.find_element_by_css_selector('input[name="email"]')
    email.send_keys('Benis')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'benis.txt')  # добавляем к этому пути имя файла
    file = browser.find_element_by_css_selector('input[name="file"]')
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector('button')
    button.click()

finally:

    time.sleep(10)
    browser.quit()
