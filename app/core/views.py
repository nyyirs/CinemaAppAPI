from rest_framework.views import APIView
from rest_framework.response import Response
from . import cinema


# Create your views here.

theaters = cinema.Theaters()


class BagatelleView(APIView):

    def get(self, request, format=None):

        return Response({'Movies': theaters.bagatelle()})


class TrianonView(APIView):

    def get(self, request, format=None):

        return Response({'Movies': theaters.trianon()})


class CaudanView(APIView):

    def get(self, request, format=None):

        return Response({'Movies': theaters.caudan()})


class FlacqView(APIView):

    def get(self, request, format=None):

        return Response({'Movies': theaters.flacq()})
