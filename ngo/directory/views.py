from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import OrgDirectory, Event, Location


def events(request):
    """ See all plays available """
    events = Event.objects.all()
    locations = Location.objects.all()

    template = "directory/events.html"
    context = {
        'events': events,
        'locations': locations,
    }

    return render(request, template, context)


def donate(request):
    """ Return homepage """
    orgs = OrgDirectory.objects.all()

    template = "directory/donate.html"
    context = {
        'orgs': orgs,
    }

    return render(request, template, context)
