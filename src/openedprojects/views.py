from django.conf import settings
from django.shortcuts import render

# Create your views here.
def openedgenres (request):
	context={
	"queryset": "Test Message.."
	}
	return render (request, 'genres2.html', context)

def opened_subcategories (request):
	context={
	"queryset": "Test Message.."
	}
	return render (request, 'opened_subcategory.html', context)