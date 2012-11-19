import os
from time import sleep
from random import random
from clint.textui import progress, puts, indent, colored
import twitter

TIME_INTERVAL_IN_SECONDS = 30 

def getTrends():
    twitter_api=twitter.Twitter(domain="api.twitter.com", api_version='1')
    WORLD_WOE_ID = 1
    world_trends = twitter_api.trends._(WORLD_WOE_ID)
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
        print "\nTrending topis:\n"
    
        new_trends = getTrends()
        for trend in new_trends:
            trend_name = trend['name']
            if isTrendNew(trend_name, old_trends):
            #if trend_name == 'Tyga':
                with indent(8, quote=colored.red(' |')):
                    puts(trend['name'] + colored.red('  NEW'))
            else:
                with indent(8, quote=colored.cyan(' |')):
                    puts(trend['name'])
        old_trends = new_trends
        
        print "\n\nRefreshing in:"
        for i in progress.bar(range(TIME_INTERVAL_IN_SECONDS)):
            sleep(1)
        os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )


main()
