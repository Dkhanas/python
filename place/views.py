from django.shortcuts import get_object_or_404, render_to_response
from place.models import Country, City


def place_list(request):
    places = City.objects.all()
    return render_to_response('place/place_list.html', {'places': places})


def place_detail(request, place_id):
    place_city = get_object_or_404(City.objects.all(), pk=place_id)
    return render_to_response('place/place_detail.html', {'city_detail':place_city})