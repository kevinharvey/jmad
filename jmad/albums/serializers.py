from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album
