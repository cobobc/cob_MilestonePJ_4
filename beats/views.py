from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Beat, Genre, Review
from .forms import BeatForm, ReviewForm

# Create your views here.


def all_beats(request):
    """ A view to show all beats, including sorting and search queries """

    beats = Beat.objects.all()
    query = None
    genres = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                beats = beats.annotate(lower_name=Lower('name'))
            if sortkey == 'genre':
                sortkey = 'genre__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            beats = beats.order_by(sortkey)

    if request.GET:
        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            beats = beats.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('beats'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            beats = beats.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'beats': beats,
        'search_term': query,
        'current_genres': genres,
    }

    return render(request, 'beats/beats.html', context)


def beat_detail(request, beat_id):
    """ A view to show individual beat details """

    beat = get_object_or_404(Beat, pk=beat_id)
    form = ReviewForm(instance=beat)
    reviews = Review.objects.filter(beat=beat)

    context = {
        'form': form,
        'beat': beat,
        'reviews': reviews,
    }

    return render(request, 'beats/beat_detail.html', context)


@login_required
def add_beat(request):
    """ Add a beat to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BeatForm(request.POST, request.FILES)
        if form.is_valid():
            beat = form.save()
            messages.success(
                request, 'Successfully added a new beat to the store!')
            return redirect(
                reverse('beat_detail', args=[beat.id]))
        else:
            messages.error(
                request, 'Failed to add beat. Please ensure the form is valid.'
                )
    else:
        form = BeatForm()

    template = 'beats/add_beat.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_beat(request, beat_id):
    """ Edit a beat in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    beat = get_object_or_404(Beat, pk=beat_id)
    if request.method == 'POST':
        form = BeatForm(request.POST, request.FILES, instance=beat)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Successfully updated beat!')
            return redirect(reverse('beat_detail', args=[beat.id]))
        else:
            messages.error(
                request, 'Failed to update beat. Please check the form.')
    else:
        form = BeatForm(instance=beat)
        messages.info(request, f'You are editing {beat.name}')

    template = 'beats/edit_beat.html'
    context = {
        'form': form,
        'beat': beat,
    }

    return render(request, template, context)


@login_required
def delete_beat(request, beat_id):
    """ Delete a beat from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    beat = get_object_or_404(Beat, pk=beat_id)
    beat.delete()
    messages.success(request, 'Beat deleted!')
    return redirect(reverse('beats'))


@login_required
def add_review(request, beat_id):
    """ Add a review of a beat """
    beat = get_object_or_404(Beat, pk=beat_id)
    if request.user.is_authenticated:
        if request.method == 'POST':

            form = ReviewForm(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.beat = beat
                form.user = request.user
                form.save()
                messages.success(
                    request, 'Successfully posted your review!')
                return redirect(reverse('beat_detail', args=[beat_id]))
            else:
                messages.error(
                    request, 'Failed to add review.')

    return redirect(reverse('beat_detail', args=[beat_id]))


@login_required
def edit_review(request, beat_id, review_id):
    """ Edit a review """
    beat = get_object_or_404(Beat, pk=beat_id)
    review = get_object_or_404(Review, pk=review_id)
    if not request.user == review.user:
        messages.error(request, 'Sorry you are not permitted to do this')
        return redirect(reverse('beat_detail', args=[beat_id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form = form.save(commit=False)
            form.beat = beat
            form.user = request.user
            form.save()
            messages.success(
                request, 'Successfully updated your review!')
            return redirect(reverse('beat_detail', args=[beat_id]))
        else:
            messages.error(
                request, 'Failed to update review. \
                    Please check review details.')

    else:
        form = ReviewForm(instance=review)

    context = {
        'form': form,
        'beat': beat,
        'review': review,
    }

    return render(request, 'beats/edit_review.html', context)


@login_required
def delete_review(request, beat_id, review_id):
    """ Delete a review """

    review = Review.objects.get(id=review_id)
    if review.user == request.user:
        review.delete()
        messages.success(request, 'Review deleted!')
        return redirect(reverse('beat_detail', args=[beat_id]))

    else:
        messages.error(request, "You are not permitted to do that.")

    return redirect(reverse('beat_detail', args=[beat_id]))
