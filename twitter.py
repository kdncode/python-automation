from selenium import webdriver
from getpass import getpass
import time

usr = input('Enter username: ')
pwd = getpass('Enter pass: ')
tweet = input('Enter a tweet: ')

driver = webdriver.Chrome()
driver.get('http://twitter.com/login')

driver.find_element_by_class_name('js-username-field').send_keys(usr)
driver.find_element_by_class_name('js-password-field').send_keys(pwd)

driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium').submit()

driver.find_element_by_name('tweet').send_keys(tweet)
driver.find_element_by_css_selector('button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn').click()

time.sleep(3)
driver.close()

print('Done')



## Twitter automatically Login + Tweet text and image

# from selenium import webdriver
# from getpass import getpass
# from time import sleep

# usr = input('Enter username: ')
# pwd = getpass('Enter pass: ')
# twt = input('Enter your tweet: ')
# # img_path = input('Enter image path: ')

# driver = webdriver.Chrome()
# driver.get('https://twitter.com/login')

# usr_box = driver.find_element_by_class_name('js-username-field')
# usr_box.send_keys(usr)
# # sleep(1)

# pwd_box = driver.find_element_by_class_name('js-password-field')
# pwd_box.send_keys(pwd)
# # sleep(3)

# login_btn = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
# login_btn.submit()
# # sleep(3)

# twt_box = driver.find_element_by_id('tweet-box-home-timeline')
# twt_box.send_keys(twt)
# sleep(1)

# # img_box = driver.find_element_by_css_selector('input.file-input.js-tooltip')
# # img_box.send_keys(img_path)

# tweet_button = driver.find_element_by_css_selector('button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn')
# tweet_button.click()