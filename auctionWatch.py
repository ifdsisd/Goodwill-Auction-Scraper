
import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


chrome_options = Options()
chrome_options.add_argument('--headless')

class auctionMonitor:
    def __init__(self,url,maxBid):
        self.url=url
        self.maxBid=maxBid
    def currentBid(self):
        pass
    def timeLeft(self):
        
        driver = self.driverSess()
        time.sleep(4)
        matches  = driver.find_elements(By.TAG_NAME,'span')
        for i in matches:
            if i.text.split(":")[0]=='Time left':
                print(i.text.split(":")[1] )
                return i.text.split(":")[1] 
        driver.close()
        
        
    def driverSess(self):
         driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
   
         driver.get(self.url)
         return driver
    def currentBid(self):
        driver = self.driverSess()
        time.sleep(4)
        matches  = driver.find_elements(By.TAG_NAME,'h3')
        for i in matches:
            print(i.text)
        return matches[1]
        driver.close()
    def getReq(self):
        return self.req
    
        
def loadItems(filePath:str):
    try:
        items=[]
        with open(filePath,"r") as file:
            for item in file.readlines():
                print("Entry added")
                items.append(item)
        return items
    except IOError as e:
        print("Unknown file error occured exiting...")
        return None
 
 


