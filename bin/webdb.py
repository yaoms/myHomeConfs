#!/usr/bin/env python
# coding:utf8

import web
import datetime
import time

t1=time.mktime(datetime.date(2012,5,28).timetuple())*1000
t2=time.mktime(datetime.date(2012,5,29).timetuple())*1000

db=web.database(dbn="mysql", host="dw-down.douwan.cn", db="douwan3android", user="douwan", pw="dw123456")
res=db.query("select count(*) as c from dw_user where rtime>=%d and rtime<%d" % (t1, t2))

print "2012-05-28号注册人数:", res[0].c

#for i in range(0,len(res)):
#	s=res.i.next()
#	print u"{必须更新：%d, 上传人：%s, 版本名：%s, 版本号：%d, APK地址：%s}" %\
#		(s.forced_update, s.upload_user ,s.versionName, s.versionCode, s.apkUrl)

del res
del db
# 'forced_update': 0L, 'upload_user': u'\u7ba1\u7406\u5458', 'projectId': u'0', 'dv_id': 27L, 'versionName': u'1.1.3', 'file_size': 3235612L, 'versionCode': 17L, 'apkUrl': u'android/platformFile/20120520/17/KKFun_Douwan1.1.3.apk', 'type': 0L, 'utime': 1337485718271L

