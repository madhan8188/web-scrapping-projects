from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
driver = webdriver.Chrome("C:/Users/auraauro/Desktop/chromedriver.exe")
driver.get("https://unsplash.com/s/photos/peaceful")
content = driver.page_source
soup = bs(content, "html.parser")
x=soup.find_all('a', {"class":"_2Mc8_"})
urls=[]
href=[]
for x1 in x:
    href.append(x1.get("href")) 
    urls.append("https://unsplash.com"+x1.get("href")+"/download?force=true")
print(len(urls))
import pandas as pd
df = pd.DataFrame({'href':href,'urls':urls})
df.to_csv('unsplash_peaceful.csv', index=False, encoding='utf-8')

