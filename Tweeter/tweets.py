import calendar
from datetime import datetime, timedelta
from random import shuffle


class Date:

    CALENDAR_DICT = {v:k for k, v in enumerate(calendar.month_abbr)}

    @staticmethod
    def parse_input(datestr):
        """Accept a STR object, return a STR object!"""
        month = datestr.split('-')[1]
        return datestr.replace(month, str(Date.CALENDAR_DICT[month]))

    @staticmethod
    def dmy_to_date(date):
        """Accept a STR object, return a DATETIME object!"""
        return datetime.strptime(date, '%Y-%m-%d')
    @staticmethod
    def dates2ndays(mindatestr, maxdatestr):
        mindate = Date.dmy_to_date(mindatestr)
        maxdate = Date.dmy_to_date(maxdatestr)
        return (maxdate - mindate).days + 1

class Tweet:

    TIMES       = ['11:30', '17:00']
    MAX_LENGTH  = 116

    def __init__(self, date, daytime, template, hashtag, maxdate, url='http://www.newdelhirestaurant.com'):
        self.date     = date
        self.daytime  = daytime
        self.template = template
        self.hashtag  = hashtag
        self.maxdate  = maxdate
        self.url      = url
        self.tweet, self.msg = self.generate_tweet()

    def generate_tweet(self):
        msg = self.template
        msg = msg.replace('#', self.hashtag)
        msg = msg.replace('MONTH/DAY', self.maxdate)
        tweet = self.date + ' ' + self.daytime + ',' + msg + ',' + self.url
        return tweet, msg

    def __repr__(self):
        return self.tweet

class AutoTweets:

    def __init__(self, conferences, templates):
        self.conferences  = conferences
        self.templates    = templates
        
    def generate_conferences(self):
        all_tweets = []
        for conference in self.conferences:
            mindate, maxdate, hashtag = conference
            ndays = Date.dates2ndays(mindate, maxdate)
            all_tweets.append('')
            all_tweets.append("%d %s %s %s" % (ndays, mindate, maxdate, hashtag))
            #print('\n', ndays, mindate, maxdate, hashtag)

            mindate = Date.dmy_to_date(mindate)
            maxdate = Date.dmy_to_date(maxdate)
            dates = [mindate + timedelta(days=i) for i in range(ndays)]
            maxdate = str(maxdate.month) + '/' + str(maxdate.day)

            exit = False
            while(not exit):
                exit, tweets = self.generate_tweets(dates, hashtag, maxdate)
            all_tweets = all_tweets + tweets
        return all_tweets

    def generate_tweets(self, dates, hashtag, maxdate):
        max_tweet_length = 0
        tweets = []
        shuffle(self.templates)
        idx_template = 0

        for date in dates:
            date = date.strftime('%m/%d/%Y')

            for daytime in Tweet.TIMES:
                tweet = Tweet(date=date, daytime=daytime, template=self.templates[idx_template], hashtag=hashtag, maxdate=maxdate)

                max_tweet_length = max(len(tweet.msg), max_tweet_length)
                # print('{:3}/{:3}'.format(len(tweet.msg), max_tweet_length))
                if max_tweet_length > Tweet.MAX_LENGTH:  return False, None

                tweets.append(tweet.tweet)
                idx_template += 1

        return True, tweets
