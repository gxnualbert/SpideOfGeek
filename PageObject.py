from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time, sys
import HTMLTestRunner
reload(sys)
import os
from bs4 import BeautifulSoup



def isElementExistByCSS(self,element):
        flag=True
        browser=self.driver
        try:
            browser.find_element_by_css_selector(element)
            return flag
        
        except:
            flag=False
            return flag