#!/bin/sh
#echo $#
if [ $# -lt 1 ]
then echo "Usage: `basename $0` domain [ postfix1,postfix2,... ]"
exit 1
fi

DOMAIN=$1
POSTFIX="com"
if [ $# -gt 1 ]
then POSTFIX=`echo $2 | sed 's/,/ /g'`
fi

echo "检查结果:"
for d in $POSTFIX
do whois $DOMAIN.$d | grep 'No match' &> /dev/null
    if [ $? -eq 0 ]
    then echo "$DOMAIN.$d   可用"
    else echo "$DOMAIN.$d   不可用"
    fi
done
