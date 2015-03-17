from django.shortcuts import get_object_or_404, render_to_response
from store.models import Store


def store_list(request):
    stores = Store.objects.all()
    return render_to_response('store/store_list.html', {'stores': stores})


def store_detail(request, store_id):
    store = get_object_or_404(Store.objects.all(), pk=store_id)
    return render_to_response('store/store_detail.html', {'store_detail':store})