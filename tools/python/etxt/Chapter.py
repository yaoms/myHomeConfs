# coding: utf-8

import sys
import os
import datetime

class Chapter:
	"""图书章节"""
	def __init__(self):
		self.name   = ""
		self.paragraphs = []

	def dumpTo(self, dirname, pre, index, nxt, chapters):
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
""" % (self.name, self.name))
		
		for p in self.paragraphs:
			this_chapter_file.writelines("""<p>%s</p>\n""" % p)
		
		this_chapter_file.writelines("<hr/>\n")
		this_chapter_file.writelines("<p>")
		if pre >= 1:
			this_chapter_file.writelines("""<a href="%d.html" title="prev">上一章</a>\n""" % pre)
		this_chapter_file.writelines("""<a href="index.html" title="home">返回目录</a>\n""")
		if nxt <= chapters:
			this_chapter_file.writelines("""<a href="%d.html" title="next">下一章</a>\n""" % nxt)
		this_chapter_file.writelines("</p>\n")
		
		this_chapter_file.writelines("""</body>
</html>""")
		this_chapter_file.close()
