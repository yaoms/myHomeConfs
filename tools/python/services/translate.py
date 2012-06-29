#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import json
except ImportError:
    import simplejson as json
import time
import urllib
import urllib2
import logging
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

__version__ = '0.9'
__author__ = 'Yao Mingshun (yms541@gmail.com)'

'''
Python client SDK for the youdao translation API
'''

def _obj_hook(pairs):
    '''
    convert json object to python object.
    '''
    o = JsonObject()
    for k, v in pairs.iteritems():
        o[str(k)] = v
    return o

class APIError(StandardError):
    '''
    raise APIError if got failed json message.
    '''
    def __init__(self, error_code, error, request):
        self.error_code = error_code
        self.error = error
        self.request = request
        StandardError.__init__(self, error)

    def __str__(self):
        return 'APIError: %s: %s, request: %s' % (self.error_code, self.error, self.request)

class JsonObject(dict):
    '''
    general json object that can bind any fields but also act as a dict.
    '''
    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

def _encode_params(**kw):
    '''
    Encode parameters.
    '''
    args = []
    for k, v in kw.iteritems():
        qv = v.encode('utf-8') if isinstance(v, unicode) else str(v)
        args.append('%s=%s' % (k, urllib.quote(qv)))
    return '&'.join(args)

def _encode_multipart(**kw):
    '''
    Build a multipart/form-data body with generated random boundary.
    '''
    boundary = '----------%s' % hex(int(time.time() * 1000))
    data = []
    for k, v in kw.iteritems():
        data.append('--%s' % boundary)
        if hasattr(v, 'read'):
            # file-like object:
            ext = ''
            filename = getattr(v, 'name', '')
            n = filename.rfind('.')
            if n != (-1):
                ext = filename[n:].lower()
            content = v.read()
            data.append('Content-Disposition: form-data; name="%s"; filename="hidden"' % k)
            data.append('Content-Length: %d' % len(content))
            data.append('Content-Type: %s\r\n' % _guess_content_type(ext))
            data.append(content)
        else:
            data.append('Content-Disposition: form-data; name="%s"\r\n' % k)
            data.append(v.encode('utf-8') if isinstance(v, unicode) else v)
    data.append('--%s--\r\n' % boundary)
    return '\r\n'.join(data), boundary

_CONTENT_TYPES = { '.png': 'image/png', '.gif': 'image/gif', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.jpe': 'image/jpeg' }

def _guess_content_type(ext):
    return _CONTENT_TYPES.get(ext, 'application/octet-stream')

_HTTP_GET = 0
_HTTP_POST = 1
_HTTP_UPLOAD = 2

def _http_get(url, headers=None, **kw):
    logging.info('GET %s' % url)
    return _http_call(url, _HTTP_GET, headers, **kw)

def _http_post(url, headers=None, **kw):
    logging.info('POST %s' % url)
    return _http_call(url, _HTTP_POST, headers, **kw)

def _http_upload(url, headers=None, **kw):
    logging.info('MULTIPART POST %s' % url)
    return _http_call(url, _HTTP_UPLOAD, headers, **kw)

def _http_call(url, method, headers=None, **kw):
    '''
    send an http request and expect to return a json object if no error.
    '''
    params = None
    boundary = None
    if method==_HTTP_UPLOAD:
        params, boundary = _encode_multipart(**kw)
    else:
        params = _encode_params(**kw)
    http_url = '%s?%s' % (url, params) if method==_HTTP_GET else url
    http_body = None if method==_HTTP_GET else params
    req = urllib2.Request(http_url, data=http_body)
    if headers:
        [req.add_header(key, value) for key, value in headers]
    if boundary:
        req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
    resp = urllib2.urlopen(req)
    body = resp.read()
    return body

class HttpObject(object):

    def __init__(self, client, method):
        self.client = client
        self.method = method

    def __getattr__(self, attr):
        def wrap(**kw):
            return _http_call('%s%s.json' % (self.client.url, attr.replace('__', '/')), self.method, **kw)
        return wrap
        #return lambda x: 

class APIClient(object):
    '''
    API client using synchronized invocation.
    '''
    #('keyfrom','yaoms-trans-bot'), ('key', '780445278'), ('type', 'data'), ('doctype', 'xml'), ('version', '1.1')
    def __init__(self, keyfrom, key, type='data', doctype="json", version="1.1", url='http://fanyi.youdao.com/openapi.do'):
        self.keyfrom = keyfrom
        self.key = key
        self.type = type
        self.doctype = doctype
        self.version = version
        self.url = url
        self.get = HttpObject(self, _HTTP_GET)
        self.post = HttpObject(self, _HTTP_POST)
        self.upload = HttpObject(self, _HTTP_UPLOAD)

    def trans(self, words):
        self.words = words
        body = _http_get(self.url, keyfrom=self.keyfrom, key=self.key, type=self.type, doctype=self.doctype, version=self.version, q=words)
        #print body
        res = json.loads(body, object_hook=_obj_hook)
        if hasattr(res, 'error_code'):
            raise APIError(res.error_code, getattr(res, 'error', ''), getattr(res, 'request', ''))
        output = []
        if hasattr(res, 'errorCode') and res.errorCode:
            output.append("ErrorCode: %s, Error: %s" % (res.errorCode, error[res.errorCode]))
        if hasattr(res, 'basic') and res.basic:
            output.append("%s%s" % (res.basic.has_key('phonetic') and "[%s]\n" % res.basic['phonetic'] or '', "\n".join(res.basic['explains'])))
        elif hasattr(res, 'translation') and res.translation:
            output.append("\n".join(res.translation))
        elif hasattr(res, 'web') and res.web:
            output.append("\n".join([ "%s:\n%s" % (i.key, ", ".join(i.value)) for i in res.web]))
        return "\n".join(output)

    def __getattr__(self, attr):
        return getattr(self.get, attr)

error = {"0":"正常", "20":"要翻译的文本过长", "30":"无法进行有效的翻译", "40":"不支持的语言类型", "50":"无效的key"}

if __name__ == '__main__':
    words=' '.join(sys.argv[1:])
    ydapi = APIClient(keyfrom='yaoms-trans-bot', key='780445278')
    print ydapi.trans(words) 


# 您的key：780445278 
# 您的keyfrom：yaoms-trans-bot
