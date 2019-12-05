from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "https://www.youtube.com/feed/trending"
    with requests.text(url) as response:
        soup = BeautifulSoup(response.text, 'lxml')

    youtube_titles = soup.select('#video-title')

    for youtube_title in youtube_titles:
        title = youtube_title.find('a').text
        address = youtube_title.find('a').get('href')

        print(title)
        print(address)
