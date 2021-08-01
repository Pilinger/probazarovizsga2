import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# initialising chrome driver
driver = webdriver.Chrome(ChromeDriverManager().install())
URL = 'https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html'
driver.get(URL)


def getting_links():
    return driver.find_elements_by_xpath('//div[@class="container-total"]/a')


# getting the Register button
button_register = driver.find_element_by_class_name('mostra-container-cadastro')

# TC001: checking if the 24 elements appeared on startup
time.sleep(3)
links = getting_links()
assert (len(links) == 24)

# TC002: checking if its possible to Register and save a new film
# test data implementation
title = 'Black widow'
release = '2021'
chrono = '2020'
trailer = 'https://www.youtube.com/watch?v=Fp9pNPdNwjI'
image = 'https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg'
summary = 'https://www.imdb.com/title/tt3480822/'

# clicking on the Register button
button_register.click()
time.sleep(2)

# gaining the input fields and Save button
title_input = driver.find_element_by_id('nomeFilme')
release_input = driver.find_element_by_id('anoLancamentoFilme')
chrono_input = driver.find_element_by_id('anoCronologiaFilme')
trailer_input = driver.find_element_by_id('linkTrailerFilme')
image_input = driver.find_element_by_id('linkImagemFilme')
summary_input = driver.find_element_by_id('linkImdbFilme')
button_save = driver.find_element_by_xpath('//button[@onclick="salvarFilme()"]')

title_input.send_keys(title)
time.sleep(0.5)
release_input.send_keys(release)
time.sleep(0.5)
chrono_input.send_keys(chrono)
time.sleep(0.5)
trailer_input.send_keys(trailer)
time.sleep(0.5)
image_input.send_keys(image)
time.sleep(0.5)
summary_input.send_keys(summary)
time.sleep(0.5)

button_save.click()
time.sleep(2)

# checking if the Black Widow appeared in 25th place
assert (len(getting_links()) == 25)
