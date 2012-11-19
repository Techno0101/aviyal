DEBUG = True
LOCAL_DEVELOPMENT = True
JSON_DEBUG = False

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
	'ENGINE':'django.contrib.gis.db.backends.postgis',
        'NAME': 'recipedb',
        'USER': 'cook',                          
        'PASSWORD': '123456',                                       
        'HOST': '',  
        'PORT': '',  
        }

    
}
EMAIL_HOST_USER = 'thechiefcook@zoho.com'
EMAIL_HOST_PASSWORD ='dgp123@123'


