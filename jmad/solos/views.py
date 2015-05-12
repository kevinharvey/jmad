from django.shortcuts import render_to_response

from .models import Solo


def index(request):
    context = {'solos': []}

    if request.GET.keys():
        solos_queryset = Solo.objects.all()

        if request.GET.get('instrument'):
            solos_queryset = solos_queryset.filter(instrument=request.GET['instrument'])

        if request.GET.get('artist', None):
            solos_queryset = solos_queryset.filter(artist=request.GET['artist'])

        context['solos'] = solos_queryset

    return render_to_response('solos/index.html', context)


def solo_detail(request, album, track, artist):
    context = {
        'solo': Solo.objects.get(slug=artist, track__slug=track, track__album__slug=album)
    }

    return render_to_response('solos/solo_detail.html', context)

