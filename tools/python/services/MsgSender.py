#!/usr/bin/env python
# coding:utf-8

import web

class MsgSender:
    """消息发送器"""

    def GET(self, subject=None):
        return web.seeother('/')

    def POST(self, subject="App Warning"):
        content = web.data()
        if content:
            self.sendMessage(subject, content)
            return "ok\n"
        else:
            return "empty content\n"

    def sendMessage(self, subject, content):
        mailSendFrom = 'monitor-py'
        mailSendTo = 'receiver@domain.com' #['sss@gmail.com', 'mailreader@mail.com']

        # web.sendmail(mailSendFrom, mailSendTo, subject, content)
        # send sms ...
        return "ok"
