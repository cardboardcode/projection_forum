from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, get_object_or_404

from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
	form = PostForm()
	context = {
		"form":form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, id):
	# instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, id=id)
	context = {
	"title": instance.title,
	"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset = Post.objects.all()
	context ={
		"object_list": queryset,
		"title":"List"
	}
	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My User List"
	# 	}
	# else:
	# context = {
	# 	"title": "List"
	# }
	return render(request, "index.html", context)
	# return HttpResponse("<h1>List</h1>")

def post_update(request):
	return HttpResponse("<h1>Update</h1>")

def post_delete(request):
	return HttpResponse("<h1>Delete</h1>")

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