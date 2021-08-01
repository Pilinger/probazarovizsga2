import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html'
driver.get(URL)

# gathering the lis
lis = driver.find_elements_by_xpath('//li')

# reading in the data.txt and assigning to chemical_elements
chemical_elements = {}
with open('data.txt', 'r', ) as data_file:
    for line in data_file:
        short = line.strip('\n')
        (key, val) = short.split(', ')
        chemical_elements[key] = val

print('in data.txt')
print(chemical_elements)
print()

# reading the site and assigning to elements_on_site
elements_on_site = {}
for li in lis:
    if li.get_attribute('class') == 'empty':
        continue
    elements_on_site[li.get_attribute('data-pos')] = li.find_element_by_tag_name('span').text

print('On the site')
print(elements_on_site)

# comparing the two dictionaries
assert (chemical_elements == elements_on_site)
