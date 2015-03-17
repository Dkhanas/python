from django.shortcuts import get_object_or_404, render_to_response
from shops.models import Shop


def shops_list(request):
    shops = Shop.objects.all()
    return render_to_response('shops/shops_list.html', {'shops': shops})


def shops_detail(request, shops_id):
    shops = get_object_or_404(Shop.objects.all(), pk=shops_id)
    return render_to_response('shops/shops_detail.html', {'shops_detail':shops})