#!/usr/bin/python
from django.contrib.gis.utils import GeoIP

def getLocation(self):

	g = GeoIP()
	ip = request.META.get('REMOTE_ADDR',None)
	if ip:
		city = g.city(ip)['city']
		return city
	
	else :
		print "nothing"
	
