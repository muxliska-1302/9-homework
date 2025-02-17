from django.shortcuts import render, redirect,get_object_or_404
from .models import Destination


def travel_list(request):
    travel = Destination.objects.all()
    ctx = {'travel':travel}
    return render(request, 'travel/travel-list.html', ctx)

def create_destination(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        country=request.POST.get('country')
        description=request.POST.get('description')
        popular_season=request.POST.get('popular_season')
        if name and country and description and popular_season:
            Destination.objects.create(
                name = name,
                country = country,
                description = description,
                popular_season = popular_season
            )
            return redirect('travel:list')
    return render(request, 'travel/travel-form.html')

def travel_detail(request, travel_id):
    travel = get_object_or_404(Destination, pk=travel_id)
    ctx = {'travel':travel}
    return render(request, 'travel/travel-detail.html', ctx)

def travel_update(request, travel_id):
    travel = get_object_or_404(Destination, pk=travel_id)
    if request.method == 'POST':
        name=request.POST.get('name')
        country=request.POST.get('country')
        description=request.POST.get('description')
        popular_season=request.POST.get('popular_season')
        if name and country and description and popular_season:
            travel.name = name
            travel.country = country
            travel.description = description
            travel.popular_season = popular_season
            travel.save()
            return redirect(travel.get_detail_url())
    ctx = {'travel':travel}
    return render(request, 'travel/travel-form.html', ctx)

def travel_delete(request, travel_id):
    travel = get_object_or_404(Destination, pk=travel_id)
    travel.delete()
    return redirect('travel:list')