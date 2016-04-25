import datetime
from twitterlistener import retrieve_data
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import User
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.base import View

# Create your views here.

def home(request):
    users = User.objects.all()
    return render(request, 'miner/home.html', {'users':users })

def stream(request):
    retrieve_data()
    return render(request, 'miner/stream.html')

def index(request):
    return render(request, 'miner/index.html')

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('home')

"""def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        #form = PostForm(request.POST, instance=post)
        #if form.is_valid():
            #post = form.save(commit=False)
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            #return redirect('post_list')
    #else:
        #form = PostForm(instance=post)
    #return render(request, 'blog/post_edit.html', {'form': form})"""
