import time
from  selenium import webdriver
from selenium.webdriver.common.by import By

url = input("Enter Product URL : ")
driver = webdriver.Chrome()
driver.get(url)

#CHeckes for the text inside availability ID
stock = driver.find_element(By.XPATH,'//*[@id="availability"]')
print(stock.text) #Takes the text inside from the <span> tag