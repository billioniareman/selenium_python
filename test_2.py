'''
hello
here we are going to open amazon and search for product like earbuds
and then fetch the brand and price range of the product
'''

from selenium import webdriver

driver = webdriver.Chrome("C:\webdriver\chromedriver.exe")
driver.get("https://www.amazon.com")


def product():
    driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys("earbuds")
    driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()


def filter_brand():
    driver.find_element_by_xpath("//span[normalize-space()='See more']").click()
    brands = driver.find_element_by_xpath('//*[@id="brandsRefinements"]/ul').text
    all_brands = []
    for i in (brands.split(sep="\n")):
        all_brands.append(i)
    print(all_brands)


def filter_price():
    price = driver.find_element_by_xpath('//*[@id="priceRefinements"]/ul[1]').text
    price_range = []
    for i in (price.split(sep="\n")):
        price_range.append(i)
    print(price_range)


product()
filter_brand()
filter_price()
