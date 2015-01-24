from django.shortcuts import render_to_response
from django.views.generic.detail import DetailView

from .models import Solo


def index(request):
    solos_queryset = Solo.objects.all()

    if request.GET.get('instrument', None):
        solos_queryset = solos_queryset.filter(instrument=request.GET.get('instrument', None))

    if request.GET.get('artist', None):
        solos_queryset = solos_queryset.filter(artist=request.GET.get('artist', None))

    context = {'solos': solos_queryset}
    return render_to_response('solos/index.html', context)


class SoloDetailView(DetailView):
    model = Solo
