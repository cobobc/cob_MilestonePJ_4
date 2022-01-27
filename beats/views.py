from django.shortcuts import render, get_object_or_404
from .models import Beat

# Create your views here.

def all_beats(request):
    """ A view to show all beats, including sorting and search queries """

    beats = Beat.objects.all()

    context = {
        'beats': beats,
    }

    return render(request, 'beats/beats.html', context)


def beat_detail(request, beat_id):
    """ A view to show individual beat details """

    beat = get_object_or_404(Beat, pk=beat_id)

    context = {
        'beat': beat,
    }

    return render(request, 'beats/beat_detail.html', context)