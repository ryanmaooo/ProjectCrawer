#網路資源URL擷取套件 import requests
#模擬瀏覽器執行 import selenium
#HTML 剖析套件 beautifulsoup , bs4= beautifulsoup4
#beautifulsoup 會自動將輸入的文檔轉成unicode ,輸出文檔轉成utf-8

# import requests
# from bs4 import BeautifulSoup

# res = requests.get("http://house.cnyes.com/global/news/3781772.do")
# # res.encoding = 'utf' #指定編碼
# soup = BeautifulSoup(res.text,"html5lib") #指定html5lib解析器 lxml亦可 , lxml速度較 html5lib 快
# soup2 = soup.select('#article p') #定位元素
# print(soup2)

import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.bnext.com.tw/articles")
res.encoding = 'utf'
soup = BeautifulSoup(res.text,"lxml")                                   #指定html5lib解析器 lxml亦可 , lxml速度較 html5lib 快

# for soup2 in soup.select('.container-fluid .div_td .item_summary'):                       #用for迴圈取 會按照網頁<p>順序依序取出
#     print(soup2.get_text(separator="\n\n",strip=True))                                      #只取內容 去除<p>
i = 0
links= []
for soup2 in soup.select('.font_sty02'):

    links.append(soup2.parent['href'])
    res2 = requests.get('"'+links[i]+'"')
    i = i+1
    res2.encoding = 'utf'
    soup2 = BeautifulSoup(res2.text,"lxml")

    for soup3 in soup2.select('.container-fluid .div_td .item_summary'):                       #用for迴圈取 會按照網頁<p>順序依序取出
        print(soup3.get_text(separator="\n\n",strip=True))
#  print(len(links))
# print(links)








