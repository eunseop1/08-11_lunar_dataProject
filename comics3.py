from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib import parse, request
from urllib.parse import urlsplit, parse_qsl


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
                # print(img['alt'], ":", img['src'])
                image_link.append(img['src'])
        except Exception as e:
            pass
    return image_link


def image_download(path, index, image_url, ext):
    import os
    os.makedirs(path, exist_ok=True)
    file_name = "{}/{:03d}.{}".format(path, index, ext)
    opener = request.build_opener()
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    request.install_opener(opener)
    request.urlretrieve(image_url, file_name)
    print(file_name, '저장완료!!!')


urlAddress = "https://wfwf220.com/view?toon=5790&num=233&title=도시정벌11부236화"
print(get_url_encoding_address(urlAddress))
for image in get_images_link(urlAddress):
    print(image)

image_download('001', 1, get_images_link(urlAddress)[0],'jpg')

