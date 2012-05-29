#!/usr/bin/env python
# coding:utf-8

import web

urls = (
		'/send', "send",
		'/.*', "index"
	)

mailSendFrom = 'monitor-py'
mailSendTo = 'receiver@domain.com' #['sss@gmail.com', 'mailreader@mail.com']

class index:
	def GET(self):
		return "USAGE: wget -qSO- %s://%s/send --post-data 'POST DATA as message content.'\n" % (web.ctx.protocol, web.ctx.host)
	def POST(self):
		return web.seeother("/")

class sendMsg:
	def GET(self, subject=None):
		return web.seeother('/')

	def POST(self, subject="App Warning"):
		content = web.data()
		if content:
			sendMessage(subject, content)
			return "ok\n"
		else:
			return "empty content\n"

def sendMessage(subject, content):
	web.sendmail(mailSendFrom, mailSendTo, subject, content)
	# send sms ...

app = web.application(urls, locals())

if __name__ == '__main__':
	web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
	app.run()
