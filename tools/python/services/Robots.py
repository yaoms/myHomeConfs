#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: dreamCubeTop.py
# author:   yaoms
# date:     Thu Jun 14 17:42:30 HKT 2012

import MySQLdb
import web
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class Robots:
    """查看机器人列表"""

    def GET(self, count=20, index=0):
        web.header('Content-Type', 'text/html; charset=utf-8')
        index=int(index)
        count=int(count)
        return self.main(count, index)

    def main(self, count=10, index=0):
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
        cursor = conn.cursor() # 获取数据库游标
    
        output = []
        sql = "select username, user_id, password, nickname, beans from dw_user where isrobot=2 limit %s,%s" % (index, count)
        output.append("execute sql: " + sql)
        count = cursor.execute(sql)
        if count:
            # conn.commit()
            s="<h3>机器人列表</h3>"
            output.append(s)
            s="<table width='100%' border='1'>"
            output.append(s)
            s="<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % ("id", "name", "keep online", "json", "nickname", "beans")
            output.append(s)
            i = index
            for item in cursor:
                i+=1
                output.append('<tr><td>%s</td><td>%s</td><td>%s %s</td><td>{"uid":"%s", "pwd":"%s"}</td><td>%s</td><td>%s</td></tr>' % (i, item[0], item[1], item[2], item[1], item[2], item[3], item[4]))
            output.append("</table>")
    
        # 关闭数据库连接
        cursor.close()
        conn.close()

        output.append("<p><a href='/'>BACK</a></p>")

        return "\n".join(output)

if __name__ == '__main__':
    m=Robots()
    print m.main()
