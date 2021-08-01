import datetime
import time
from selenium.webdriver.support.ui import Select
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html'
driver.get(URL)

# gathering the items from the first page
select_first = Select(driver.find_element_by_name('bf_totalGuests'))
buttons = driver.find_elements_by_xpath('//button')

# filling in the needed fields in the first page
select_first.select_by_value('4')
time.sleep(0.5)
buttons[0].click()
time.sleep(0.5)

# gathering the items from the second page
date_time_input = driver.find_element_by_name('bf_date')
select_time = Select(driver.find_element_by_name('bf_time'))
select_hours = Select(driver.find_element_by_name('bf_hours'))
# test data
date_time = datetime.datetime(2021, 8, 2, 12, 25)

# filling in the needed fields in the second page
date_time_input.send_keys(date_time.strftime('%Y-%m-%d %H:%M'))
time.sleep(0.5)
select_time.select_by_value('Midday')
time.sleep(0.5)
select_hours.select_by_value('4')
time.sleep(0.5)
buttons[1].click()
time.sleep(0.5)

# gathering the items from the third page
name_input = driver.find_element_by_name('bf_fullname')
email_input = driver.find_element_by_name('bf_email')
#test data
fullname = 'György Ivó Pilinger'
email = 'dummy@freemail.hu'
invalid_email = 'pittyputty@valami@megvalami@ize.hu'

# filling in with correct name
name_input.send_keys(fullname)
time.sleep(0.5)
# TC002: checking first with invalid email address
email_input.send_keys(invalid_email)
time.sleep(0.5)
buttons[2].click()
time.sleep(0.5)
warning_span = driver.find_elements_by_id('bf_email-error')
assert (len(warning_span) == 1)

# TC001: continuing with correct email, and checking the response message
email_input.clear()
time.sleep(0.5)
email_input.send_keys(email)
buttons[2].click()
time.sleep(2)

assert (driver.find_element_by_tag_name('h2').text == "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!).")
