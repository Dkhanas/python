from django.conf.urls import url
from shops import views

urlpatterns = [
    url(r'^$', views.shops_list, name='shops_list'),
    url(r'^(?P<shops_id>\d+)$', views.shops_detail, name='shops_detail'),

]