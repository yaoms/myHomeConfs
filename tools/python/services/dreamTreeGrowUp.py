#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: checkurl.py
# author:   yaoms
# date:     Thu Jun  7 15:50:01 HKT 2012
# describe: 检查apk下载链接是否可用，不可用的自动禁用

import MySQLdb
import time
import urllib2
import random

def main():
    # 配置数据库参数
    host='dw-mysql-remote'
    db='douwan3android'
    charset='utf8'
    user='douwan'
    passwd='dw123456'
    #user='root'
    #passwd=''
    dw_userId=26982
    dw_growupvalue=random.randint(1,3)

    # 建立数据库连接
    conn = MySQLdb.connect(host=host, db=db, charset=charset, user=user, passwd=passwd)
    cursor = conn.cursor() # 获取数据库游标
    sql = "update dw_dream_tree set dream_value = dream_value + %s where user_id = %s"
    values = (dw_growupvalue, dw_userId)
    print "execute sql:", sql % values
    count = cursor.execute(sql, values)
    if count:
        conn.commit()
    else:
        print "userId: %s not found." % dw_userId

    # 关闭数据库连接
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
