from django.shortcuts import render
from .models import Beat

# Create your views here.

def all_beats(request):
    """ A view to show all beats, including sorting and search queries """

    beats = Beat.objects.all()

    context = {
        'beats': beats,
    }

    return render(request, 'beats/beats.html', context)