#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import htmlParserPtags

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template, util

ROOT_PATH = os.path.dirname(__file__)
DEBUG = ROOT_PATH.find('/base') != 0

# さきほど取得した各情報をここで指定する
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
TWITTER_ACCESS_TOKEN = ''
TWITTER_ACCESS_TOKEN_SECRET =  ''
stringParser = htmlParserPtags.htmlParserGameFeed()


class TweetHandler(webapp.RequestHandler):
    def get(self):
        if stringParser != "nullnu":
            import oauth
            client = oauth.TwitterClient(TWITTER_CONSUMER_KEY,
                                     TWITTER_CONSUMER_SECRET, None)
            param = {'status': stringParser}
            client.make_request('https://api.twitter.com/1.1/statuses/update.json',
                            token=TWITTER_ACCESS_TOKEN,
                            secret=TWITTER_ACCESS_TOKEN_SECRET,
                            additional_params=param,
                            protected=True,
                            method='POST')
            self.response.out.write('')


def main():
    
    application = webapp.WSGIApplication([('/tasks/check', TweetHandler)], debug=DEBUG)
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()