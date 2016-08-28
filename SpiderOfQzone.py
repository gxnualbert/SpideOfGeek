from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time, sys
import HTMLTestRunner
reload(sys)
import os




profile_dir=r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
chrome_options=webdriver.ChromeOptions()  
chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))  
driver = webdriver.Chrome(chrome_options=chrome_options)  
driver.implicitly_wait(30)
url = "http://qzone.qq.com/"
driver.get(url)
time.sleep(3)
account="1204351"
password=""
driver.switch_to_frame("login_frame")
switchLoginLink=driver.find_element(By.XPATH, "//*[@id='switcher_plogin']")
switchLoginLink.click()
time.sleep(4)

username=driver.find_element(By.CSS_SELECTOR, "#u")
username.clear()
username.send_keys(account)
time.sleep(2)
pwd=driver.find_element(By.CSS_SELECTOR,"#p")
pwd.clear()
pwd.send_keys(password)
time.sleep(2)

loginbtn=driver.find_element_by_css_selector("input#login_button")
loginbtn.click()





