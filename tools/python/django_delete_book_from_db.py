# coding: utf-8
from mysite.tools.utils.confirm_ask import confirm_ask
from mysite.book import helper

import mysite.settings

import re
import sys


bookid = 0
if len(sys.argv) > 1:
	bookid = int(sys.argv[1])

book = helper.getBook(bookid)
print "=============================="
print u"- 书名:\t%s" % book.name
print u"- 作者:\t%s" % book.author
print "=============================="
if confirm_ask("确认删除吗？"):
	#删除评论
	comments = helper.getCommentsOfBook(book)
	[i.delete() for i in comments]
	#删除书签
	markers = helper.getMarkersOfBook(book)
	[i.delete() for i in markers]
	#删除内容
	chapters = helper.getChaptersOfBook(book)
	[helper.getContent(i).delete() for i in chapters]
	#删除章节
	[i.delete() for i in chapters]
	#删除相关文件
	#删除书
	book.delete()
