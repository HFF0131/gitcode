import requests
import re
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import time


def getHTMLText(url):
    """获取网页"""

    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except(Exception):
        return ""


def moviePage(html):
    """解析每一个电影,并筛选出合适的电影"""
    try:
        soup = BeautifulSoup(html, 'html.parser')
        # cllink = soup.find("td", {'valign': 'top'}).find("h4", text=re.compile("(MIDE|mide)[-]?(902)"))
        title = soup.find('td', {'colspan': '2'}).find_all('a')[1]
        print(title.next_sibling)
        linktxt = soup.find("div", {'class': "tpc_content do_not_catch"}).find_all("a", text=re.compile(
            'http:\/\/www.rmdown.com\/link.php\?hash='))
        print(linktxt[0].text)
    except(Exception):
        print("")


def reurl(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find(id="tbody").find_all(class_="tal")
    for item in items:
        item = item.find('a')
        item_text = item.get_text()
        reitem = re.search(".*?HD.*?(MIDE|mide)[-]?(902)", item_text)
        if not (reitem is None):
            href = 'https://cl.do57.xyz/' + item.attrs['href']
            page_href.append(href)


def main():
    test_url = url
    for i in range(1, 20):
        html = getHTMLText(test_url)
        reurl(html)
        for item in page_href:
            t_page = getHTMLText(item)
            moviePage(t_page)
        i = i + 1
        test_url = 'https://cl.do57.xyz/thread0806.php?fid=15&search=&page=' + str(i)
        print('*******************************************')
        print(test_url)
        time.sleep(3)

# for item in items:
#     author = item.find('.UserLink-link').text()
#     answer = item.find('.RichContent-inner span').text()
#     file = open('explore.txt', 'w', encoding='utf-8')
#     file.write('\n'.join([author, answer]))
#     file.write('\n' + '=' * 50 + '\n')
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    url = 'https://cl.do57.xyz/thread0806.php?fid=15&search=&page=1'
    page_href = []
    main()
