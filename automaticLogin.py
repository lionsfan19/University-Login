'''
Created on Aug 6, 2020

@author: aaryangaikwad
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/AG/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)


driver.get("https://outlook.office.com")

search = driver.find_element_by_id('i0116')
search.send_keys('')
search.send_keys(Keys.ENTER)


username = driver.find_element_by_id('username')
username.send_keys('')
password = driver.find_element_by_id('password')
password.send_keys('')


time.sleep(5)
driver.quit()






