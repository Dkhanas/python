from django.conf.urls import url
from place import views

urlpatterns = [
    url(r'^$', views.place_list, name='place_list'),
    url(r'^(?P<place_id>\d+)$', views.place_detail, name='place_detail'),

]
