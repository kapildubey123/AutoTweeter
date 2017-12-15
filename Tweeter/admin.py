from django.contrib import admin

# Register your models here.
from .models import Conferences
from .models import TemplateTweets

admin.site.register(Conferences)
admin.site.register(TemplateTweets)