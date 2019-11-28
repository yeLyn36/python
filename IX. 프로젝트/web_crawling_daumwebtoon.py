import json
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == "__main__":
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/fivedisciple") as data:
        datafile = json.loads(data.read())
        html = "<html><head><meta charset='utf-8'></head><body>"
        cartoon_titles = datafile["data"]["webtoon"]["webtoonEpisodes"]
        for cartoon_title in cartoon_titles:
            title = cartoon_title["title"]
            thumbnail = cartoon_title["thumbnailImage"]["url"]
            url = cartoon_title["id"]
            url = "http://webtoon.daum.net/webtoon/view/"+str(url)
            html += "<a href='{}'><img src={}/>{}</a><br/>".format(url, thumbnail, title)
        html += "</body></html>"

        outputSoup = BeautifulSoup(html, "lxml")
        prettyHtml = str(outputSoup.prettify())

        with open("샬롯에게는 다섯 명의 제자가 있다.html", "w", encoding='utf8') as f:
            f.write(prettyHtml)