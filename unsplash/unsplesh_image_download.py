import pandas as pd 
import requests 
from bs4 import BeautifulSoup 
import re
import requests
import time
from pandas.io.json import json_normalize
import glob
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager

try:
    driver = webdriver.Chrome("C:/Users/auraauro/Desktop/chromedriver.exe") 
except:
    driver=  webdriver.Chrome(ChromeDriverManager().install())

# driver=  webdriver.Chrome(ChromeDriverManager().install())
# driver = webdriver.Chrome("C:/Users/auraauro/Desktop/chromedriver.exe")
# driver.get("https://unsplash.com/s/photos/peaceful")


def proxy_service(url):
    r = requests.get(url, proxies = proxy, verify = False)
    print("request with proxy",r)
    return r

def use_requests(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0'}
    r = requests.get(url, headers=headers, timeout=100 )
    print(r)
    # r = requests.get(url) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    soup
    href_link = []
    for link in soup.findAll('a', attrs={'href': re.compile("^https://unsplash.com/photos/")}):
        # print (link.get('href'))
        dicts = {}
        dicts['download'] = link.get('href')
        dicts['short_code'] = link.get('href').split('photos/')[1].split('/download')[0]
        href_link.append(dicts)
        
    # print(href_link)
    dict = href_link
    df = pd.DataFrame(dict) 
    print(df)
    return df



def return_unsplesh_urls(driver, url,num):
    driver.get(url)
    time.sleep(3)
    image_urls = []
    total_urls = 0
    old_urls = 0
    counter = 0
    while counter < 5:
        image_url_divs = driver.find_elements_by_xpath(
            '//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div/div/div[1]/div/figure/div/div/div/div/a')
        for url_div in image_url_divs:
            try:
                url = (url_div.get_attribute('href') )  
                image_urls.append(url)
            except Exception as e:
                print(e)
        total_urls = len(set(image_urls))
        if total_urls == old_urls:
            counter += 1
        else:
            old_urls = total_urls
            counter = 0
        print("Collected", total_urls, "URLs...")
        scroll_timer = 0
        while scroll_timer < 5  and total_urls<num:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            scroll_timer += 1
    df = pd.DataFrame()
    df["post_url"] = image_urls
    df.drop_duplicates("post_url", inplace=True)
    return df


def get_image_urls(driver, url,num):
    driver.get(url)
    time.sleep(3)
    image_urls = []
    total_urls = 0
    old_urls = 0
    counter = 0
    while counter < 5:
        content = driver.page_source
        soup = BeautifulSoup(content, "html.parser")
        x=soup.find_all('a', {"class":"_2Mc8_"})
        image_urls=[]
        href=[]
        for x1 in x:
            href.append(x1.get("href")) 
            image_urls.append("https://unsplash.com"+x1.get("href")+"/download?force=true")
        print(len(image_urls))
        total_urls = len(set(image_urls))
        if total_urls == old_urls:
            counter += 1
        else:
            old_urls = total_urls
            counter = 0
        print("Collected", total_urls, "URLs...")
        scroll_timer = 0
        while scroll_timer < 10  and total_urls<num:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            scroll_timer += 1
    df = pd.DataFrame()
    df["post_url"] = image_urls
    df.drop_duplicates("post_url", inplace=True)
    return df



# tag = 'peaceful'
# num = 500
# url='https://unsplash.com/s/photos/'+tag

# df = get_image_urls(driver,url,num)
# print(df)

# df.to_csv(tag+'.csv')

driver = webdriver.Chrome("C:/Users/auraauro/Desktop/chromedriver.exe")
csv_list = pd.read_excel('emotions.xlsx')
lists = list(csv_list['Unnamed: 1'])



scroll_timer=0
tag = lists[39]
print(tag)
driver.get("https://unsplash.com/s/photos/"+tag)
while scroll_timer < 10000 :
    # print(scroll_timer)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    scroll_timer += 1
time.sleep(3)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
x=soup.find_all('a', {"class":"_2Mc8_"})
urls=[]
href=[]
for x1 in x:
    href.append(x1.get("href")) 
    urls.append("https://unsplash.com"+x1.get("href")+"/download?force=true")
print(len(urls))
import pandas as pd
df = pd.DataFrame({'href':href,'urls':urls})
df.to_csv(tag+'.csv', index=False, encoding='utf-8')



















