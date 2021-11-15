from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

username=input("Enter linkedin mail id: ")
password=input("Enter password: ")


#link="https://www.linkedin.com/mynetwork/"

driver=webdriver.Chrome(PATH)
driver.get("https://in.linkedin.com/")

search = driver.find_element_by_class_name("nav__button-secondary")
search.click()

# logging in to linkedin

search=driver.find_element_by_id("username")
search.send_keys(username)
search.send_keys(Keys.RETURN)
search=driver.find_element_by_id("password")
search.send_keys(password)
search = driver.find_element_by_class_name("login__form_action_container ")
search.click()

driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(5)

# Getting names from linkedin

for i in range(1,7):
    xpath1="./html/body/div[8]/div[3]/div/div/div/div/div/div/div/main/ul/li[3]/ul/li[i]/div/section/div[1]/a/span[2]"
    x=xpath1[:74]+str(i)+xpath1[75:]
    xpath2="/html/body/div[8]/div[3]/div/div/div/div/div/div/div/main/ul/li[1]/ul/li[i]/div/section/div[1]/a/span[2]"
    y=xpath2[:73]+str(i)+xpath2[74:]
    search=driver.find_element_by_xpath(y)
    print(search.text)
    search=driver.find_element_by_xpath(x)
    print(search.text)

time.sleep(3)
driver.close()



