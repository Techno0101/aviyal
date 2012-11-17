from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from chef.models import RecipePoster

class RecipeForm(forms.ModelForm):
	class Meta
		model = RecipePoster
		
	#def save(self):
	#	new_user= super(SignupFormExtra, self).save()
	#	user_profile = new_user.get_profile()
		#user_profile.first_name = self.cleaned_data['first_name']
		#user_profile.last_name = self.cleaned_data['last_name']
	#	user_profile.mobile_number = self.cleaned_data['mobile_number']
		#user_profile.mobile_number = UserProfile.objects.get_or_create(name=user_profile.mobile_number)

	#	user_profile.save()
	#	return new_user	
	def save(self):
		if request.method == 'POST':
			form = RecipeForm(request.POST)
			if form.is_valid():
				dn, dd, co_t, cu_t, di, dm, p, c = RecipePoster.objects.get_create(**form.cleaned_data)
			form.save()
			return form
		
		
