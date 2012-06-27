#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: checkurl.py
# author:   yaoms
# date:     2012年 06月 16日 星期六 15:45:33 CST
# describe: 监控豆顽服务器

from checkurl import useful
import MySQLdb
import os

def main():
    rsp = useful('http://dw-web.douwan.cn/douwan3android/main')
    print rsp
    if rsp and rsp[0]==200 and rsp[1].startswith('mix-text/'):
        print "server ok"
    else:
        os.system('wget -qSO- http://dw3.tisgame.cn:8080/send --post-data "%s"' % "豆顽服务器挂了。。。")
    # 配置数据库参数
    host='dw-mysql-remote'
    db='douwan3android'
    charset='utf8'
    user='douwan'
    passwd='dw123456'
    #user='root'
    #passwd=''

    # 建立数据库连接
    conn = MySQLdb.connect(host=host, db=db, charset=charset, user=user, passwd=passwd)
    if conn:
        print 'db connected.'
        conn.close()
    else:
        os.system('wget -qSO- http://dw3.tisgame.cn:8080/send --post-data "%s"' % "数据库挂了。。。")


if __name__ == '__main__':
    main()
