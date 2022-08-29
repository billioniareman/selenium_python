# here we are going to login into amazon webpage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.in/')
ele1=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
ele1.send_keys("shoes")
ele1.submit()
time.sleep(3)
ele2=driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-star-medium a-star-medium-4']")
ele2.click()
time.sleep(3)
ele3=driver.find_element(By.XPATH,"//li[@id='p_89/Puma']//i[@class='a-icon a-icon-checkbox']")
ele3.click()
#//span[@class='a-size-base a-color-base'][normalize-space()='Puma']
#//li[@id='p_89/Puma']//i[@class='a-icon a-icon-checkbox']
time.sleep(3)
driver.close()

