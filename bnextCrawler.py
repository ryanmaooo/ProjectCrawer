import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path='D:/PhantomJS/phantomjs-2.1.1-windows/bin/phantomjs.exe')
driver.get('https://www.bnext.com.tw/articles')

page = 0
while page < 3:
    driver.find_element_by_class_name('more_btn').click()
    time.sleep(1.5)
    page = page + 1

driver.encoding = 'utf'
soup = BeautifulSoup(driver.page_source, 'lxml')

i = 0
links = []
# f = open('D:/bnext.txt', 'w', encoding='UTF-8')

for soup2 in soup.select('.font_sty02'):
    links.append(soup2.parent['href'])
    res = requests.get(links[i])
    i = i + 1
    res.encoding = 'utf'
    soup2 = BeautifulSoup(res.text, "lxml")

    for soup3 in soup2.select('.left .article_summary , .main_content p , .main_content h2'):
        print(soup3.get_text(separator="\n\n", strip=True))
        # f.write(soup3.get_text(separator="\n\n", strip=True))
# f.close()
# driver.close()
print(links[len(links) - 1])
