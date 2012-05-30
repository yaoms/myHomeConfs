#!/usr/bin/python
# coding:utf8
# 发送文本文件到 paste.ubuntu.org.cn

"""
USAGE %s -c bash filename.sh
        -c filetype
        --class=filetype
            指定文件类型，支持的文件类型有：
            actionscript actionscript-french ada apache applescript asm asp autoit bash blitzbasic
            c c_mac caddcl cadlisp cfdg cpp csharp css d delphi diff div dos eiffel fortran freebasic
            gml html4strict inno java java5 javascript lisp lua matlab mpasm mysql nsis objc ocaml
            ocaml-brief oobas oracle8 pascal perl php php-brief python qbasic robots ruby sas scheme
            sdlbasic smarty sql tsql vb vbnet vhdl visualfoxpro xml

        filename.sh
            要上传的文件名
"""
import sys
import re
import os
import formdata

filetypes = [
        "actionscript",
        "actionscript-french",
        "ada",
        "apache",
        "applescript",
        "asm",
        "asp",
        "autoit",
        "bash",
        "blitzbasic",
        "c",
        "c_mac",
        "caddcl",
        "cadlisp",
        "cfdg",
        "cpp",
        "csharp",
        "css",
        "d",
        "delphi",
        "diff",
        "div",
        "dos",
        "eiffel",
        "fortran",
        "freebasic",
        "gml",
        "html4strict",
        "inno",
        "java",
        "java5",
        "javascript",
        "lisp",
        "lua",
        "matlab",
        "mpasm",
        "mysql",
        "nsis",
        "objc",
        "ocaml",
        "ocaml-brief",
        "oobas",
        "oracle8",
        "pascal",
        "perl",
        "php",
        "php-brief",
        "python",
        "qbasic",
        "robots",
        "ruby",
        "sas",
        "scheme",
        "sdlbasic",
        "smarty",
        "sql",
        "tsql",
        "vb",
        "vbnet",
        "vhdl",
        "visualfoxpro",
        "xml"
        ]

filetype='bash'
filename=None
filecontent=None

while len(sys.argv)>=2:
    if sys.argv[1]=='-c':
        if len(sys.argv)>=3:
            if sys.argv[2] in filetypes:
                filetype=sys.argv[2]
                print "the filetype:", filetype
                del sys.argv[1]
                del sys.argv[1]
            else:
                print "error filetype", sys.argv[2]
                sys.exit(1)
        else:
            print "no filetype specified"
            sys.exit(1)
    elif sys.argv[1].startswith('--class='):
        filetype=sys.argv[1][8:]
        if not filetype:
            print "no filetype specified"
            sys.exit(1)
        elif filetype not in filetypes:
            print "error filetype:", filetype
            sys.exit(1)
        else:
            print "the filetype:", filetype
            del sys.argv[1]
    else:
        if os.path.isfile(sys.argv[1]):
            filename=sys.argv[1]
            print "the filename:", filename
            del sys.argv[1]
        else:
            print "error filename:", sys.argv[1]
            sys.exit(1)

if filetype=='bash':
    print "use default filetype:", filetype

if filename==None:
    print "use stdin as file input."
    filecontent = sys.stdin.read()
else:
    filecontent = open(filename, 'r').read()


fields = [('poster', 'yaoms'),('parent_pid', ''), ('paste', 'send'), ('class', filetype), ('code2', filecontent)]
files = []
rsp = formdata.post_multipart("paste.ubuntu.org.cn", "/", fields, files)
print "http://paste.ubuntu.org.cn/%s" % formdata.find_group(r'''href=['"]/d(\d+)''', rsp)
