from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import OrgDirectory, Event


def events(request):
    """ See all plays available """
    events = Event.objects.all()

    template = "directory/events.html"
    context = {
        'events': events,
    }

    return render(request, template, context)