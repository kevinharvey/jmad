from django.shortcuts import render_to_response

from rest_framework import viewsets, mixins

from .models import Solo
from .tasks import get_artist_tracks_from_musicbrainz
from .serializers import SoloSerializer


def index(request):
    context = {'solos': []}

    if request.GET.keys():
        solos_queryset = Solo.objects.all()

        if request.GET.get('instrument'):
            solos_queryset = solos_queryset.filter(instrument=request.GET['instrument'])

        artist_kwarg = request.GET.get('artist', None)
        if artist_kwarg:
            solos_queryset = solos_queryset.filter(artist=artist_kwarg)

        context['solos'] = solos_queryset

        if context['solos'].count() == 0 and artist_kwarg:
            get_artist_tracks_from_musicbrainz.delay(artist=artist_kwarg)

    return render_to_response('solos/index.html', context)


def solo_detail(request, album, track, artist):
    context = {
        'solo': Solo.objects.get(slug=artist, track__slug=track, track__album__slug=album)
    }

    return render_to_response('solos/solo_detail.html', context)


class SoloViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin):
    queryset = Solo.objects.all()
    serializer_class = SoloSerializer

