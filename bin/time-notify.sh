#!/bin/bash
set -u
set -e
set -E
command="$@"
tmp="/tmp/fifo-time-notify"
startime=$(date +%s)
$command
endtime=$(date +%s)

time_cost=$(expr $endtime - $startime )

#echo 
#echo "Execute:" $command
#echo "Cost   :" $time_cost seconds

icon=/usr/share/pixmaps/faces/butterfly.png
DISPLAY=:0.0 notify-send -i $icon -u low "命令执行完毕" """$command:\n消耗时间：$time_cost 秒"""
canberra-gtk-play -f /usr/share/sounds/gnome/default/alerts/drip.ogg &
