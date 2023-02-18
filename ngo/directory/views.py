from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import OrgDirectory, Event
from .forms import EventForm


def events(request):
    """ See all plays available """
    events = Event.objects.all()
    form = EventForm()

    template = "directory/events.html"
    context = {
        'events': events,
        'form': form,
    }

    return render(request, template, context)