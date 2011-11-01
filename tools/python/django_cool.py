import mysite.settings

from mysite.post.models import Post
from mysite.book.models import Book,Author

import datetime

cool_set = [Post, Book, Author]

def cool():
	print "[%s] start cooling..." % datetime.datetime.now()
	count = 0
	for model in cool_set:
		items = [ i for i in model.objects.filter(hits__gte=0) ]

		for item in items:
			item.hits -= 1
			item.save()
			count += 1

	print "[%s] %d items cooled, sleep......." % (datetime.datetime.now(), count)

if __name__ == "__main__":
	cool()
