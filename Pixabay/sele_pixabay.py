from selenium import webdriver
driver = webdriver.Chrome("/home/stemland/Downloads/chromedriver")
likes = []
stars = []
cmnts = []
url = []
url_fin = []
alt_tab=[]
page_no=1
while(page_no<=3):
    webpage = "https://pixabay.com/images/search/?pagi={}".format(page_no)
    page_no=page_no+1
    driver.get(webpage)
    content = driver.page_source
    from bs4 import BeautifulSoup as bs
    soup = bs(content, "html.parser")
    '''meta_content'''
    i=0
    for s in soup.find_all('meta'):
        if(i>=5):
            url.append(s.get('content'))
        i=i+1
    #print(len(url_fin))
    #print(len(url))
    #for u in url_fin:
        #print(u.split("_")[0])
    '''likes,cmnt,share'''
    packets = soup.findAll("div", {"class": "counts hide-xs hide-sm"})
    #print(len(packets))
    for pack in packets:
        a = pack.text
        a = a.split(" ")
        likes.append(a[1])
        stars.append(a[2])
        cmnts.append(a[3])
        '''images tag'''
    images = soup.findAll('img')
    for image in images:
        # print image source
        # print alternate text
        cd=image.get("alt")
        alt_tab.append(cd)
###print("=========================================================")
#print(likes)
#print("=========================================================")
#print(stars)
#print("=========================================================")
#print(cmnts)
#print("=========================================================")
#print(url)
#print("=========================================================")
#print(alt_tab)
name_tag1= [name for name in alt_tab if name!=None]
url_fin=[url[i] for i in range(len(url)) if i%2==0]
import pandas as pd
df = pd.DataFrame({'likes':likes,'No_of_comments':cmnts,'Star_Ratings':stars,'img_url_320':url_fin,'search_tags':name_tag1})
df['img_url_1280'] = [x.replace("__340","_1280") for x in df['img_url_320']]
df.to_csv('pixabay_sha.csv', index=False, encoding='utf-8')

    # for image in images:
    # print(image['alt'])