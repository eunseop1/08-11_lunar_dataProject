import urllib.request

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def get_link_list():
    url = "https://wfwf220.com/list?toon=5790"
    urlTicker = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urlopen(urlTicker)
    soup = BeautifulSoup(res, "html.parser")

    comic_list = soup.select("section#content div.box > div > div")
    # print(len(comic_list), '개')
    c_list = comic_list[1].select("div > ul")
    # print(len(c_list), '개')
    c_list = comic_list[1].select("li")
    # print(len(c_list), '개')
    link_list = []
    for li in c_list:
        a = li.select_one("a")
        try:
            if a['href'] != '#':
                # print(a['href'])
                link_list.append(a['href'])
        except Exception as e:
            # print(e)
            pass
    link_list.reverse()
    # print(link_list)
    return link_list


if __name__ == "__main__":
    base_url = 'https://wfwf220.com'
    for link in get_link_list():
        print(base_url + link);


