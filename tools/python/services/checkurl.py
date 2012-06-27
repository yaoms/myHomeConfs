#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: checkurl.py
# author:   yaoms
# date:     Thu Jun  7 15:50:01 HKT 2012
# describe: 检查apk下载链接是否可用，不可用的自动禁用

import urllib2

def useful(url):
    # 建立请求体，将请求方法设为 HEAD
    request = urllib2.Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        # 尝试打开请求，超时设为3秒
        response = urllib2.urlopen(request, timeout=3)
        print response.getcode(), response.msg
        print response.info()
        if response.getcode()==200:
            return (response.getcode(), response.headers['content-type'], response.headers['content-length'])
        else:
            return (response.getcode(), response.msg)
    except:
        pass
    return None
