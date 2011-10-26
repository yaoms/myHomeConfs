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

[ -d $DIR ] && rm -rvf $DIR
mkdir -pv $DIR

for img in $@
do
	size=`identify $img | grep -Po '\d+x\d+' | head -1`
	width=${size%%x*}
	height=${size##*x}
	[ $width -ge $height ] && GEO=${w}x${h}
	[ $width -lt $height ] && GEO=${h}x${w}
	new_img=${DIR}/${img}
	echo -n "Start converting $img ..."
	gm convert -quality 95 -resize ${GEO}^ -gravity Center -crop ${GEO}+0+0  $img $new_img
	echo "...done" ;
done
