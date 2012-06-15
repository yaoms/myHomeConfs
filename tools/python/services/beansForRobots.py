#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: checkurl.py
# author:   yaoms
# date:     Thu Jun  7 15:50:01 HKT 2012
# describe: 给没有钱的机器人加钱

import MySQLdb
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
    dw_growupvalue=random.randint(13,82)

    # 建立数据库连接
    conn = MySQLdb.connect(host=host, db=db, charset=charset, user=user, passwd=passwd)
    cursor = conn.cursor() # 获取数据库游标
    sql = "update dw_user set beans = beans + %s where isrobot=2 and beans < 20"
    values = (dw_growupvalue)
    print "execute sql:", sql % values
    count = cursor.execute(sql, values)
    if count:
        conn.commit()

    # 关闭数据库连接
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
