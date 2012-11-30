# Create your views here.
#from models import *
from django.shortcuts import render_to_response, get_object_or_404
from ox.django.shortcuts import get_object_or_404_json, render_to_json_response

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from fuzzywuzzy import process as fuzzprocess
from django.http import HttpResponse
from django import forms
from chef.forms import RecipeForm
@login_required
def recipe_posted(request):
    if request.user.is_authenticated():	
	if request.method == 'POST':
	    recipe = RecipeForm(request.POST)
	    if recipe.is_valid():
	        new_recipe = recipe.save()
	        #new_recipe.save()
                return HttpResponseRedirect('.')
	    else:
	        recipe = RecipeForm()
			
	return render_to_response('addrecipe.html',
				{'RecipeForm':recipe},
				 context_instance=RequestContext(request))
	
