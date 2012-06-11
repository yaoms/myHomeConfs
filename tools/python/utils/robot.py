#!/usr/bin/python
# coding:utf8
from datetime import datetime
from random import random

actions = [
        {
            'type':'signin', # 签到
            'startHour':(7,), # 时间段内执行 默认 (0,23)
            'startMin':(0,59), # 默认 (0,59)
            'startSec':(0,59) # 默认 (0,59)
            },
        {
            'type':'playcube' # 报名赛
            },
        {
            'type':'traincube' # 练习赛
            }
        ]
robots = [
        {
            'uid':133244, # 豆玩号
            'password':'dsfqdsdf' # 密码
            },
        {
            'uid':133246, # 豆玩号
            'password':'dsfqdsdf' # 密码
            }
        ]

def init(robots, actions):
    tasks = []
    for robot in robots:
        for action in actions:
            for hour in range(0, 24):
                hours = None
                if action.has_key('startHour'):
                    hours = action['startHour']
                if not hours:
                    hours = range(0, 24)
                if hour in hours:
                    minute = int(random()*60)
                    second = int(random()*60)
                    tasks.append({'type':action['type'], 'uid':robot['uid'], 'password':robot['password'], 'time':datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour, minute, second)})
    print len(tasks)
    print tasks

if __name__ == '__main__':
    init(robots, actions)
