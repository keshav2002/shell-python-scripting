from selenium import webdriver
from getpass import getpass

usr = input('Enter username / email ID: ')
pwd = getpass('Enter password: ')

driver = webdriver.Chrome(r"‪C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://www.facebook.com/')

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)

login_btn = driver.find_element_by_id('u_0_2')
login_btn.submit()