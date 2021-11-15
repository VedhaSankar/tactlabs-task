from bs4 import BeautifulSoup
import requests


with open("sample.html") as html_file:
    soup= BeautifulSoup(html_file,"lxml")    #    will fetch the html code.

print(soup.prettify())   # will print the html code
    
title= soup.title.text   # title of html  code,,,first one in the dec


match = soup.find("div",class_="footer")
print(match)
print(match.p.text)  # will print just the footer info


article = soup.find("div", class_="article") # code in the first article div stored in div
print(article.a.text)  # prints text in first article div

summary = article.p.text     
print(summary)      # prints content of first article div


for article in soup.find_all("div",class_="article"):    # prints article title and summary in all divs
    print(article.a.text)
    print(article.p.text)
    print()
