# encoding: utf-8
from dbi_getdbhandle import dbi_getdbhandle
from dbi_getbookinfo import dbi_getbookinfo

dbh = dbi_getdbhandle()

bookid=1213

bookinfo = dbi_getbookinfo(dbh,bookid)

print u"书名：%s\t作者：%s" % bookinfo
