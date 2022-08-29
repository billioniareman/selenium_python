from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
text="hey buddy"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://demoqa.com/alerts')
sleep(3)
ele1 = driver.find_element(By.XPATH, "//button[@id='promtButton']").click()
sleep(3)
alt = driver.switch_to.alert.send_keys(text)
sleep(3)

