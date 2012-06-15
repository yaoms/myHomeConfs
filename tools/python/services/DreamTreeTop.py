#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: dreamTreeTop.py
# author:   yaoms
# date:     Thu Jun 14 14:14:55 HKT 2012

import MySQLdb
import web
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

class DreamTreeTop:
    """查看梦想树排名"""

    def GET(self, count=10, index=0):
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

        output=[]
        sql = "select t.user_id, u.nickname, t.dream_value, u.isrobot from dw_dream_tree t left join dw_user u on u.user_id=t.user_id order by t.dream_value desc limit %s,%s" % (index, count)
        output.append("execute sql: " + sql)
        count = cursor.execute(sql)
        if count:
            # conn.commit()
            s="<h3>梦想树排名</h3>"
            output.append(s)
            s="<table width='100%' border='1'>"
            output.append(s)
            s="<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % ("id", "userId", "Value", "nickname")
            output.append(s)
            i = index
            for item in cursor:
                i+=1
                if item[3]==2:
                    output.append("<tr bgcolor='#cec'><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (i, item[0], item[2], item[1]))
                else:
                    output.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (i, item[0], item[2], item[1]))
            output.append("</table>")

        # 关闭数据库连接
        cursor.close()
        conn.close()

        output.append("<p><a href='/'>BACK</a></p>")

        return "\n".join(output)

if __name__ == '__main__':
    m=DreamTreeTop()
    print m.main()
