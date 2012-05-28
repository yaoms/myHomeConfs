#!/bin/bash

# require ENV TMP
TMP=/tmp/tmp.html
# require ENV HHTM
# require ENV FHTM

die() {
	echo USAGE: HHTM=HHTM FHTM=FHTM `basename $0` xxx.md
	echo HHTM	头部文件
	echo FHTM	尾部文件
	exit 1
}

[ ! -z $HHTM ] && [ -f $HHTM ] || die
[ ! -z $FHTM ] && [ -f $FHTM ] || die
[ ! -z $1 ] && [ -f $1 ] || die

cat $HHTM
markdown $1 | perl -pe '$i=1 if $i==0;s/(<h\d>\d)/<a name="a_$i"\/>\1/,$i++ if m/<h\d>\d/' | tee $TMP | perl -ne 'if (m/<a name/) {s/<a name="([^"]+)"\/><h\d>(.+)<\/h\d>$/<a href="#\1">\2<\/a><br \/>/; print}'
echo "<br />"
echo "<hr />"
echo "<br />"
cat $TMP
cat $FHTM

rm $TMP
