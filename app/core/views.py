from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import cinema, serializers


# Create your views here.

theaters = cinema.Theaters()


class BagatelleView(APIView):

    serializer_class = serializers.MovieDetailSerializer

    def get(self, request, format=None):

        return Response({'Movies': theaters.bagatelle()})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            movieUrl = serializer.validated_data.get('movieUrl')
            return Response({'MovieInfo': theaters.getMovieDetail(movieUrl, 'accordion-07-body-19')})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class TrianonView(APIView):

    serializer_class = serializers.MovieDetailSerializer

    def get(self, request, format=None):

        return Response({'Movies': theaters.trianon()})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            movieUrl = serializer.validated_data.get('movieUrl')
            return Response({'MovieInfo': theaters.getMovieDetail(movieUrl, 'accordion-07-body-23')})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class CaudanView(APIView):

    serializer_class = serializers.MovieDetailSerializer

    def get(self, request, format=None):

        return Response({'Movies': theaters.caudan()})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            movieUrl = serializer.validated_data.get('movieUrl')
            return Response({'MovieInfo': theaters.getMovieDetail(movieUrl, 'accordion-07-body-10')})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class FlacqView(APIView):

    serializer_class = serializers.MovieDetailSerializer

    def get(self, request, format=None):

        return Response({'Movies': theaters.flacq()})

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            movieUrl = serializer.validated_data.get('movieUrl')
            return Response({'MovieInfo': theaters.getMovieDetail(movieUrl, 'accordion-07-body-24')})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
