import requests
from bs4 import BeautifulSoup


class Theaters():

    def __init__(self):

        self.movies = {}

    def getMovieList(self, url):

        try:
            page = requests.get(url)

            soup = BeautifulSoup(page.content, 'html.parser')

            results = soup.find_all(
                'figure', class_='text-center u-block-hover mb-0')

            for index, item in enumerate(results):
                title = item.find('a')
                img = item.find('img')
                self.movies[index] = {
                    'title': title.get('title'),
                    'img': img.get('src'),
                    'details': title.get('href')
                }

            return (self.movies)

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
