import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import numpy as np
import pandas as pd

options = Options()
options.page_load_strategy = 'normal'
options.add_experimental_option('detach',True)
options.add_argument('window-size=1920x1080') ## so the virtual browser can click on elements
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

driver.get("https://stake.us/casino/games/crash") 


vals = []

time.sleep(5)

b = driver.find_elements(By.CLASS_NAME,"variant-game.line-height-150pct.text-size-sm.spacing-normal.weight-semibold.align-center.svelte-1aq1zn0")
b[0].click()

time.sleep(1.5)

nextbutton = driver.find_elements(By.XPATH,"//*[@id='main-content']/div/div[1]/div[3]/div[2]/div[2]/div[2]/button[2]")

for i in range(99):
    time.sleep(2)
    words = driver.find_elements(By.CLASS_NAME,"chromatic-ignore")
    for word in words:
        span = word.find_elements(By.TAG_NAME,'span')
        for el in span:
            if el.get_attribute('innerHTML')[-1]=='×':
                num = float(el.get_attribute('innerHTML')[0:-1])
            else:
                num = el.get_attribute('innerHTML')
            vals.append(num)
    nextbutton[0].click()
    time.sleep(3)

vals=np.reshape(vals,(-1,2))
df= pd.DataFrame(vals)

df.rename(columns={0:'Time',1:'Factor'},inplace=True)
print(df)

df.to_csv("stake_factors.csv",mode='a', header=False)
time.sleep(5)
driver.quit()