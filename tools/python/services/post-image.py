#!/usr/bin/python
# coding:utf8
# 发送图片到 paste.ubuntu.org.cn
import sys, os, optparse
import formdata

# 配置脚本版本，用法说明，命令行选项等信息
version="%prog 1.0"
usage="usage: %prog FILENAME"
parser = optparse.OptionParser(usage=usage, version=version)

# 解析命令行选项
(options, args) = parser.parse_args()

# 定义并初始化脚本使用的变量
filename=None

# 从命令行选项中提取合适的值
if len(args):
    if os.path.isfile(args[0]):
        filename=args[0]
    else:
        print >> sys.stderr, "file not found:", args[0]
        parser.print_help()
        sys.exit(2)
else:
    print >> sys.stderr, "FILENAME not provided."
    parser.print_help()
    sys.exit(3)

# 初始化表单域
fields = [
            ('poster', 'yaoms'),
            ('parent_pid', ''),
            ('paste', 'send'),
            ('class', 'bash'),
            ('code2', '')
         ]
files = [('screenshot', filename, open(filename, 'rb').read()),]
# 提交表单
rsp = formdata.post_multipart("paste.ubuntu.org.cn", "/", fields, files)
# 提取关注的内容
print "http://paste.ubuntu.org.cn/%s" % formdata.find_group(r'''href=['"]/(i\d+)''', rsp)
