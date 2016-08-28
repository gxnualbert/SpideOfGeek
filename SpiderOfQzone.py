from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time, sys
import HTMLTestRunner
import lxml
reload(sys)
import os
from bs4 import BeautifulSoup
import PageObject


class SpiderOfQzone(object):
    
    def loginQzone(self,driver,account,password):
        
        po=PageObject.PageObejct()
#         profile_dir=r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
#         chrome_options=webdriver.ChromeOptions()  
#         chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))  
#         driver = webdriver.Chrome(chrome_options=chrome_options)  
#         driver=webdriver.Chrome()
#         driver.implicitly_wait(30)
        url = "http://qzone.qq.com/"
        time.sleep(1)
        driver.get(url)
        isExist=po.isElementExistByCSS(driver, "li.menu_item_N1 a")
        if(not isExist):
            driver.switch_to_frame("login_frame")
            switchLoginLink=po.findElementByXpath(driver, "//*[@id='switcher_plogin']")
            switchLoginLink.click()
            time.sleep(2)
            
            username=po.findElementByCSS(driver, "#u")
            username.clear()
            username.send_keys(account)
            time.sleep(2)
            pwd=po.findElementByCSS(driver, "#p")
            pwd.clear()
            pwd.send_keys(password)
            time.sleep(2)
            
            loginBtn=po.findElementByCSS(driver, "input#login_button")
            loginBtn.click()
    
#     time.sleep(6)   
#     driver.execute_script("window.scrollBy(0,1500)", "")
    
    def getPeopleInfo(self,people):
        singlePeopleSoup=BeautifulSoup(people,"lxml")
        
        info = {}
        info["NickName"]=singlePeopleSoup.find("a", "f-name").get_text().encode("utf-8")
        print info["NickName"]
#         info["PostTime"]=""
#         info["Device"]=""
#         info["Browse People"]=""
#         info["Content"]=""
        
        return info
        
        
        
    def getPageSource(self,driver):
     
        html_doc=driver.page_source
        soup = BeautifulSoup(html_doc,"lxml")
        return soup
         
     
    def getPeoples(self,soup):   #single people
        singlePagePeople=soup.find_all("li", "f-single")
         
#         for a in range(len(singlePagePeople)):
#             people=singlePagePeople[a]
#      
#         namelist=[]
#         for i in range(len(namelist)):
#             nickname=namelist[i].get_text("|", strip=True)
#             nickname=nickname.encode("utf-8")
#             print nickname
         
     
    def saveInfo(self,classinfo):
        f = open('QzoneUserInfo.txt','a')
        for i in range(len(classinfo)):
            each=classinfo[i]
            f.writelines("NickName: "+str(i)+ '\n')
            f.writelines('PostTime:' +each['title'].encode("utf-8").replace("\t","").replace("\n","")+ '\n')
            f.writelines('Device:' + each['content'].encode("utf-8").replace("\t","").replace("\n","") + '\n')
            f.writelines('Browse People:' + each['classtime'].encode("utf-8").replace("\t","").replace("\n","") + '\n')
            f.writelines('Content:' + each['classlevel'].encode("utf-8").replace("\t","").replace("\n","") + '\n')
#             f.writelines('learnnum:' + each['learnnum'].encode("utf-8").replace("\t","").replace("\n","")+'\n\n\n')
        f.close()
if __name__ == '__main__':
    account=""
    pwd="01"
    classinfo = []
    profile_dir=r"C:\Users\Administrator\AppData\Local\Google\Chrome\User Data"
    chrome_options=webdriver.ChromeOptions()  
    chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))  
    driver = webdriver.Chrome(chrome_options=chrome_options)  
    driver.implicitly_wait(30)
    mySpider=SpiderOfQzone()
    
    mySpider.loginQzone(driver, account, pwd)
    time.sleep(8)
    m=str(driver.page_source())
    soup = BeautifulSoup(m)
    b=soup.find_all("a")
    print b

















#     pageSourceSoup=mySpider.getPageSource(driver)
#     peoples=mySpider.getPeoples(pageSourceSoup)
#     for i in range(len(peoples)):
#         singlePeople=peoples[i]
#         mySpider.getPeopleInfo(singlePeople)








