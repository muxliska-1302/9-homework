from django.shortcuts import render, redirect,get_object_or_404
from .models import Sport


def event_list(request):
    sports = Sport.objects.all()
    ctx = {'sports':sports}
    return render(request, 'sports/event-list.html', ctx)

def create_event(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        location=request.POST.get('location')
        date=request.POST.get('date')
        sport_type=request.POST.get('sport_type')
        if name and location and date and sport_type:
            Sport.objects.create(
                name = name,
                location = location,
                date = date,
                sport_type = sport_type
            )
            return redirect('sports:list')
    return render(request, 'sports/event-create.html')

def event_detail(request, event_id):
    sport = get_object_or_404(Sport, pk=event_id)
    ctx = {'sport':sport}
    return render(request, 'sports/event-detail.html', ctx)

def event_update(request, event_id):
    event = get_object_or_404(Sport, pk=event_id)
    if request.method == 'POST':
        name=request.POST.get('name')
        location=request.POST.get('location')
        date=request.POST.get('date')
        sport_type=request.POST.get('sport_type')
        if name and location and date and sport_type:
            event.name = name
            event.location = location
            event.date = date
            event.sport_type = sport_type
            event.save()
            return redirect(event.get_detail_url())
    ctx = {'event':event}
    return render(request, 'sports/event-create.html', ctx)

def event_delete(request, event_id):
    event = get_object_or_404(Sport, pk=event_id)
    event.delete()
    return redirect('sports:list')
