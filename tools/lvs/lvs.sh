#!/bin/bash

# 虚拟服务器配置
vip="10.0.5.14"
mask="255.255.255.255"
vdev="eth0:0"

port="80"

# 真实服务器节点地址表，多个ip使用空格间隔
rs_ips="10.0.5.12 10.0.5.13"

ifconfig $vdev $vip broadcast $vip netmask $mask
#route add -host $vip dev $vdev
ipvsadm -C

ipvsadm -A -t $vip:$port -s rr

for rip in $rs_ips
do ipvsadm -a -t $vip:$port -r $rip:$port -g
done

#ifconfig eth0:0 10.0.5.14 broadcast 10.0.5.14 netmask 255.255.255.255
#route add -host 10.0.5.14 dev eth0:0
#ipvsadm -C
#ipvsadm -A -t 10.0.5.14:80 -s rr
#ipvsadm -a -t 10.0.5.14:80 -r 10.0.5.12:80 -g
