from urllib import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post

# Create your views here.
def post_create(request):
	if not request.user.is_authenticated():
		raise Http404

	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.user = request.user
		instance.save()
		#message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	
	context = {
		"form":form,
	}
	return render(request, "post_form.html", context)

def post_detail(request, slug=None):
	# instance = Post.objects.get(id=1)
	instance = get_object_or_404(Post, slug=slug)
	share_string = quote_plus(instance.content)
	context = {
	"title": instance.title,
	"instance": instance,
	"share_string": share_string,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all()#.order_by("-timestamp")
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
			Q(title__icontains=query) |
			Q(content__icontains=query) |
			Q(user__username__icontains=query)
			).distinct()
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context ={
		"object_list": queryset,
		"title":"List",
		"page_request_var": page_request_var
	}
	return render(request, "post_list.html", context)


def post_update(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		instance = form.save(commit = False)
		instance.save()
		#message success
		messages.success(request, "Item Saved")
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)


def post_delete(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully Deleted")
	return redirect("posts:list")

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