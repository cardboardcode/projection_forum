from urllib import quote_plus

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect

from comments.forms import CommentForm
from comments.models import Comment
from openedprojects.forms import PostForm
from openedprojects.models import Post, Category

# Create your views here.
def display_hidden(request,slug):
	instance = get_object_or_404(Post, slug=slug)
	share_string = quote_plus(instance.content)

	initial_data = {
		"content_type": instance.get_content_type,
		"object_id": instance.id
	}
	form = CommentForm(request.POST or None, initial = initial_data)
	if form.is_valid():
		c_type = form.cleaned_data.get("content_type")
		content_type = ContentType.objects.get(model = c_type)
		obj_id = form.cleaned_data.get("object_id")
		content_data = form.cleaned_data.get("content")
		parent_obj = None

		try:
			parent_id = int(request.POST.get("parent_id"))
		except:
			parent_id = None

		if parent_id:
			parent_qs = Comment.objects.filter(id = parent_id)
			if parent_qs.exists() and parent_qs.count() == 1:
				parent_obj = parent_qs.first()

		new_comment, created = Comment.objects.get_or_create(
			user = request.user,
			content_type = content_type,
			object_id = obj_id,
			content = content_data,
			parent = parent_obj,
			)
		return HttpResponseRedirect(new_comment.content_object.get_absolute_url())

	comments = instance.comments
	
	slugtest = slug

	context = {
	"slugtest": slugtest,
	"title": instance.title,
	"instance": instance,
	"share_string": share_string,
	"comments": comments,
	"comment_form": form
	}
	return render(request,'testing.html',context)
