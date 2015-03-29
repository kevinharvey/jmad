from rest_framework import viewsets, mixins

from .models import Album
from .serializers import AlbumSerializer


class AlbumViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
