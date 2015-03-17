from django.conf.urls import url
from store import views

urlpatterns = [
    url(r'^$', views.store_list, name='store_list'),
    url(r'^(?P<store_id>\d+)$', views.store_detail, name='store_detail'),

]