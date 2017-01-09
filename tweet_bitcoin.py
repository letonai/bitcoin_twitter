#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import csv
import datetime
import time
import twitter
import urllib2
import json
from HTMLParser import HTMLParser
from StringIO import StringIO
reload(sys)
sys.setdefaultencoding('utf8')
#https://api.blinktrade.com/api/v1/BRL/ticker
class Cotacao():

        def getCurrencyInfo(self):
                try:

                        request = urllib2.Request("https://api.blinktrade.com/api/v1/BRL/ticker")
                        request.add_header('Accept-enconding', 'gzip')
                        response = urllib2.urlopen(request)
                        data=""
                        if response.info().get('Content-Encoding') == 'gzip':
                                buf = StringIO(response.read())
                                f = gzip.GzipFile(fileobj=buf)
                                data = f.read()
                        else:
                                data = response.read()
                        j=json.loads(data)

                        return j    
                except Exception as e:
                        print e


        def getCurrencyValue(self,currency):
                j=self.getCurrencyInfo(currency)
                return j




def test():

        #connect to twitter
        TOKEN="" 
        TOKEN_KEY="" 
        CON_SEC=""
        CON_SEC_KEY="" 
        
        cotacao=Cotacao() 
        my_auth = twitter.OAuth(TOKEN,TOKEN_KEY,CON_SEC,CON_SEC_KEY)
        twit = twitter.Twitter(auth=my_auth)

        #try to tweet if speedtest couldnt even connet. Probably wont work if the internet is down
        btc=cotacao.getCurrencyInfo()
	  
        tweet="#Bitcoin\nUltima: R$ %.2f Alta: R$ %.2f Baixa: R$ %.2f\nFonte: Foxbit" % (btc['last'],btc['high'],btc['low'])
        print tweet
        twit.statuses.update(status=tweet)
        return
        
if __name__ == '__main__':
        test()
        print 'completed'

