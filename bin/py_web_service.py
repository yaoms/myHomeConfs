#!/usr/bin/env python
# coding: utf8

import web

urls = (
		'/hello/(.+)/(.+)', 'hello',
		'/sendmsg/(.+)/(.+)', 'sendmsg'
)

app = web.application(urls, globals())

class hello:
	def GET(self, name, txt):
		if not name:
			name="world"
		if not txt:
			txt="...."
		return "hello %s, %s" % (name, txt)
class sendmsg:
	def GET(self, num, txt):
		return "send text sms to %s: %s" % (num, txt)

if __name__ == "__main__":
	app.run()
