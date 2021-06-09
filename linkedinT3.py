from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymongo import MongoClient
from collections import defaultdict
import time
import os

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

PATH = "C:\Program Files (x86)\chromedriver.exe"

username=input("Enter linkedin mail id: ")
password=input("Enter password: ")

connection_string = os.getenv("connection_string")
client = MongoClient(connection_string)
mydb = client["mydb"]
mycol = mydb["people"]

driver = webdriver.Chrome(PATH)
driver.get("https://in.linkedin.com/")
dict1 = defaultdict(list)
dict2 = defaultdict(list)


search = driver.find_element_by_class_name("nav__button-secondary")
search.click()

# logging in to linkedin

search = driver.find_element_by_id("username")
search.send_keys(username)

search.send_keys(Keys.RETURN)

search = driver.find_element_by_id("password")
search.send_keys(password)

search = driver.find_element_by_class_name("login__form_action_container ")
search.click()

driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(5)

# Getting names from linkedin

for i in range(1,6):

    xpath1 = "./html/body/div[8]/div[3]/div/div/div/div/div/div/div/main/ul/li[3]/ul/li[i]/div/section/div[1]/a/span[2]"

    x = xpath1[:74]+str(i)+xpath1[75:]

    xpath2 = "/html/body/div[8]/div[3]/div/div/div/div/div/div/div/main/ul/li[1]/ul/li[i]/div/section/div[1]/a/span[2]"

    y = xpath2[:73]+str(i)+xpath2[74:]

    search = driver.find_element_by_xpath(y)

    dict1["name"].append(search.text)

    #mycol.insert_one(dict1)
    search=driver.find_element_by_xpath(x)

    #mycol.insert_one(dict2)
    dict2["name"].append(search.text)

z = merge_two_dicts(dict1, dict2)

#mycol.insert_one(dict1)
#mycol.insert_one(dict2)

mycol.insert_one(z)

time.sleep(5)

driver.close()

print("done")

    

