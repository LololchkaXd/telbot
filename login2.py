#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import selenium
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")



driver = webdriver.Chrome(options=options)
driver.get("http://nzrbhome.sytes.net:8080/index.htm")

time.sleep(5)
# fill in username and hit the next button
elem = driver.find_element_by_xpath('//div[25]/div[2]')
actions = ActionChains(driver)
actions.click(elem).perform()
time.sleep(2)
elm2 = driver.find_element_by_xpath('//div[26]/div[4]/div[2]')
time.sleep(2)
actions = ActionChains(driver)
actions.click(elm2).perform()
elm3 = driver.find_element_by_xpath('//div[2]/input')
actions = ActionChains(driver)
actions.click(elm3).perform()
time.sleep(5)

driver.close()







