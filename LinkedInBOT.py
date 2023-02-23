import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://linkedin.com/uas/login")
time.sleep(5)

username = driver.find_element(By.ID,"username")
username.send_keys("__YOUR USERNAME__")

pword = driver.find_element(By.ID,"password")
pword.send_keys("__YOUR PASSWORD__")

driver.find_element(By.XPATH,"//button[@type='submit']").click()

profile_url = input("Enter The Profile URL : ")
driver.get(profile_url)

#Scrolling Script

start = time.time()
initialScroll = 0
finalScroll = 1000

while(True):
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    initialScroll = finalScroll
    finalScroll+=1000
    time.sleep(3)
    
    end=time.time()
    if round(end-start)>10:
        break
        
################
#getting page source
src = driver.page_source
soup = BeautifulSoup(src,'lxml')

#getting page introduction
intro = soup.find('div',{'class':'pv-text-details__left-panel'})

#Extracting HTML
name_loc  = intro.find('h1')
name = name_loc.get_text().strip()

work_loc = intro.find("div",{'class':'text-body-medium'})
work = work_loc.get_text().strip()

connection_loc = intro.find_all("span", {'class': 'text-body-small'})
connection = connection_loc[0].get_text().strip()

location_loc = f"/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/section[1]/div[2]/div[2]/div[2]/span[1]"
location = driver.find_element(By.XPATH,location_loc)

print("Name : ",name)
print("Works As : ",work)
print("Connection : ",connection)
print("Location : ",location.text)

#Going to jobs page
jobs = driver.find_element(By.XPATH,"//*[@id='global-nav']/div/nav/ul/li[3]/a")
jobs.click()