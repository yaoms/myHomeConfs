#!/usr/bin/env python
from urllib2 import urlopen
from urllib import urlencode
import simplejson
import sys

# The google translate API can be found here:
# http://code.google.com/apis/ajaxlanguage/documentation/#Examples

target=sys.argv[1]

text=' '.join(sys.argv[2:])

# base_url='http://ajax.googleapis.com/ajax/services/language/translate?'
base_url='https://www.googleapis.com/language/translate/v2?'

params=urlencode( (('key','AIzaSyCTMQYOQUQdWSAJ478lI-peSVelazL_iCQ'), ('target',target), ('q',text), ) )

url=base_url+params

response=urlopen(url)

jsonObject = simplejson.load(response)

print "From: %s \"%s\"\n%s" % (jsonObject['data']['translations'][0]['detectedSourceLanguage'],text,jsonObject['data']['translations'][0]['translatedText'].encode('utf-8'))

