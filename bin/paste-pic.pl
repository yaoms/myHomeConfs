#!/usr/bin/perl -w
use utf8;
use strict;
use WWW::Mechanize;
my $poster="yaoms";
my $paste_url = 'http://paste.ubuntu.org.cn/';
my $mech = WWW::Mechanize->new();

$mech -> get("$paste_url");

$mech -> submit_form(
	fields => { 
		"screenshot" => $ARGV[0],
		#"code2" => join("\n",`xsel -o`),
		"poster" => $poster,
		"class" => "perl"
	} ,
	form_name => "editor" ,
	button => "paste"
);

if ($mech->success()) {
	my $rr=$mech->uri();
	print "$rr\n";
	#`echo $rr|xsel -i`;
	#`/home/exp/应用/脚本/msg eog-48.png 贴图地址 $rr`;
} else {
	#`/home/exp/应用/脚本/msg 贴图 失败`;
	print "ERROR:\t".$mech->status()."\n";
}
