import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://t-mobile.com')

driver.find_element_by_css_selector('div.icon.slide').click()
driver.find_element_by_name('q').send_keys('iPhone X')
driver.find_element_by_class_name('search-submit').send_keys(Keys.ENTER)

time.sleep(5)

print('CLOSE')
