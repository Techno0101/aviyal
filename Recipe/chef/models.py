from django.db import models
# This is main model for Recipe.
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
import datetime

class RecipePoster(models.Model):
	COURSE_CHOICES =(
                (1, _('Appetizer and Starter')),
                (2, _('Baking')),
		(3, _('Breakfast')),
		(4, _('Brunch')),
		(5, _('Deserts and Sweets')),
		(6, _('Drinks')),
		(7, _('Other')),
		(8, _('Sauces')),
		(9, _('Side Dish')),
		(10,_('Snacks')),
		(11,_('Soups')),
        )
	CUISINE_CHOICES=(
                (1, _('North Indian')),
                (2, _('South Indian')),
		(3, _('East Indian')),
		(4, _('West Indian')),
		(5, _('Fusion')),
		(6, _('Non Indian')),
	)
	dish_name = models.CharField(_('Dish Name'),max_length=300)
	dish_desc = models.CharField(_('Dish Description'),max_length=300)

	course_type=  models.PositiveSmallIntegerField(_('Course Type'),
                                                 choices=COURSE_CHOICES,
                                                 blank = True,
                                                 null=True)
	cusine_type = models.PositiveSmallIntegerField(_('Cuisine Type'),
						 choices=CUISINE_CHOICES,
						 blank = True,
						 null=True)
	dish_ingre = models.TextField()
	dish_method = models.TextField()
	photo = models.ImageField(upload_to = 'Photos/', null=True, blank=True)
	created_date = models.DateTimeField()

	def __unicode__(self):
		return u"%s, %s, %s %s, %s, %s, %s" %(self.dish_name, self.dish_desc, self.course_type, self.cusine_type, self.dish_ingre, self.dish_method,self.created_date)
