from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Beat

# Create your views here.

def all_beats(request):
    """ A view to show all beats, including sorting and search queries """

    beats = Beat.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('beats'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            beats = beats.filter(queries)

    context = {
        'beats': beats,
        'search_term': query,
    }

    return render(request, 'beats/beats.html', context)


def beat_detail(request, beat_id):
    """ A view to show individual beat details """

    beat = get_object_or_404(Beat, pk=beat_id)

    context = {
        'beat': beat,
    }

    return render(request, 'beats/beat_detail.html', context)