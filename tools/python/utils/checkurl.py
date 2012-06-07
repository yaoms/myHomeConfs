#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: checkurl.py
# author:   yaoms
# date:     Thu Jun  7 15:50:01 HKT 2012
# describe: 检查apk下载链接是否可用，不可用的自动禁用

import MySQLdb
import time
import urllib2

def useful(url):
    # 建立请求体，将请求方法设为 HEAD
    request = urllib2.Request(url)
    request.get_method = lambda : 'HEAD'
    try:
        # 尝试打开请求，超时设为3秒
        response = urllib2.urlopen(request, timeout=3)
        print response.getcode(), response.msg
        print response.info()
        if response.getcode()==200 and response.headers['Content-Type'].startswith('application/vnd.android.package-archive'):
            return True
    except:
        pass
    return False

def main():
    # 配置数据库参数
    host='localhost'
    db='dbname'
    charset='utf8'
    user='username'
    passwd='123456'
    #user='root'
    #passwd=''

    # 建立数据库连接
    conn = MySQLdb.connect(host=host, db=db, charset=charset, user=user, passwd=passwd)
    cursor = conn.cursor() # 获取数据库游标
    count = cursor.execute("select ac_id, url from dw_apk_cdn where status=0") # 查询有效的cdn记录
    # result = cursor.fetchone()

    # 逐条处理，禁用已经失效的cdn链接
    values = []
    now=int(time.time()*1000)
    for i in cursor:
        print "check ac_id:%d, url:%s ..." % i
	# 如果已经不可用了, 就把它加入到待处理列表中。
        if not useful(i[1]):
            values.append((now, i[0]))
            print 'ac_id', i[0], ' will disable.'

    # 如果待处理列表非空，执行批量修改，禁用对应的记录，并提交。
    if len(values):
        sql="update dw_apk_cdn set dtime=%s, status=1 where ac_id=%s"
        cursor.executemany(sql, values)
        conn.commit()

    # 关闭数据库连接
    cursor.close()
    conn.close()

if __name__ == '__main__':
    #main()
    print useful('http://www.jandan.net/sd')
