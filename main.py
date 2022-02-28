from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class login():
    def login_acc(self):
        url="https://www.amazon.com"
        driver=webdriver.Chrome("C:\webdriver\chromedriver.exe")
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="nav-link-accountList"]').click()
        driver.find_element_by_xpath('//*[@id="ap_email"]').send_keys("9893023657")
        driver.find_element_by_xpath("//input[@id='continue']").click()
        driver.find_element_by_xpath('//*[@id="ap_password"]').send_keys("qwery123")
        driver.find_element_by_xpath('//*[@id="signInSubmit"]'). click()
        time.sleep(20)
        driver.close()

login_into=login()
login_into.login_acc()