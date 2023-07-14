import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exception
import pandas as pd

def initialize_webdriver(linke = 'https://www.emag.ro/#opensearch'):
    # try:
    # Creating the Safari driver instance
    driver = webdriver.Safari()
    # Setting the size of the Safari window
    driver.set_window_size(1400, 1440)
    # Entering the URL to the Safari driver instance
    driver.get(linke)
    return driver
    # except Exception as e:
    #     print(f'Error getting driver: {e}')

# Initialize the webdriver
driver = initialize_webdriver()

#

get_element = driver.find_element(by= By.ID, value='searchboxTrigger')
get_element.send_keys('telefon')
get_element.submit()

# Wait 10 seconds
time.sleep(10)

elements = driver.find_elements(by=By.CLASS_NAME, value='card-item')
list_of_elements = []
product_list = []
price_list = []
for i in elements:
    try:
        product = i.find_element(by=By.CLASS_NAME, value='card-v2-title-wrapper')
        product_list.append(product.text)
        print(product.text)
        price = i.find_element(by=By.CLASS_NAME, value='product-new-price')
        product_list.append(price.text)
        print(price.text)
    except exception.NoSuchElementException:
        pass

list_of_elements.append(product_list)
list_of_elements.append(price_list)
print(list_of_elements)

df = pd.DataFrame(list_of_elements).transpose()
df.to_csv('emag_all_products.csv', sep='|')
