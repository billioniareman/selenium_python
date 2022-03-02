#this is the automation code to get earbuds details 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome("C:\webdriver\chromedriver.exe")
driver.get("https://www.amazon.com")
class get_product():
    def product(self):

        value=driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("earbuds")
        driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()

obj1=get_product()
obj1.product()
