from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://euw.op.gg/summoner/userName=Tetetot")

