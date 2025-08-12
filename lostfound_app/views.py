from django.shortcuts import render
from django.db.models import Q
from .models import LostItem, FoundItem

def home(request):
    return render(request, 'lostfound_app/home.html')

def report_lost(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        contact_number = request.POST.get('contact_number')  # New line

        lost_item = LostItem.objects.create(
            item_name=item_name,
            description=description,
            location=location,
            contact_number=contact_number
        )

        matches = FoundItem.objects.filter(
            Q(item_name__icontains=lost_item.item_name),
            Q(location__icontains=lost_item.location)
        )
        return render(request, 'lostfound_app/matches.html', {
            'matches': matches,
            'item_type': 'lost',
            'item_name': lost_item.item_name
        })

    return render(request, 'lostfound_app/report_lost.html')

def report_found(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')
        description = request.POST.get('description')
        location = request.POST.get('location')
        contact_number = request.POST.get('contact_number')  # New line

        found_item = FoundItem.objects.create(
            item_name=item_name,
            description=description,
            location=location,
            contact_number=contact_number
        )

        matches = LostItem.objects.filter(
            Q(item_name__icontains=found_item.item_name),
            Q(location__icontains=found_item.location)
        )
        return render(request, 'lostfound_app/matches.html', {
            'matches': matches,
            'item_type': 'found',
            'item_name': found_item.item_name
        })

    return render(request, 'lostfound_app/report_found.html')
