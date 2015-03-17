from __future__ import absolute_import
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.apps import apps
from contact.models import Contact


def models_name(request):
    modeget = list(apps.all_models)[6:]
    return render_to_response('main.html', {'modeget': modeget})


def models_view(request, slug):
    return render_to_response('main.html', {slug} )