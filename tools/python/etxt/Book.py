# coding: utf-8

import sys
import os
import datetime

class Chapter:
	"""图书章节"""
	def __init__(self):
		self.title   = ""
		self.content = []

class Book:
	"""etxt 图书对象"""
	def __init__(self):
		self.name     = ""
		self.author   = ""
		self.chapters = []

	def load(self, lines):
		currentChapter = 0;
		for line in lines:
			if line.startswith("书名:"):
				self.name = line.strip()[len("书名:"):]
			if line.startswith("作者:"):
				self.author = line.strip()[len("作者:"):]
			if line.count(" 字数:"):
				if currentChapter:
					self.chapters.append(currentChapter)
				currentChapter = Chapter()
				currentChapter.title = line.strip()[:line.index(" 字数:")]
			if line.startswith("  "):
				if currentChapter:
					currentChapter.content.append(line.strip())
		if currentChapter:
			self.chapters.append(currentChapter)

	def info(self):
		print("")
		print("书名: %s" % self.name)
		print("作者: %s" % self.author)
		print("章节: %d章" % len(self.chapters))
		print("")
		if __name__ == "__main__":
			print("=================")
			for c in self.chapters:
				print(" = %s" % c.title)
				print(id(c.content))
			print("=================")
	
	def dumpTo(self, dirname):
		"""将本书导出到指定目录"""
		if not os.path.isdir(dirname):
			os.mkdir(dirname)
		
		
		indexfile = open("%s/index.html" % dirname, 'w')
		
		indexfile.writelines("""<html>
<head>
<title>%s</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
</head>
<body>
<h1>《%s》</h1>
<p>作者：%s</p>
<ol>
""" % (self.name, self.name, self.author))
		
		index=1
		pre=0
		nxt=index+1
		
		for chapter in self.chapters:
			indexfile.writelines("""  <li><a href="%d.html">%s</a></li>\n""" % (index, chapter.title))
			this_chapter_file=open("%s/%d.html" % (dirname, index), 'w')
			this_chapter_file.writelines("""<html>
<head>
<title>%s</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
<style>
p {text-indent:2em;}
</style>
</head>
<body>
<h1>%s</h1>
""" % (chapter.title, chapter.title))
		
			for p in chapter.content:
				this_chapter_file.writelines("""<p>%s</p>\n""" % p)
			
			this_chapter_file.writelines("<hr/>\n")
			this_chapter_file.writelines("<p>")
			if pre >= 1:
				this_chapter_file.writelines("""<a href="%d.html" title="prev">上一章</a>\n""" % pre)
			this_chapter_file.writelines("""<a href="index.html" title="home">返回目录</a>\n""")
			if nxt <= len(self.chapters):
				this_chapter_file.writelines("""<a href="%d.html" title="next">下一章</a>\n""" % nxt)
			this_chapter_file.writelines("</p>\n")
		
			this_chapter_file.writelines("""</body>
</html>""")
			this_chapter_file.close()
			index+=1;
			pre = index - 1
			nxt = index + 1
		
		indexfile.writelines("""</ol>
<p>Generated by from_etxt_to_html.py by yaoms. %s</p>
</body>
</html>""" % datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %T"))
		
		indexfile.close()

if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	lines = f.readlines()
	book = Book()
	book.load(lines)
	book.info()
