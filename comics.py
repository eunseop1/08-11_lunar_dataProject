from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib import parse, request
from urllib.parse import urlsplit, parse_qsl


def get_link_list(url):
    urlTicker = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    res = urlopen(urlTicker)
    soup = BeautifulSoup(res, "html.parser")
    comic_list = soup.select("section#content div.box > div > div")
    c_list = comic_list[1].select("li")
    link_list = []
    for li in c_list:
        a = li.select_one("a")
        try:
            if a['href'] != '#':
                link_list.append(a['href'])
        except Exception as e:
            pass
    link_list.reverse()
    return link_list


def get_url_encoding_address(urlAddress):
    urlAddr = parse.urlparse(urlAddress)
    data = dict(parse_qsl(urlsplit(urlAddr.query).path))
    data['title'] = parse.quote(data['title'])
    encoding_query = parse.urlencode(data, doseq=False)
    address = urlAddress[:urlAddress.index('?')+1] + encoding_query
    return address


def get_images_link(urlAddress):
    urlTicker = Request(get_url_encoding_address(urlAddress), headers={'User-Agent': 'Mozilla/5.0'})
    res = urlopen(urlTicker)
    soup = BeautifulSoup(res, "html.parser")
    comic_list = soup.select("section")
    c_list = comic_list[0].select("img")
    image_link = []
    for img in c_list:
        try:
            if img['src'].endswith('.jpg'):
                image_link.append(img['src'])
        except Exception as e:
            pass
    return image_link


def image_download(path, index, image_url, ext):
    import os
    os.makedirs(path, exist_ok=True)
    file_name = "{}/{}.{}".format(path, index, ext)
    opener = request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    request.install_opener(opener)
    request.urlretrieve(image_url, file_name)
    return file_name


if __name__ == "__main__":
    base_url = 'https://wfwf220.com'
    # name= "도시정벌01부"
    # url = "https://wfwf220.com/list?toon=3910"
    # name= "도시정벌02부"
    # url = "https://wfwf220.com/list?toon=3948"
    name= "도시정벌11부"
    url = "https://wfwf220.com/list?toon=5790"
    for i, link in enumerate(get_link_list(url)):
        # print(base_url + link);
        path = "{}/{:03d}".format(name, i)
        for j, image_url in enumerate(get_images_link(base_url + link)):
            index = "{:03d}".format(j)
            image_download(path, index, image_url, 'jpg')
            # print(image)
        print("{}권 저장완료!!!".format(path))
