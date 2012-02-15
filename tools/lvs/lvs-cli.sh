#!/bin/bash

# 虚拟服务器配置
vip="10.0.5.14"
mask="255.255.255.255"
vdev="lo:0"

ifconfig $vdev $vip broadcast $vip netmask $mask
#route add -host $vip dev $vdev
echo "1" > /proc/sys/net/ipv4/conf/lo/arp_ignore 
echo "2" > /proc/sys/net/ipv4/conf/lo/arp_announce 
echo "1" > /proc/sys/net/ipv4/conf/all/arp_ignore 
echo "2" > /proc/sys/net/ipv4/conf/all/arp_announce 
sysctl -p

#ifconfig lo:0 10.0.5.14 broadcast 10.0.5.14 netmask 255.255.255.255
#route add -host 10.0.5.14 dev lo:0
#echo "1" > /proc/sys/net/ipv4/conf/lo/arp_ignore 
#echo "2" > /proc/sys/net/ipv4/conf/lo/arp_announce 
#echo "1" > /proc/sys/net/ipv4/conf/all/arp_ignore 
#echo "2" > /proc/sys/net/ipv4/conf/all/arp_announce 
#sysctl -p
