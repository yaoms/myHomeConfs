import mysite.settings

from django.contrib.auth.models import User
from mysite.book import helper

if __name__ == "__main__":
	book = helper.getBook(1)
	print "book %s" % book.name
	user = User.objects.get(pk=1)
	print "user %s" % user.username
	auto_marker=helper.getAutoMarker(book,user)
	print "marker %s" % auto_marker
	new_chapters = helper.getNewChaptersFrom(auto_marker.datetime,book)
	for chapter in new_chapters:
		print "%s" % chapter.name

