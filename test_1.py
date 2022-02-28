# this is an automation test on the amazon 
# we are going to explore the selenium framework with python 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
product_name=input("enter the product name ")
brand_name=input("enter the name of brand ")
min,max=input("enter range of price(in dollars)").split('-')
url="https://www.amazon.com"
driver=webdriver.Chrome("C:\webdriver\chromedriver.exe")
driver.get(url)
driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]').send_keys(product_name," ",brand_name)
driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]').click()
driver.find_element_by_xpath('//*[@id="low-price"]').send_keys(min)
driver.find_element_by_xpath('//*[@id="high-price"]').send_keys(max)
driver.find_element_by_xpath('//*[@id="a-autoid-1"]/span/input').click()

lst=driver.find_elements_by_xpath('//*[@id="brandsRefinements"]/ul')
print(lst)
