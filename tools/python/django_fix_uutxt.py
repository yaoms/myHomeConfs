# -*- coding: utf-8 -*-
import mysite.settings

from django.contrib.auth.models import User
from mysite.book import helper

if __name__ == "__main__":
	book = helper.getBook(3) #bookid 
	print u"书名：%s" % book.name
	chapters = helper.getChaptersOfBook(book)
	for chapter in chapters:
		print "%s" % chapter.name
		chapter.name = chapter.name.replace(u"正文 ","")
		print "%s" % chapter.name
		chapter.save()
