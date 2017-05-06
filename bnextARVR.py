import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
url = "https://www.bnext.com.tw/categories/vr"
rel = 0
rel2 = 1
# while (rel-rel2)!=0:
while rel < 13:
    j = 0
    links1 = []
    driver = webdriver.PhantomJS(executable_path='D:/PhantomJS/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.get(url)
    print("loading driver complete")
    driver.execute_script("document.querySelector('div.more_btn').setAttribute('rel1','" + str(rel) + "')")
    rel2 = int(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    driver.find_element_by_class_name('more_btn').click()
    # time.sleep(3)
    print("loading complete2")
    driver.encoding = 'utf'
    dps = driver.page_source
    soup = BeautifulSoup(dps, "lxml")
    rel = int(driver.find_element_by_class_name('more_btn').get_attribute("rel1"))
    articlefinal = []
    for soup21 in soup.select("div.tg_list div.item_title"):
        links1.append(soup21.parent['href'])
        res21 = requests.get(links1[j])
        res21.encoding = 'utf'
        soup21 = BeautifulSoup(res21.text, "lxml")
        print("request" + str(j))
        j += 1
        # time.sleep(3)
        dfList = []
        for soup31 in soup21.select(
                '#article_view_body > div.main_block > div > div > div.content.htmlview > div > div.left > article.main_content'):
            article = soup31.get_text(strip=True)
            article2 = article.rstrip()
            dfList.append(article2)
        articlefinal.append(dfList)
        df = pd.DataFrame(articlefinal)
    driver.close()
    df.to_csv('bnextARVR.csv')
    print(df)