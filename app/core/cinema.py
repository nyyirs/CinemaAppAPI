import requests
from bs4 import BeautifulSoup
import http.client
import re

http.client._MAXHEADERS = 1000


def getMovieDetails(url):
    try:
        # Get each movile link

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')

        links = soup.find_all(
            'a', class_='vh_button yellow icon-play-1 hover_right')

        movieLinks = []

        for elem in links:

            movieLinks.append('https://cinema.mu' + elem.get('href'))

        # Navigate to individual movie page

        movieInfo = {}

        for index, url in enumerate(movieLinks):

            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')

            title = soup.find('div', class_='page_title event').string
            try:
                duration = soup.find('div', class_='info movies_length').string
            except:
                duration = 'N/A'
            image = soup.find('img', class_='open_entry_image').get('src')
            try:
                rating = soup.find(
                    'div', class_='info event_imdb_rating').text
            except:
                rating = 'N/A'

            schedules = soup.find('div', class_='panel-body').find_all('td')
            showTimes = []
            for time in schedules:

                data = time.findChildren(text=True)
                data = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in data]
                data = ' '.join(data).split()
                showTimes.append(data)

            movieInfo[index] = {

                'title': title,
                'image': 'https://cinema.mu/' + image,
                'rating': rating,
                'duration': duration,
                'showTimes': showTimes

            }

        return (movieInfo)
    except Exception as e:
        return ('Error: ' + str(e))
