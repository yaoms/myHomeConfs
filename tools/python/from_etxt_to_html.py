# coding: utf-8
from optparse import OptionParser
from utils.confirm_ask import confirm_ask
from etxt.Book import Book, Chapter

import re
import os
import sys

version = "%prog 1.0"
usage="\n\n  %prog -f eletxtbookname.etxt -d outputdir"

parser = OptionParser(usage=usage, version=version)
parser.add_option("-f", "--file", dest="filename",
                      help="read etxt from FILENAME.")
parser.add_option("-d", "--dir", dest="dirname",
                      help="output html to this DIRNAME.")
(options, args) = parser.parse_args()

if not options.filename or not options.dirname:
    parser.print_help()
    sys.exit(1)

f = open(options.filename,'r')
lines = f.readlines()
f.close()

book = Book()
book.load(lines)

#提问一些简单的信息，例如书的分类
book.info()
#for chapter in chapters[:3]:
#    print chapter['title']
#    print "-----------------------"
#    print chapter['content']
#    print "-----------------------"
##!!!!!
#sys.exit(0)
print("将导出到 %s 目录" % options.dirname)

if not confirm_ask("是否确认继续？"):
    print("exit")
    sys.exit(0)

book.dumpTo(options.dirname)

