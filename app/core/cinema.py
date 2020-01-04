import requests
from bs4 import BeautifulSoup
import re


class Theaters():

    def __init__(self):

        self.movieList = {}
        self.movieDetails = []
        self.movieInfo = {}

    def getMovieList(self, url):

        try:
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')

            results = soup.find_all(
                'figure', class_='text-center u-block-hover mb-0')

            for index, item in enumerate(results):
                title = item.find('a')
                img = item.find('img')
                self.movieList[index] = {
                    'title': title.get('title'),
                    'img': img.get('src'),
                    'details': title.get('href')
                }

            return (self.movieList)

        except:

            return ('Error - unable to retrieve information from source')

    def getMovieDetail(self, url, className):
        self.movieDetails = []
        try:
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')

            results = soup.find(
                'div', id=className).find_all('td')

            for item in results:

                data = item.findChildren(text=True)

                data = [re.sub('[^a-zA-Z0-9]+', '', _) for _ in data]

                data = ' '.join(data).split()
                self.movieDetails.append(data)

            return (self.movieDetails)

        except:

            return ('Error - unable to retrieve information from source')

    def bagatelle(self):

        return (self.getMovieList(
            'https://www.myt.mu/sinformer/cinema/les-salles/19/cinema-star-bagatelle'))

    def trianon(self):

        return (self.getMovieList('https://www.myt.mu/sinformer/cinema/les-salles/23/cinema-mcine'))

    def caudan(self):

        return (self.getMovieList('https://www.myt.mu/sinformer/cinema/les-salles/10/cinema-star-caudan'))

    def flacq(self):

        return (self.getMovieList('https://www.myt.mu/sinformer/cinema/les-salles/24/cinema-mcineflacq'))
