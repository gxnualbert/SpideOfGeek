#coding=utf-8
from selenium import webdriver
import time
#access baidu.com

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#search selenium
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)

#Please note that, when you execute the drag scroll bar sript, please make sure the browser is not 
#loading anything,(you can sleep few minutes), or this script can not drag the browser

driver.execute_script("window.scrollBy(0,750)", "")