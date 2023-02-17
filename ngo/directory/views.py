from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import OrgDirectory, Events


def organisations(request):
    """ See all plays available """
    orgs = OrgDirectory.objects.all()

    template = "orgs.html"
    context = {
        'orgs': orgs,
    }

    return render(request, template, context)


def Events(request):
    """ See all plays available """
    events = Events.objects.all()

    template = "directory/events.html"
    context = {
        'events': events,
    }

    return render(request, template, context)