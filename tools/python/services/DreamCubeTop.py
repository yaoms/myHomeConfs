#!/usr/bin/python
# -*- coding: utf8 -*-
# filename: dreamCubeTop.py
# author:   yaoms
# date:     Thu Jun 14 14:28:07 HKT 2012
# describe: 查看梦立方排名前30

import MySQLdb
import sys
import web
reload(sys)
sys.setdefaultencoding('UTF-8')

class DreamCubeTop:
    """查看梦立方排名"""

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
    
        sql = "select u.cube_score, u.user_id, u.nickname, u.isrobot, u.password, u.beans, u.is_online, l.city from dw_user u left join dw_location l on l.loc_id=u.loc_id order by u.cube_score desc limit %s,%s" % (index, count)
        output = []
        output.append("execute sql: " + sql)
        count = cursor.execute(sql)
        if count:
            # conn.commit()
            s="<h3>梦立方排名</h3>"
            output.append(s)
            s="<table width='100%' border='1'>"
            output.append(s)
            s="<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % ("id", "cube_score", "user_id", "nickname", "beans", "online", "city", "keep online", "json")
            output.append(s)
            i = index
            for item in cursor:
                (cube_score, user_id, nickname, isrobot, password, beans, is_online, city) = (item[0], item[1], item[2], item[3], item[4], item[5], item[6], item[7])
                i+=1
                ko = "%s %s" % (user_id, password)
                json = '{"uid":"%s", "pwd":"%s"},' % (user_id, password)
                if item[3]==2:
                    output.append("<tr bgcolor='#cec'><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (i, cube_score, user_id, nickname, beans, (is_online==1 and "在线" or '离线'), city, ko, json))
                else:
                    output.append("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (i, cube_score, user_id, nickname, beans, (is_online==1 and "在线" or '离线'), city, "", ""))
            output.append("</table>")

        # 关闭数据库连接
        cursor.close()
        conn.close()

        output.append("<p><a href='/'>BACK</a></p>")

        return "\n".join(output)

if __name__ == '__main__':
    m = DreamCubeTop()
    print m.main()
