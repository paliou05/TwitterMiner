import datetime
from twitterlistener import retrieve_data
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import User,Tweet
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def home(request):
    tweets = Tweet.objects.all()
    paginator = Paginator(tweets,15)
    page = request.GET.get('page')
    try:
        tweets = paginator.page(page)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)
    return render(request, 'miner/home.html', {'tweets': tweets })

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

def get_top_users(request):
    users = User.objects.order_by('-trust')[:10]
    return render(request, 'miner/get_top_users.html', {'users': users })

