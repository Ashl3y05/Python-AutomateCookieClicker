from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=edge_options)

driver.get("http://ozh.github.io/cookieclicker/")

select_en = driver.find_element(By.ID, value="langSelect-EN")

select_en.click()