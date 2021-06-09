'''
xpathh="./html/body/div[8]/div[3]/div/div/div/div/div/div/div/main/ul/li[3]/ul/li[i]/div/section/div[1]/a/span[2]"
x=xpathh[:74]
print(x)

#search=driver.find_element_by_xpath='.//*[@id="ember107"]/li-icon/svg"]'
#search.click()

names= driver.find_elements_by_class_name("discover-entity-type-card__info-container")
for name in names:
    n=names.find_element_by_class_name("Elevation-0dp discover-entity-type-card artdeco-card artdeco-card--with-hover ember-view")
    print(n)


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ember749"))
    )
    element.click()
finally:
    driver.quit()

try:
    search=driver.find_element_by_id("ember22")   # DOESNT WORK
    search.click()

except:
    time.sleep(5)
    driver.quit()

bsoup:

source=requests.get("https://www.linkedin.com/mynetwork/discover-hub/").text
soup=BeautifulSoup(source,"html")

print(soup.prettify())

mainc=soup.find('div',class_="discover-cohort-view- -list - item ember-view")
print(mainc.prettify())
'''
