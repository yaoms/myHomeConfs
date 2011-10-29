#!/bin/sh

die() {
	echo $@
	exit 1
}

usage="USAGE: GEO=120x240 DIR=newdir `basename $0` *.jpg"

[ -z $GEO ] && die $usage
[ -z $DIR ] && die $usage
[ $# -lt 1 ] && die $usage

echo $GEO | grep -P '\d+x\d+' || die $usage

w=${GEO%%x*}
h=${GEO##*x}
g=h
[ $w -gt $h ] && g=1
[ $w -le $h ] && g=2

[ -d $DIR ] && rm -rvf $DIR
mkdir -pv $DIR

for img in $@
do
	size=`identify $img | grep -Po '\d+x\d+' | head -1`
	width=${size%%x*}
	height=${size##*x}
	[ $g -eq 1 ] && [ $width -ge $height ] && GEO=${w}x${h}
	[ $g -eq 2 ] && [ $width -ge $height ] && GEO=${h}x${w}
	[ $g -eq 1 ] && [ $width -lt $height ] && GEO=${h}x${w}
	[ $g -eq 2 ] && [ $width -lt $height ] && GEO=${w}x${h}
	new_img=${DIR}/${img}
	echo -n "Start converting $img ..."
	#gm convert -quality 95 -resize ${GEO}^ -gravity Center -crop ${GEO}+0+0  $img $new_img
	gm convert -resize ${GEO}^ -gravity Center -crop ${GEO}+0+0  $img $new_img
	echo "...done" ;
done
