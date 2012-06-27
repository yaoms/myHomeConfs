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

    def GET(self, orderby="cube", count=20, index=0):
        web.header('Content-Type', 'text/html; charset=utf-8')
        index=int(index)
        count=int(count)
        return self.main(orderby, count, index)

    def main(self, orderby="cube", count=20, index=0):
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

        if orderby == 'cube':
            order = "u.cube_score desc"
        elif orderby == 'dream':
            order = "dt.dream_value desc"
        else:
            order = "u.cube_score desc"
            orderby = "cube"
    
        sql = "select u.user_id, u.password, u.nickname, u.beans, u.cube_score, u.is_online, u.isrobot, u.ip, u.lltime, l.city, dt.dream_value from (dw_user u left join dw_location l on u.loc_id=l.loc_id) left join dw_dream_tree dt on dt.user_id=u.user_id order by %s limit %s,%s" % (order, index, count)
        output = []
        output.append("<!--execute sql: " + sql + "-->")
        count = cursor.execute(sql)
        if count:
            # conn.commit()
            s="<h3>梦立方排名</h3>"
            output.append(s)
            s="<table width='100%' border='1'>"
            output.append(s)
            pager=""
            if count==20:
                if index==0:
                    pass
                else:
                    pager="count%s/index%s" % (count, index)
            else:
                if index==0:
                    pager="count%s" % count
                else:
                    pager="count%s/index%s" % (count, index)

            s="<tr><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th></tr>" % ("id", "keep online", "json", "beans", orderby=="cube" and '<span style="background:green;color:white;">cube score</span>' or ('<a href="/top/cube/%s">cube score</a>' % pager), orderby=="dream" and '<span style="background:green;color:white;">dream value</span>' or ('<a href="/top/dream/%s">dream value</a>' % pager), "ip", "city", "online", "last online time", "is robot")
            output.append(s)
            i = index
            for item in cursor:
                (user_id, password, nickname, beans, cube_score, is_online, isrobot, ip, lltime, city, dream_value) = item
                i+=1
                style=''
                is_robot="用户"
                keep_online="&nbsp;"
                json="&nbsp;"
                if isrobot==2:
                    style='style="background:#cec;"'
                    is_robot="机器人"
                    keep_online = "%s %s" % (user_id, password)
                    json = '{"nick":"%s", "uid":"%s", "pwd":"%s"},' % (nickname, user_id, password)
                else:
                    json = '{"nick":"%s", "uid":"%s", "pwd":"%s"},' % (nickname, user_id, "")
                if is_online:
                    online = '<span style="background:#e99">在线</span>'
                else:
                    online = "离线"
                output.append("<tr %s><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % (style, i, keep_online, json, beans, cube_score, dream_value, ip, city, online, self.getHumanTime(lltime), is_robot))
            output.append("</table>")

            pages="<p>%s %s %s</p>" % (index==0 and "首页" or '<a href="/top/%s/count%s/index0">首页</a>' % (orderby, count),  index==0 and "上一页" or '<a href="/top/%s/count%s/index%s">上一页</a>' % (orderby, count, index-count<0 and 0 or index-count), '<a href="/top/%s/count%s/index%s">下一页</a>' % (orderby, count, index+count))
            output.append(pages)

        # 关闭数据库连接
        cursor.close()
        conn.close()

        output.append("<p><a href='/'>BACK</a></p>")

        return "\n".join(output)

    def getHumanTime(self, timestamp):
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
    m = DreamCubeTop()
    print m.main()
