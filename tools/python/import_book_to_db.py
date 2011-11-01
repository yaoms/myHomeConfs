# encoding: utf-8
from confirm_ask import confirm_ask
from mysite.book import helper

import mysite.settings

import re
import sys


filename = ''
if len(sys.argv) > 1:
    filename = sys.argv[1]

bookName = ''
author = ''
keyword = ''
chapterCount = -1
wordCount = 0
chapters = []

f = open(filename,'r')
p = re.compile(r'(.+) 字数:(\d+)')
for line in f:
    if line.startswith('书名:'):
        bookName = line.replace('书名:','').strip()
    elif line.startswith('作者:'):
        author = line.replace('作者:','').strip()
    elif line.startswith('标签:'):
        keyword = line.replace('标签:','').strip()
    elif p.match(line):
        g = p.match(line)
        chapterCount += 1
        wordCount += int(g.group(2))
        chapters += [{'title':g.group(1),'content':"",'wordcount':int(g.group(2))}]
    elif chapterCount>=0 and line.startswith('  '):
        chapters[chapterCount]['content'] += line.strip();
        chapters[chapterCount]['content'] += "\n";
chapterCount += 1

f.close()

#提问一些简单的信息，例如书的分类
print "显示统计信息"
print "------------------------------"
print "- 书名：\t%s" % bookName
print "- 作者：\t%s" % author
print "- 标签：\t%s" % keyword
print "- 章节数：\t%d" % chapterCount
print "- 字数：\t%d" % wordCount
print "------------------------------"
print
#for chapter in chapters[:3]:
#    print chapter['title']
#    print "-----------------------"
#    print chapter['content']
#    print "-----------------------"
##!!!!!
#sys.exit(0)

if not confirm_ask("是否确认继续？"):
    print "exit"
    sys.exit(0)


catalogs = helper.getCatalogs()
for catalog in catalogs:
	print "%s\t%s" % (catalog.id,catalog.name)

catalog_selecteds=None

err=''
while True:
	print "%s请选择此书的分类ID: " % err,
	catalog_id=int(raw_input())

	catalog_selecteds = [i for i in catalogs if i.id==catalog_id]

	err='发现错误，'
	if len(catalog_selecteds):
		break

book = helper.getNewBook(name=bookName,catalog=catalog_selecteds[0],author=author,tag=keyword)
book.save()

for chapter in chapters:
	chapter_db=helper.getNewChapter(book=book,name=chapter['title'],wordcount=chapter['wordcount'])
	chapter_db.save()
	content = helper.getNewContent(chapter=chapter_db,content=chapter['content'])
	content.save()

