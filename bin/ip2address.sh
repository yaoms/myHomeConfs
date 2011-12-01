#!/bin/sh

if [ $# -lt 1 ]
then echo "USAGE: `basename $0` ipOrHostname"
exit 1
fi

IP_OR_HOSTNAME=$1

RES="`wget -qO- "http://ip138.com/ips.asp?ip=$IP_OR_HOSTNAME&action=2" | perl -ne 'if (/"ul1"/) { s/<\/li><li>/\n/g; s/<[^<>]+>//g; s/^\s+//g; s/[\f\t ]+$//g; print }' | iconv -f GB18030`"

echo "[ ip138.com 提供的数据 ]"
echo "$RES"
