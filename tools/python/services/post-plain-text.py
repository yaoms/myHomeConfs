#!/usr/bin/python
# coding:utf8
# 发送文本文件到 paste.ubuntu.org.cn

import sys, os, optparse 
import formdata

# 配置脚本版本，用法说明，命令行选项等信息
version="%prog 1.0"
usage="usage: %prog [options] [FILENAME]\n\n\t-- read from stdin if FILENAME is not provited."
filetypes = [
        "actionscript", "actionscript-french", "ada", "apache", "applescript", "asm", "asp", "autoit", "bash",
        "blitzbasic", "c", "c_mac", "caddcl", "cadlisp", "cfdg", "cpp", "csharp", "css", "d", "delphi", "diff",
        "div", "dos", "eiffel", "fortran", "freebasic", "gml", "html4strict", "inno", "java", "java5", "javascript",
        "lisp", "lua", "matlab", "mpasm", "mysql", "nsis", "objc", "ocaml", "ocaml-brief", "oobas", "oracle8",
        "pascal", "perl", "php", "php-brief", "python", "qbasic", "robots", "ruby", "sas", "scheme", "sdlbasic",
        "smarty", "sql", "tsql", "vb", "vbnet", "vhdl", "visualfoxpro", "xml"
        ]

parser = optparse.OptionParser(usage=usage, version=version)
parser.add_option('-c', '--class', dest="filetype", help=" ".join(filetypes))

# 解析命令行选项
(options, args) = parser.parse_args()

# 定义并初始化脚本使用的变量
filetype='bash'
filename=None
filecontent=None

# 从命令行选项中提取合适的值
if options.filetype:
    if options.filetype in filetypes:
        filetype = options.filetype
    else:
        print >> sys.stderr, "error FILETYPE", options.filetype
        parser.print_help()
        sys.exit(1)
if len(args):
    if os.path.isfile(args[0]):
        filename=args[0]
    else:
        print >> sys.stderr, "file not found:", args[0]
        parser.print_help()
        sys.exit(2)

# 处理默认值
if filetype=='bash':
    print >> sys.stderr, "use default filetype:", filetype
if filename==None:
    print >> sys.stderr, "use stdin as file input."
    filecontent = sys.stdin.read()
else:
    filecontent = open(filename, 'r').read()

# 初始化表单域
fields = [
            ('poster', 'yaoms'),
            ('parent_pid', ''),
            ('paste', 'send'),
            ('class', filetype),
            ('code2', filecontent)
         ]
files = []
# 提交表单
rsp = formdata.post_multipart("paste.ubuntu.org.cn", "/", fields, files)
# 提取关注的内容
print "http://paste.ubuntu.org.cn/%s" % formdata.find_group(r'''href=['"]/d(\d+)''', rsp)
