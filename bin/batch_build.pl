#!/usr/bin/perl -w
use strict;

# 项目ID配置文件
my $conf="/path/to/project/res/values/string_config.xml";
# 项目ID列表
my $list="/tmp/list";
# 编译命令
my $ant_cmd="./ant.sh";


## 文件操作命令配置
# 拷贝文件命令
my $copy_cmd="copy";
# 删除文件命令
my $del_cmd="del";
# 移动文件命令
my $move_cmd="move";

if ($^O =~ /linux/) {
# 拷贝文件命令
	my $copy_cmd="cp";
# 删除文件命令
	my $del_cmd="rm";
# 移动文件命令
	my $move_cmd="mv";
}

open LIST, "<", $list;
my @proIds=<LIST>;
close LIST;

foreach my $proId(@proIds){
	$proId =~ s/^\s+//;
	$proId =~ s/\s+$//;

	# 备份原始文件
	system("$copy_cmd $conf $conf.bak");

	# 生成替换后的临时文件
	open(FP, "<$conf");
	open(NEW, ">$conf.tmp");
	while(<FP>) {
		# 替换项目ID
		s#<string name="proId">.+</string>#<string name="proId">$proId</string>#;
		print NEW;
	}
	close(FP);
	close(NEW);

	# 用临时文件替换原文件内容
	system("$move_cmd $conf.tmp $conf");

	print "当前项目ID：". $proId . "\n";
	print "调用 ant 编译打包 .....\n";

	# 调用ant命令，编译打包
	open ANTOUT, "$ant_cmd 2>&1 |";
	while(<ANTOUT>) {
		print;
	}
	close ANTOUT;

	# 将打包输出文件拷贝到指定目录
	#system("$copy_cmd sd sd");
}
