from django.db import models

# Create your models here.
class Conferences(models.Model):
    start = models.DateTimeField('Start Date')
    end = models.DateTimeField('End Date')
    hashtag = models.CharField(max_length=100)

    def getData(self):
        return [ str(self.start.date()), str(self.end.date()), self.hashtag ]

class TemplateTweets(models.Model):
    msg = models.CharField(max_length=200)

    def getData(self):
            return self.msg