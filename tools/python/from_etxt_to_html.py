# coding: utf-8
# 电子书整理程序
from utils.confirm_ask import confirm_ask
from etxt.Book import Book

from optparse import OptionParser
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

# options.filename
# options.dirname

book = Book()
book.load(options.filename)
print book.info()
print("将导出到 %s 目录" % options.dirname)
print("")
if not confirm_ask("是否确认继续？"):
    print("exit")
    sys.exit(0)

book.dumpTo(options.dirname)
