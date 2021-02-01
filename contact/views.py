from django.shortcuts import render

# Create your views here.
from django.template import RequestContext

from contact.forms import ContactUsForm
from mail_list.forms import SubscribeForm


def render_landing_page(request, template="index.html"):
    return render(request, template, context={})


def render_error_page(request, template="error.html"):
    return render(request, template, context={})


def render_success_page(request, template="success.html"):
    return render(request, template, context={})


def contact_us(request):
    form = ContactUsForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "success.html", context={})
    else:
        return render(request, "error.html", context={})


def subscribe(request):
    form = SubscribeForm(request.POST)
    if form.is_valid():
        form.save()
        return render(request, "success.html", context={})
    else:
        return render(request, "error.html", context={})
