from django.conf import settings
from django.shortcuts import get_object_or_404
from beats.models import Beat

def bag_contents(request):

    bag_items = []
    total = 0
    beat_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        beat = get_object_or_404(Beat, pk=item_id)
        total += quantity * beat.price
        beat_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'beat': beat,
        })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'beat_count': beat_count,
        'grand_total': grand_total,
    }

    return context