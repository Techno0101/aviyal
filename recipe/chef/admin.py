from django.contrib import admin
from chef.models import RecipePoster


class RecipeAdmin(admin.ModelAdmin):
	fields =['created_date', 'dish_name', 'dish_desc', 'course_type', 'cusine_type', 'dish_ingre', 'dish_method','photo']
admin.site.register(RecipePoster, RecipeAdmin)
