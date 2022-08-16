import urllib.request

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib import parse
from urllib.parse import urlsplit, parse_qsl

urlAddress = "https://wfwf220.com/view?toon=5790&num=233&title=도시정벌11부236화"
urlAddr = parse.urlparse(urlAddress)
# print(urlAddr.scheme)  # https
# print(urlAddr.netloc)  # wfwf220.com
# print(urlAddr.path)    # /view
# print(urlAddr.params)  #
# print(urlAddr.query)   # toon=5790&num=233&title=도시정벌11부236화

data = dict(parse_qsl(urlsplit(urlAddr.query).path))
# print(data)  # {'toon': '5790', 'num': '233', 'title': '도시정벌11부236화'}
# print(data['title'])  # 도시정벌11부236화
# print(parse.quote(data['title']))  # %EB%8F%84%EC%8B%9C%EC%A0%95%EB%B2%8C11%EB%B6%80236%ED%99%94
data['title'] = parse.quote(data['title'])
# print(data)  # {'toon': '5790', 'num': '233', 'title': '%EB%8F%84%EC%8B%9C%EC%A0%95%EB%B2%8C11%EB%B6%80236%ED%99%94'}
encoding_query = parse.urlencode(data, doseq=False)
# print(encoding_query)  # toon=5790&num=233&title=%25EB%258F%2584%25EC%258B%259C%25EC%25A0%2595%25EB%25B2%258C11%25EB%25B6%2580236%25ED%2599%2594

u1 = urlAddress[:urlAddress.index('?')+1]
u2 = urlAddress[urlAddress.index('?')+1:]
# print(u1)
# print(u2)
# print(u1 + encoding_query)
urlAddress = u1 + encoding_query
print(urlAddress)

# url = parse.quote("https://wfwf220.com/view?toon=5790&num=233&title=도시정벌11부236화")
# urlTicker = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
# res = urlopen(urlTicker)
# soup = BeautifulSoup(res, "html.parser")
#
# comic_list = soup.select("section")
# print(len(comic_list), '개')
# c_list = comic_list[0].select("div.group")
# print(len(c_list), '개')
# c_list = comic_list[0].select("img")
# print(len(c_list), '개')
# for img in c_list:
#     try:
#         print(img['alt'], ":", img['src'])
#     except Exception as e:
#         pass
#
#
