from django.conf.urls import url, include, patterns
from django.contrib import admin
from views import display_hidden


urlpatterns = [
	url(r'^$', display_hidden, name = 'display_hidden'),
]