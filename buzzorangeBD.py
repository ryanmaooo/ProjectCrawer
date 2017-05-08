import requests
from bs4 import BeautifulSoup
import pandas as pd

k = 1
links = []
j = 0
url = "https://buzzorange.com/techorange/?s=%E5%A4%A7%E6%95%B8%E6%93%9A"
x = 1
while x < 90:
    res = requests.get(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
    res.encoding = 'utf'
    soup = BeautifulSoup(res.text, "lxml")
    res.close()
    articlefinal =[]
    for souplink in soup.select(" header > h4"):
        links.append(souplink.a['href'])
        feedres = requests.get(links[j], headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"})
        feedres.encoding = 'utf'
        soupfeeds = BeautifulSoup(feedres.text, "lxml")
        feedres.close()
        print("value"+str(k))
        dfList=[]
        for soupfeed in soupfeeds.select(
                '#main p'):
            article = soupfeed.get_text(strip=True)
            article2 = article.rstrip()
            dfList.append(article2)
        articlefinal.append(dfList)
        df = pd.DataFrame(articlefinal)
        j += 1
    x += 1
    df.to_csv('buzzorangeBD')
    print(df)
    url = "https://buzzorange.com/techorange/page/" + str(x) + "/?s=%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7"
    print("page" + str(x))