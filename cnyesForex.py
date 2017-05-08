import requests
import time
from bs4 import BeautifulSoup
import json
import pandas as pd
url = "http://news.cnyes.com/api/v3/news/category/forex"
Sat = 1494086400
Eat = 1494172799
# Sat = 1356969600  # 20130101 00點00分00秒
# Eat = 1357055999  # 20130101 23點59分59秒
page = 1
lastpage = 1
while Sat < 1494172800:
    print("Sat=" + str(Sat))
    page = 1
    print("start")
    pl = {'startAt': Sat, 'endAt': Eat, 'limit': '30', 'page': page}
    print("check page" + str(page))
    res = requests.get(url, params=pl)
    res.close()
    restoJson = res.json()
    resJson = json.dumps(restoJson)
    rdj = json.loads(resJson)
    print("page="+str(page))
    lastpage = int(rdj['items']['last_page'])
    print("lastpage="+str(lastpage))
    while (lastpage - page) != -1:
        dataid = 0
        iftotal = rdj['items']['total']
        iftotal30 = iftotal % 30
        if (lastpage - page) == 0 or int(iftotal) < 30:
            print("data<30 or lastpage")
            while dataid < iftotal30:
                print("loading" + str(dataid))
                newsid = rdj['items']['data'][dataid]['newsId']
                newsurl = "http://news.cnyes.com/news/id/" + str(newsid)
                newsres = requests.get(newsurl, headers={"Accept": "image/webp,image/*,*/*;q=0.8",
                                                         "Accept-Encoding": "gzip, deflate, sdch",
                                                         "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
                                                         "Connection": "keep-alive",
                                                         "Referer": "http://news.cnyes.comnews/id/3792704",
                                                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
                newsres.encoding = 'utf'
                soup = BeautifulSoup(newsres.text, "lxml")
                newsres.close()
                dataid += 1
                # time.sleep(3)
                articlefinal= []
                dfList= []
                for soup2 in soup.select(
                        '._82F p'):
                    article = soup2.get_text(strip=True)
                    article2= article.rstrip()
                    dfList.append(article2)
                articlefinal.append(dfList)
                df = pd.DataFrame(articlefinal)
            df.to_csv('cnyesForex')
            print(type(df))
            # print(df)
                # dataid += 1
        else:
            while dataid < 30:
                print("loading" + str(dataid))
                newsid = rdj['items']['data'][dataid]['newsId']
                newsurl = "http://news.cnyes.com/news/id/" + str(newsid)
                newsres = requests.get(newsurl, headers={"Accept": "image/webp,image/*,*/*;q=0.8",
                                                         "Accept-Encoding": "gzip, deflate, sdch",
                                                         "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4",
                                                         "Connection": "keep-alive",
                                                         "Referer": "http://news.cnyes.comnews/id/3792704",
                                                         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
                newsres.encoding = 'utf'
                soup = BeautifulSoup(newsres.text, "lxml")
                newsres.close()
                dataid += 1
                # time.sleep(3)
                for soup2 in soup.select(
                        '._82F p'):
                    article = soup2.get_text(strip=True)
                    article2 = article.rstrip()
                    dfList.append(article2)
                articlefinal.append(dfList)
                df = pd.DataFrame(articlefinal)
            df.to_csv('cnyesForex')
            print(type(df))
            # print(df)
                # dataid += 1
        page += 1
    print("total page=" + str(page))
    Sat = Sat + 86400
    Eat = Eat + 86400
