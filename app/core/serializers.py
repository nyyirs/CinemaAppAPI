from rest_framework import serializers


class MovieDetailSerializer(serializers.Serializer):

    movieUrl = serializers.CharField()
