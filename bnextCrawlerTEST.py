import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

url = 'https://www.bnext.com.tw/articles'
driver = webdriver.PhantomJS(executable_path='D:/PhantomJS/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get(url)

page = 0
while page < 1:
    driver.find_element_by_class_name('more_btn').click()
    # time.sleep(2)
    page = page + 1
driver.encoding = 'utf'
soup = BeautifulSoup(driver.page_source, 'lxml')

i = 0
links = []
articlefinal = []
for soup2 in soup.select('.font_sty02'):
    links.append(soup2.parent['href'])
    res = requests.get(links[i])
    i = i + 1
    res.encoding = 'utf'
    soup2 = BeautifulSoup(res.text, "lxml")
    dfList = []
    for soup3 in soup2.select(
            '#article_view_body > div.main_block > div > div > div.content.htmlview > div > div.left > article.main_content'):
        article = soup3.get_text(strip=True)
        article2 = article.rstrip()
        dfList.append(article2)
    articlefinal.append(dfList)
df = pd.DataFrame(articlefinal)
driver.close()
df.to_csv('bnext.csv')
print(df)
