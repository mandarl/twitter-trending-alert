import sys
import os
from time import sleep
from random import random
from clint.textui import progress, puts, indent, colored
import twitter

TIME_INTERVAL_IN_SECONDS = 30
#WOEIDS at http://engineering.twitter.com/2010/02/woeids-in-twitters-trends.html
WORLD_WOE_ID = 1
US_WOE_ID = 23424977
WOE_ID = US_WOE_ID
 

def getTrends():
    twitter_api=twitter.Twitter(domain="api.twitter.com", api_version='1')
    world_trends = twitter_api.trends._(WOE_ID)
    trends = [ trend for trend in world_trends()[0]['trends'] ]
    return trends

def isTrendNew(trend_name, old_trends):
    ret = True
    for trend in old_trends:
        if trend['name'] == trend_name:
            ret = False
    return ret


def main():
    old_trends = {}
    while 1==1:
        isNew = False
        try:
            print "\nTrending topics:\n"
        
            new_trends = getTrends()
            for trend in new_trends:
                trend_name = trend['name']
                if isTrendNew(trend_name, old_trends):
                #if trend_name == 'Tyga':
                    isNew = True
                    sys.stdout.write("\t" + trend['name'])
                    puts(colored.red('  NEW'))
                else:
                    print "\t" + trend['name']
            if isNew:
                print "\a\a\a"
            old_trends = new_trends
            
            print "\n\nRefreshing in:"
            for i in progress.bar(range(TIME_INTERVAL_IN_SECONDS)):
                sleep(1)
        finally:
            os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )


main()
