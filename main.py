from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("http://ozh.github.io/cookieclicker/")

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "langSelect-EN")))

select_en = driver.find_element(By.ID, value="langSelect-EN")

select_en.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "bigCookie")))

cookie = driver.find_element(By.ID, value="bigCookie")

for _ in range(100):
    cookie.click()