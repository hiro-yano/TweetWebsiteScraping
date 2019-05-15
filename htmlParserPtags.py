#!/usr/bin/env python
# !-*- coding: utf-8 -*-

from BeautifulSoup import BeautifulSoup,NavigableString
import urllib2,sys
import random
#from google.appengine.api import urlfetch

from google.appengine.ext import db
class NModel(db.Model):
    content = db.StringProperty()

def htmlParserGameFeed():

    url = 'http://www.mizukinana.jp/blog/index.html'
    url=url+'?'+ str(random.random())
    
    atag = ""
    nm = NModel()
    nm2 = nm.get_by_id(1002, parent=None)
    
    try:
        html = urllib2.urlopen(url).read()
        html = html.lstrip(None)
        html = html.strip()
        html = html.replace('\r\n','')
        html = html.replace('\n','')
        html = html.replace('\r','')
        html = html.replace('\t','')

        soup = BeautifulSoup(html)
        txt_comment_tags = soup.findAll('h3')
        txt_detail_tags = soup.findAll('div', attrs={'class':'message'})
    except urllib2.URLError, e:
        handleError(e)

    TagString = []
    def printText(tags):
        for tag in tags:
            if tag.__class__ == NavigableString:
                TagString.append(tag)
            else:
                printText(tag)

    printText(txt_comment_tags[1])
    s = ''.join(TagString)

    TagString = []
    printText(txt_detail_tags[0])
    m = ''.join(TagString)

    BlogLength=81-len(s)
    m = m[0:BlogLength]

    atag = u"【NANABLOG更新】「%s」:%s... http://www.mizukinana.jp/blog/index.html" % (s,m)


    if atag == nm2.content:
        atag = "nullnu"
    else:
        nm2.content = atag
        nm2.put()

    return atag.encode('utf-8')