#!/usr/bin/python
# coding:utf8
# 发送文本文件到 paste.ubuntu.org.cn

"""
USAGE %s filename.png
        filename.png
            要上传的文件名
"""
import sys
import re
import os

import formdata

filename=None

while len(sys.argv)>=2:
    if os.path.isfile(sys.argv[1]):
        filename=sys.argv[1]
        print "the filename:", filename
        del sys.argv[1]
    else:
        print "error filename:", sys.argv[1]
        sys.exit(1)

if filename:
    fields = [('poster', 'yaoms'),('parent_pid', ''), ('paste', 'send'), ('class', 'bash'), ('code2', 'test')]
    files = [('screenshot', filename, open(filename, 'rb').read()),]
    rsp = formdata.post_multipart("paste.ubuntu.org.cn", "/", fields, files)
    print "http://paste.ubuntu.org.cn/%s" % formdata.find_group(r'''href=['"]/(i\d+)''', rsp)
else:
    print "on file"
