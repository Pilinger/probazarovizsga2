import time
import datetime
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html'
driver.get(URL)

# getting the radio buttons
original_radio = driver.find_element_by_id('original')
force_radio = driver.find_element_by_id('force')
factor_radio = driver.find_element_by_id('factor')
hellfire_radio = driver.find_element_by_id('hellfire')

original_rb = driver.find_element_by_xpath('//label[@for="original"]')
force_rb = driver.find_element_by_xpath('//label[@for="force"]')
factor_rb = driver.find_element_by_xpath('//label[@for="factor"]')
hellfire_rb = driver.find_element_by_xpath('//label[@for="hellfire"]')
# checking the original radio button
force_rb.click()
time.sleep(0.5)
original_rb.click()
time.sleep(0.5)

# getting the characters and checking if its original and size 100
# or not and size 50
characters = driver.find_elements_by_xpath('//ul/li')
for character in characters:
    img_size = character.find_element_by_xpath('.//img').size
    if 'original' in character.get_attribute('data-teams'):
        assert (img_size.get('height') == 100)
        assert (img_size.get('width') == 100)
    else:
        assert (img_size.get('height') == 50)
        assert (img_size.get('width') == 50)
