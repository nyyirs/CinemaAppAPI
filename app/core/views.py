from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from bs4 import BeautifulSoup


# Create your views here.


class BagatelleView(APIView):

    def get(self, request, format=None):

        movies = {}
        try:
            URL = "https://www.myt.mu/sinformer/cinema/les-salles/19/cinema-star-bagatelle"

            page = requests.get(URL)

            soup = BeautifulSoup(page.content, 'html.parser')

            results = soup.find_all(
                'figure', class_='text-center u-block-hover mb-0')

            for index, item in enumerate(results):
                title = item.find('a')
                img = item.find('img')
                movies[index] = {
                    'title': title.get('title'),
                    'img': img.get('src'),
                    'details': title.get('href')
                }

            return Response({'Movies': movies})

        except:

            return Response({'Error': 'Could not retrieve information from source'})
