from django.conf.urls import include, url, handler404
from django.contrib import admin
from homework5 import views

urlpatterns = [
    url(r'^$', views.models_name, name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/', include('contact.urls'), name='contact'),
    url(r'^place/', include('place.urls'), name='place'),
    url(r'^store/', include('store.urls'), name='store'),
    url(r'^shops/', include('shops.urls'), name='shops'),
    url(r'^(?P<slug>[\w\-]+)/', views.models_view, name='models'),

]
