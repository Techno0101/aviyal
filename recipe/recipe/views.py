# Create your views here.
#from models import *
from django.shortcuts import render_to_response, get_object_or_404
from ox.django.shortcuts import get_object_or_404_json, render_to_json_response

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from fuzzywuzzy import process as fuzzprocess
from django.http import HttpResponse


def home(request):
    context = RequestContext(request, {})
    return render_to_response("index.html", context)
    

def about(request):
    context = RequestContext(request, {})
    return render_to_response("innov/about_chalobest.html", context)


def join_us(request):
    context = RequestContext(request, {})
    return render_to_response("innov/joinus.html", context)


def contact(request):
    context = RequestContext(request, {})
    return render_to_response("innov/contactus.html", context)

