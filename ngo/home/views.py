from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from directory.models import Org


# Create your views here.
def index(request):
    """ See home page """

    template = "home/index.html"

    return render(request, template)
