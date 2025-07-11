import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium.common.exceptions

timeout = time.time() + 60*5
purchase_time = 0

def buy_upgrades():
    items = 20
    for num in range(items,0,-1):
        purchasable = driver.find_element(By.ID, value=f"product{num-1}")
        try:
            driver.execute_script("arguments[0].scrollIntoView();", purchasable)
            purchasable.click()
        except selenium.common.exceptions.ElementNotInteractableException:
            pass

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("http://ozh.github.io/cookieclicker/")

WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "langSelect-EN")))

select_en = driver.find_element(By.ID, value="langSelect-EN")

select_en.click()

# WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "bigCookie")))
time.sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")

while True:
    cookie.click()
    if time.time() > timeout:
        break
    if purchase_time == 500:
        buy_upgrades()
        purchase_time = 0
    purchase_time +=1




