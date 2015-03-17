from django.conf.urls import url
from contact import views

urlpatterns = [
    url(r'^$', views.contact_list, name='contact_list'),
    url(r'^(?P<contact_id>\d+)$', views.contact_detail, name='contact_detail'),

]
