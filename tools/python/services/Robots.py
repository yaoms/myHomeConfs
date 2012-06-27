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

    def main(self, count=20, index=0):
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
        sql = "select u.user_id, u.password, u.nickname, u.beans, u.cube_score, u.is_online, u.ip, u.lltime, l.city, dt.dream_value from (dw_user u left join dw_location l on u.loc_id=l.loc_id) left join dw_dream_tree dt on dt.user_id=u.user_id where u.isrobot=2 limit %s,%s" % (index, count)
        output.append("execute sql: " + sql)
        count = cursor.execute(sql)
        if count:
            # conn.commit()
            s="<h3>机器人列表</h3>"
            output.append(s)
            s="<table width='100%' border='1'>"
            output.append(s)
            s="<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % ("id", "keep online", "json", "beans", "cube score", "dream value", "ip", "city", "online", "lastonlinetime")
            output.append(s)
            i = index
            for item in cursor:
                i+=1
                (user_id, password, nickname, beans, cube_score, is_online, ip, lltime, city, dream_value) = item
                keep_online="%s %s" % (user_id, password)
                json='{"nick":"%s", "uid":"%s", "pwd":"%s"},' % (nickname, user_id, password)
                if is_online:
                    online='<span style="background:#e99;">在线</span>'
                else:
                    online="离线"
                output.append('<tr style="background:#cec;"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (i, keep_online, json, beans, cube_score, dream_value, ip, city, online, getHumanTime(lltime)))
            output.append("</table>")
    
        # 关闭数据库连接
        cursor.close()
        conn.close()

        output.append("<p><a href='/'>BACK</a></p>")

        return "\n".join(output)

def getHumanTime(timestamp):
    import time
    seces = time.time()-timestamp/1000
    if seces < 0:
        seces = 0
    if seces < 3600:
        return "<span style='background:#aea'>%s分钟</span>" % int(seces/60)
    elif seces >= 3600 and seces < 86400:
        return "<span style='background:yellow'>%s小时</span>" % int(seces/3600)
    elif seces >= 86400 and seces < 2592000:
        return "<span style='background:orange'>%s天</span>" % int(seces/86400)
    else:
        return "<span style='background:red'>一月之前</span>"

if __name__ == '__main__':
    m=Robots()
    print m.main()
