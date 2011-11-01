# coding: utf-8
from mysite.tools.utils.confirm_ask import confirm_ask
from mysite.book import helper

import mysite.settings

import re
import sys
import datetime


filename = ''
bookid = 0
if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	print "USAGE: %s file" % sys.argv[0]

chapterCount = -1
wordCount = 0
chapters = []

f = open(filename,'r')
p = re.compile(r'(.+) 字数:(\d+)')
for line in f:
    if line.startswith('编号:'):
        bookid = line.replace('编号:','').strip()
    elif p.match(line):
        if chapterCount>-1:
            chapters[chapterCount]['wordcount'] = len(chapters[chapterCount]['content'].decode('utf-8'))
        g = p.match(line)
        chapterCount += 1
        wordCount += int(g.group(2))
        chapters += [{'title':g.group(1),'content':"",'wordcount':int(g.group(2))}]
    elif chapterCount>=0 and line.startswith('  '):
        chapters[chapterCount]['content'] += line.strip()
        chapters[chapterCount]['content'] += "\n"
chapterCount += 1

f.close()

print bookid
book = helper.getBook(bookid)
bookName = book.name
author = book.author


#提问一些简单的信息，例如书的分类
print "显示统计-更新-信息"
print "------------------------------"
print "- 编号：\t%s" % bookid
print u"- 书名：\t%s" % bookName
print u"- 作者：\t%s" % author
print "- 章节数：\t%s" % chapterCount
print "- 字数：\t%s" % wordCount
print "------------------------------"
print

if not confirm_ask("是否确认继续？"):
    print "exit"
    sys.exit(0)

for chapter in chapters:
	chapter_db=helper.getNewChapter(book=book,name=chapter['title'],wordcount=chapter['wordcount'])
	chapter_db.save()
	content = helper.getNewContent(chapter=chapter_db,content=chapter['content'])
	content.save()

book.updatetime = datetime.datetime.now()
book.save()
