#!/usr/bin/env python
# coding: utf8

import web
import sendTextMsg

urls = (
		'/hello/(.+)', 'hello',
		'/sendmsg/(.+)/(.+)', 'sendmsg'
)

app = web.application(urls, globals())

class hello:
	def GET(self, name):
		if not name:
			name="world"
		return "hello %s" % name

class sendmsg:
	def GET(self, num, txt):
		sendTextMsg.sendSMS(num, txt)
		return "send text sms to %s: %s" % (num, txt)

if __name__ == "__main__":
	app.run()
