#!/bin/sh
cat /home/yaoms/bin/add_nameserver.conf >>  /etc/resolv.conf
/etc/init.d/networking restart
