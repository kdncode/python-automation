from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://google.com')

driver.find_element_by_name('q').send_keys('imkhoa')

driver.find_element_by_name('btnK').click()

time.sleep(10)

driver.quit()

print('Test complete')


## Google Test

# import time
# from selenium import webdriver

# driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()