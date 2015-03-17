from django.shortcuts import get_object_or_404, render_to_response
from contact.models import Contact


def contact_list(request):
    contacts = Contact.objects.all()
    return render_to_response('contact/contact_list.html', {'contacts': contacts})


def contact_detail(request, contact_id):
    contactinf = get_object_or_404(Contact.objects.all(), pk=contact_id)
    return render_to_response('contact/contact_detail.html', {'detail': contactinf, 'sex': contactinf.get_sex_display})