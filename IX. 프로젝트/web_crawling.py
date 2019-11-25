from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == "__main__":
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=695796")
    soup = BeautifulSoup(data, "lxml")  #httpResponse -> HTML
    print(soup)
    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = soup.find_all("td", attrs= {"class":"title"}) # <td class="title"> --- </td>
    for cartoon_title in cartoon_titles:                        # cartoon_title[:2}
        title = cartoon_title.find("a").text                        #텍스트 가져오기 <a>text</a>
        link = cartoon_title.find("a").get("href")                  #태그의 속성값 가져오기 <a href="">text</a>
        link = "http://comic.naver.com" + link
        # print(title)
        # print(link)
        html += "<a href='{}'>{}</a><br/>".format(link, title)

    html += "</body></html>"
    # print(html)
    with open("내일.html", "w", encoding='utf8') as f:
        f.write(html)