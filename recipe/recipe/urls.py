from django.conf.urls.defaults import *
import settings
from os.path import join
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
#import ox.django.api.urls
#from users.forms import SignupFormExtra 


urlpatterns = patterns('',
    # Example:
    # (r'^chaloBEST/', include('chaloBEST.foo.urls')),
#    url(r'^$','views.index', name='index'),

    url(r'^about/$', 'recipe.views.about'),
    url(r'^contact$', 'recipe.views.contact'),
     (r'^home/$', 'recipe.views.home'),	
     (r'^addrecipe/$','chef.views.recipe_posted'),
     (r'^showdata/$','recipe.views.showdata'), 
     (r'^searchdata/$','recipe.views.searchdata'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^grappelli/', include('grappelli.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
# url(r'^accounts/', include('userena.urls')),
# url(r'^accounts/signup/$', 
#		'userena.views.signup',
#      		{'signup_form': SignupFormExtra}),
     url(r'^accounts/', include('userena.urls')),
 
     url(r'^messages/',include('userena.contrib.umessages.urls')),

    
)

if settings.LOCAL_DEVELOPMENT:
#
  urlpatterns += patterns('',
#
  (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': join(settings.PROJECT_ROOT, "allstatic/static")}),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': join(settings.PROJECT_ROOT, "media")}),
#
)

