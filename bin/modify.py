#!/usr/bin/python
# coding:utf8

import os
import re
import shutil

marker='name="proid"'
partten=r'<string name="proid">\d+</string>'
repl='<string name="proid">%d</string>'
filename='/tmp/sd.xml'
pidlist="/tmp/proidlist.properties"

def batch(proidlist, cmd):
    for id in [x for x in open('proidlist', 'r') if not x.startswith('#') and len(x.strip())]:
        cmd(filename, id)

def modify(filename, proid):
    if check_file(filename):
        replace_project_id(filename, marker, partten, repl % proid)

def check_file(filename):
    return filename and os.path.exists(filename) and os.path.isfile(filename)


def replace_project_id(filename, marker, partten, repl):
    shutil.copyfile(filename, "%s.bak" % filename)
    filehandler = open("%s.bak" % filename, 'r')
    filehandler2= open(filename, 'w')
    for line in filehandler:
        if line.count(marker): line=re.sub(partten, repl, line) # modify
        filehandler2.write(line)
    filehandler2.close()
    filehandler.close()
    os.remove("%s.bak" % filename)

if __name__ == '__main__':
    print ""   
