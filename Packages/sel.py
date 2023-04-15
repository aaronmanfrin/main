import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.page_load_strategy = 'normal'
options.add_experimental_option('detach',True)
options.add_argument(r"--user-data-dir=/Users/aarondsouza/Library/Application Support/Google/Chrome/")
options.add_argument("--headless")
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options) ##creating a driver instance

driver.get("https://www.neuralnine.com/") ## opens the specified webpage
driver.maximize_window()## this will force fullscreen the window

## finding all the links /a tags on page

links = driver.find_elements("xpath","//a[@href]") ## getting all lines that have an href tag
for link in links:
    pass
    #print(link.get_attribute('innerHTML'))## printing each of the inner html tags we gathered

for link in links:
    if "Books" in link.get_attribute('innerHTML'):  ##checking if link includes Books
        link.click() ## click on the book link
        break

book_links = driver.find_elements('xpath',"//div[contains(@class, 'elementor-column-wrap')][.//h2[text()[contains(., '7 IN 1')]]][count(.//a)=2]//a") ## this is looking for a div container thats meets this condition: it contains a class called elementor-column-wrap, and if that is met then it also has an h2 heading, with text containing the words 7IN 1, then checking if it has 2 anchor tags and if so then get them
#for book_link in book_links:
#    print(book_link.get_attribute("href"))

book_links[1].click()  ## clicking on the first link we got

## in selenium we are still on the first tab, we must move to the new amazon tab
driver.switch_to.window(driver.window_handles[1])
time.sleep(3) ## allowing the page to load

buttons = driver.find_elements("xpath","//a[.//span[text()[contains(.,'Paperback')]]]//span[text()[contains(., '$')]]")##finding anchor tags that contains span which contains "paperback", then within that we find text that contains $ sign

for button in buttons:
    print(button.get_attribute('innerHTML')) ## printing the button which contains our monetary value