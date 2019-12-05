from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == "__main__":
    data = urlopen('https://www.174.co.kr/product/list.html?cate_no=65')
    soup = BeautifulSoup(data, 'lxml')

    clothes_data = soup.find_all('div', attrs={'class':'description'})

    html = '<html><head><meta charset="utf-8"></head><body>'

    for cloth_data in clothes_data:
        clothes_address = cloth_data.find('a').get('href')
        link = 'https://m.174.co.kr/' + clothes_address
        clothes_names = cloth_data.find('a').text
        html += ('<a href={}>{}</a><br/>'.format(link, clothes_names))
    html += "</body></html>"

    outputSoup = BeautifulSoup(html, "lxml")
    prettyHtml = str(outputSoup.prettify())

    with open("174.html", "w", encoding='utf8') as f:
        f.write(prettyHtml)
