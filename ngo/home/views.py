from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from directory.models import OrgDirectory


# Create your views here.
def index(request):
    """ See all plays available """
    orgs = OrgDirectory.objects.all()

    template = "home/index.html"
    context = {
        'orgs': orgs,
    }

    return render(request, template, context)
