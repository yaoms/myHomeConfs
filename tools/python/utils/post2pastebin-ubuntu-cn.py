#!/usr/bin/python
# coding:utf8
# 发送代码和截图到 paste.ubuntu.org.cn

import sys, os, optparse, re
import formdata

# 配置脚本版本，用法说明，命令行选项等信息
version="%prog 1.0"
usage="usage: %prog [options] [FILENAME]\n\n\t-- read from stdin if FILENAME is -."
filetypes = [
        "actionscript", "actionscript-french", "ada", "apache", "applescript", "asm", "asp", "autoit", "bash",
        "blitzbasic", "c", "c_mac", "caddcl", "cadlisp", "cfdg", "cpp", "csharp", "css", "d", "delphi", "diff",
        "div", "dos", "eiffel", "fortran", "freebasic", "gml", "html4strict", "inno", "java", "java5", "javascript",
        "lisp", "lua", "matlab", "mpasm", "mysql", "nsis", "objc", "ocaml", "ocaml-brief", "oobas", "oracle8",
        "pascal", "perl", "php", "php-brief", "python", "qbasic", "robots", "ruby", "sas", "scheme", "sdlbasic",
        "smarty", "sql", "tsql", "vb", "vbnet", "vhdl", "visualfoxpro", "xml"
        ]

parser = optparse.OptionParser(usage=usage, version=version)
parser.add_option('-c', '--class', dest="filetype", help=" ".join(filetypes), default="bash")
parser.add_option('-s', '--screenshot', dest="screenshot", help="screenshot to attach.", default=None)

# 解析命令行选项
(options, args) = parser.parse_args()

# 定义并初始化脚本使用的变量
filetype=None
filename=None
filecontent=None
screenshot=None
files=None

# 从命令行选项中提取合适的值
if options.filetype in filetypes:
    filetype = options.filetype
else:
    print >> sys.stderr, "error FILETYPE", options.filetype
    parser.print_help()
    sys.exit(1)

if options.screenshot:
    if os.path.isfile(options.screenshot) and re.match(r".*(jpeg|jpg|png)", options.screenshot):
        screenshot=options.screenshot
    else:
        print >> sys.stderr, "error screenshot", options.screenshot
        parser.print_help()
        sys.exit(1)

if len(args):
    if args[0]=='-':
        filename="-"
    elif os.path.isfile(args[0]):
        filename=args[0]
    else:
        print >> sys.stderr, "file not found:", args[0]
        parser.print_help()
        sys.exit(2)
else:
    filename=None


# 处理默认值
if filetype=='bash':
    print >> sys.stderr, "use default filetype:", filetype
if filename:
    if filename=="-":
        print >> sys.stderr, "use stdin as file input."
        filecontent = sys.stdin.read()
    else:
        filecontent = open(filename, 'r').read()
else:
    filecontent=""
if screenshot:
    files=[('screenshot', screenshot, open(screenshot, 'rb').read()),]
else:
    files=[]

# 初始化表单域
fields = [
            ('poster', 'name'),
            ('parent_pid', ''),
            ('paste', 'send'),
            ('class', filetype),
            ('code2', filecontent)
         ]
# 提交表单
rsp = formdata.post_multipart("paste.ubuntu.org.cn", "/", fields, files)
# 提取关注的内容
print "http://paste.ubuntu.org.cn/%s" % formdata.find_group(r'''href=['"]/d(\d+)''', rsp)
