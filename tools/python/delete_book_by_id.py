# encoding: utf-8
import sys

from confirm_ask import confirm_ask
from dbi_deletebookinfoexceptbook import dbi_deletebookinfoexceptbook
from dbi_getdbhandle import dbi_getdbhandle

print "请输入需要删除的书ID:",
bookid=int(raw_input().strip())
if bookid:
    pass
else:
    print "错误的书ID。"
    sys.exit(1)

dbh = dbi_getdbhandle()

# 执行一下Sql语句
cursor = dbh.cursor()
cursor.execute(u"SELECT BOOKID,BOOKNAME,AUTHOR FROM BOOK WHERE BOOKID=:bookid",bookid=bookid)

goon = confirm_ask(u"%d\t %s\t作者:%s\n确认删除吗？" % cursor.fetchone())
cursor.close()
if goon:
    pass
else:
    sys.exit(0)

dbi_deletebookinfoexceptbook(dbh,bookid)

print "删除 图书 %d 的相关信息..." % bookid
cursor = dbh.cursor()
cursor.execute(u"delete from book where bookid=:bookid",bookid=bookid)
if cursor.rowcount:
    print "删除了 %d 条记录。\n" % cursor.rowcount
else:
    print "没有删除任何记录。\n"


dbh.commit()
#//断开连接



