#!/usr/bin/env python
from urllib2 import urlopen
from urllib import urlencode
#import simplejson
import re
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

def ipinfo(host):
    base_url='http://ip138.com/ips1388.asp?'
    
    params=urlencode( (('ip',host), ('action','s'), ) )
    
    url=base_url+params
    
    response=urlopen(url)
    
    #print response.read().decode('gb2312')
    lines = response.readlines()
    for line in lines:
        if line.count('class="ul1"'):
            line = line.decode('gb2312')
            line = line.replace('li><li', 'li>\n<li')
            sublines = line.split('\n')
            return [re.sub('<[^>]+>', '', subline).strip() for subline in sublines if len(subline.strip())]

if __name__ == '__main__':
    host=sys.argv[1]
    print "\n".join(ipinfo(host))
