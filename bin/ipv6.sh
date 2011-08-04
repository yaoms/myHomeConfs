#!/bin/sh
cat add_nameserver.conf >>  /etc/resolv.conf
/etc/init.d/networking restart
