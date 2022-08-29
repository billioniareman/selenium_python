# here we are going to login into amazon webpage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
username = input("enter your username or email:")
phone_number=input("enter your phone number")

# installing chrome as a webdriver for environment
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.amazon.in/')

# finding sign in button
login = driver.find_element(By.XPATH, '//*[@id="nav-link-accountList"]')
login.click()
time.sleep(2)

# finding textarea and give username
ele1 = driver.find_element(By.XPATH, "//input[@id='ap_email']")
time.sleep(2)
ele1.send_keys(username)
time.sleep(2)

# finding continue button and clicking it
ele2 = driver.find_element(By.XPATH, '//*[@id="continue"]')
ele2.click()
# finding and clicing on forget password link
ele3=driver.find_element(By.XPATH,"//a[@id='auth-fpp-link-bottom']")
ele3.click()
#finding textarea and giving phone number to get otp
ele4=driver.find_element(By.XPATH,"//input[@id='ap_email']")
ele4.clear()
ele4.send_keys(phone_number)
# clicking continue button after finding it
ele5=driver.find_element(By.XPATH,"//input[@id='continue']")
ele5.click()
time.sleep(3)
driver.close()

