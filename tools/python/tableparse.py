#!/usr/bin/python
# -*- coding: utf8 -*-
# Author:   yaoms
# Date:     Tue Jun  5 11:04:10 HKT 2012
# Describe: 这是一个处理异构数据表导入的脚本，从其他数据库到出的数据，
#           以csv文件的形式读入，逐行处理，拼凑成新的Sql插入语句。

import sys
import time

def parse(fi, fo):
    for i in fi:
        if i.startswith('p'):
            continue
        (phonenum,imsi,lsn,telecom,projectid,productid,feeid,feeamount,chargeno,CreateTime) = i.strip().split(',')
        #print phonenum,imsi,lsn,telecom,projectid,productid,feeid,feeamount,chargeno,CreateTime
        #(recharge_id,fee_id,charge_no,fee_amount,product_id,project_id,imsi,lsn,  phonenum,telecom,charge_date,status,result,result_str,get_time)
        print >> fo, "(0, %s, '%s', %s, %s, %s, '%s','%s', '%s', %s, '%s', 1, 0, '成功', %d)," %\
                        (feeid,chargeno,feeamount,productid,projectid,imsi,lsn,phonenum,telecom,CreateTime,int(get_time(CreateTime)*1000))

def get_time(strtime):
    return time.mktime(time.strptime(strtime, '%Y-%m-%d %H:%M:%S'))

if __name__ == '__main__':
    #print "%d" % (get_time('2012-05-27 12:34:12')*1000)
    parse(sys.stdin, sys.stdout)
