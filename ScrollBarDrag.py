#coding=utf-8
from selenium import webdriver
import time
#访问百度

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#搜索
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
#将页面滚动条拖到底部

driver.execute_script("window.scrollBy(0,750)", "")