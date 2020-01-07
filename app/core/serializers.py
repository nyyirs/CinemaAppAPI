from rest_framework import serializers


class MovieDetailSerializer(serializers.Serializer):

    movieNumb = serializers.IntegerField()
