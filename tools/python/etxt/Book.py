# coding: utf-8

import sys

class Book:
	"""etxt 图书对象"""
	name	= ''
	author	= ''
	chapters= []
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
				currentChapter.content = []
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

class Chapter:
	"""图书章节"""
	title	= ""
	content	= []

if __name__ == "__main__":
	f = open(sys.argv[1], "r")
	lines = f.readlines()
	book = Book()
	book.load(lines)
	book.info()
