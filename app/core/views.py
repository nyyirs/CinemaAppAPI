from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import cinema as m


# Create your views here.

class BagatelleView(APIView):

    def get(self, request, format=None):

        return Response({'Movies': m.getMovieDetails('https://cinema.mu/cinema-movie-theatres-in-mauritius/star-cinema-bagatelle/')})


class TrianonView(APIView):
    def get(self, request, format=None):

        return Response({'Movies': m.getMovieDetails('https://cinema.mu/cinema-movie-theatres-in-mauritius/cinema-mcine-trianon/')})


class CaudanView(APIView):
    def get(self, request, format=None):

        return Response({'Movies': m.getMovieDetails('https://cinema.mu/cinema-movie-theatres-in-mauritius/star-cinema-le-caudan/')})


class FlacqView(APIView):
    def get(self, request, format=None):

        return Response({'Movies': m.getMovieDetails('https://cinema.mu/cinema-movie-theatres-in-mauritius/mcine-flacq/')})
