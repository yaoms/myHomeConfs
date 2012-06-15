#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: checkurl.py
# author:   yaoms
# date:     Fri Jun 15 14:28:50 HKT 2012
# describe: 更新用户位置

import MySQLdb
import time
import urllib2
import random
import sys

def main():
    # 配置数据库参数
    host='dw-mysql-remote'
    db='douwan3android'
    charset='utf8'
    user='douwan'
    passwd='dw123456'
    #user='root'
    #passwd=''
    dw_userId=sys.argv[1]
    dw_loc=sys.argv[2]

    # 建立数据库连接
    conn = MySQLdb.connect(host=host, db=db, charset=charset, user=user, passwd=passwd)
    cursor = conn.cursor() # 获取数据库游标
    sql = "select loc_id from dw_location where city like '%%%s%%'" % dw_loc
    print "execute sql:", sql
    count = cursor.execute(sql)
    locids=[]
    for i in cursor:
        locids.append(i[0])
    if not len(locids):
        print dw_loc, "不存在于现有的位置库"
        sys.exit(2)
    index = random.randint(0,len(locids)-1)
    locid=locids[index]
    sql = "update dw_user set loc_id=%s where user_id=%s" % (locid, dw_userId)
    print sql
    count=cursor.execute(sql)
    if count:
        conn.commit()
    else:
        print "userId: %s not found." % dw_userId

    # 关闭数据库连接
    cursor.close()
    conn.close()

if __name__ == '__main__':
    if len(sys.argv)<3:
        print "%s uid city" % (sys.argv[0])
        sys.exit(1)
    main()
