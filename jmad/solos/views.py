from django.shortcuts import render_to_response

from .models import Solo


def index(request):
    solos_queryset = Solo.objects.all()

    if request.GET.get('instrument', None):
        solos_queryset = solos_queryset.filter(instrument=request.GET.get('instrument', None))

    artist_kwarg = request.GET.get('artist', None)
    if artist_kwarg:
        solos_queryset = solos_queryset.filter(artist=artist_kwarg)

    context = {'solos': solos_queryset}

    if context['solos'].count() == 0 and artist_kwarg:
        context['solos'] = Solo.get_artist_tracks_from_musicbrainz(artist_kwarg)

    return render_to_response('solos/index.html', context)


def solo_detail(request, album, track, artist):
    context = {
        'solo': Solo.objects.get(slug=artist, track__slug=track, track__album__slug=album)
    }
    return render_to_response('solos/solo_detail.html', context)
