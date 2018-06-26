# Facebook Login

from selenium import webdriver
from getpass import getpass

# Get the input
usr = input('Enter your email or phone: ')
pwd = getpass('Enter your password: ')

# Open browser Chrome
driver = webdriver.Chrome()
driver.get('https://facebook.com/')

# Find the username field
username_box = driver.find_element_by_id('email')
# Send username input to the webpage
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('loginbutton')
login_btn.submit()


## Python Search

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


