import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from getfood import getFood

from OL import *

 

food = getFood()

order = getOrder()

friend = getFriendOrder()

options = Options()

options.page_load_strategy = 'normal'

options.add_experimental_option('detach',True)

options.add_argument(r"--user-data-dir=C:\\Users\\adsouza\\AppData\\Local\\Google\\Chrome\\User Data")

options.add_argument('--headless=new')

options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome(options=options)

 

driver.get(https://web.yammer.com/main/users/eyJfdHlwZSI6IlVzZXIiLCJpZCI6IjExNzgxOTQyODg2NDAifQ/storyline)

 

time.sleep(10)

 

discussion_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/ul/div/div/li/div/div/div[1]/div/div/div/div/div[2]/div[1]/button")

discussion_button.click()

time.sleep(10)

text_area = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/ul/div/div/li/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div/div")

if order =='':

    text_area.send_keys("Today I'm going to have "+food+" for lunch!"+friend)

else:

    text_area.send_keys("Today I'm going to have "+order+" for lunch!"+friend)

time.sleep(10)

post_button = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[1]/ul/div/div/li/div/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div/div[1]/button")

post_button.click()

time.sleep(1)

post_button.click()

time.sleep(10)

driver.close()

 

print("COMPLETE")

 

#discussion.send_keys("Text to input into Yammer")

#discussion.send_keys(Keys.RETURN)

## automated used task scheduler