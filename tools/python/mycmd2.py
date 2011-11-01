import mysite.settings

from mysite.post.models import *

def update():
	relays = [r.post for r in RelayRelation.objects.all()]
	postClass = PostClass.objects.filter(text='relay')[0]

	for relay in relays:
		relay.post_class = postClass
		relay.save()

update()
