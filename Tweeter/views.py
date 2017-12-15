# Create your views here.
from django.http import HttpResponse
from Tweeter.tweets import AutoTweets
from .models import Conferences
from .models import TemplateTweets

def index(request):
    return HttpResponse("Hello world. You are at my first webapp")

def justRun(request):
    all_conf = [ item.getData() for item in Conferences.objects.order_by('start') ]
    all_msg = [ item.getData() for item in TemplateTweets.objects.order_by('msg')]
    autoTweets = AutoTweets(all_conf,all_msg)
    tweets = autoTweets.generate_conferences()
    return HttpResponse("<br>".join(tweets))