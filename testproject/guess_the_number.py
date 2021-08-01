import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def guessing(value):
    num_input = driver.find_element_by_xpath('//input[@type="number"]')
    num_input.clear()
    time.sleep(0.5)
    num_input.send_keys(value)
    time.sleep(0.5)
    button_guess.click()
    time.sleep(0.5)


def success():
    success_alert = driver.find_element_by_xpath('//p[@ng-show="deviation === 0"]')
    return success_alert.get_attribute('class') == 'alert alert-success'


# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html'
driver.get(URL)

# getting the input fields and buttons
guess_number = driver.find_element_by_xpath('//span[@class="badge ng-binding"]')
button_guess = driver.find_element_by_xpath('//button[@class="btn btn-primary"]')
button_restart = driver.find_element_by_xpath('//button[@class="btn btn-warning btn-sm pull-right pull-down"]')

# TC003: checking with false values -19 and 255
low_value = '-19'
high_value = '255'

guessing(low_value)
lower_alert = driver.find_element_by_xpath('//p[@ng-show="deviation > 0"]')
assert (lower_alert.get_attribute('class') == 'alert alert-warning')

guessing(high_value)
higher_alert = driver.find_element_by_xpath('//p[@ng-show="deviation < 0"]')
assert (higher_alert.get_attribute('class') == 'alert alert-warning')

# TC001: guessing and finding the correct number and checking the guess count
button_restart.click()
time.sleep(0.5)

guess_count = 0
for i in range(1, 101):
    guess_count += 1
    guessing(str(i))
    if success():
        break

assert (str(guess_count) == guess_number.text)
