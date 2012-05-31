#!/bin/sh
# Mysql 自动备份脚本 完整备份
# 作者：yaoms
# 日期：2011年 09月 15日 星期四 10:05:56 CST
#
# 脚本运行需要 mysqldump 工具
# 如果异地备份，则需要一个配置好的 ftp 服务器
# 可以将本脚本加入到 crontab 进行管理
#
# 如需 增量备份，启用数据库的 log_bin 模式，每天备份 `uname -n`-bin.xxxx
# 恢复时，按照时间顺序导入即可 bin log 文件需要使用 mysqlbinlog 工具处理
#
# 更多备份方案参考：http://blog.sina.com.cn/s/blog_4e424e2101000c1x.html

##########################
#
#  配置部分
#
##########################

# 数据库主机IP
DB_HOST=127.0.0.1

# 数据库监听端口
DB_PORT=3306

# 数据库备份用户和密码
DB_USER=root
DB_PASS=password

# 数据库备份工具 mysqldump 的绝对路径
DB_DUMPER=/usr/bin/mysqldump

# 要备份的数据库
DB_NAMES="test2 test3"

# 备份工作目录
BACKUP_WORKDIR=/tmp

# 备份文件名前缀
DB_FILE_PREFIX=mysql_backup_for_

# 备份文件名后缀
DB_FILE_POSTFIX=_`date +%Y%m%d`.sql

# 压缩文件前缀
DB_ARCH_PREFIX=mysql_backup

# 是否上传？0 不， 1 是
AUTO_UPLOAD=0

# 上传ftp服务器
UPLOAD_HOST=127.0.0.1
UPLOAD_PORT=21
UPLOAD_USER=dbbackup
UPLOAD_PASS=123456
UPLOAD_PATH=/mysql/backup

# 是否清除工作文件？0 不， 1 是
AUTO_CLEAN=0


##########################
#
#  备份部分
#
##########################

cd $BACKUP_WORKDIR

for database in $DB_NAMES
do echo "backup mysql database $database: "
$DB_DUMPER --verbose --host=$DB_HOST --port=$DB_PORT --user=$DB_USER \
              --password=$DB_PASS $database > $DB_FILE_PREFIX$database$DB_FILE_POSTFIX
done


##########################
#
#  压缩部分
#
##########################

tar -cvjf $DB_ARCH_PREFIX$DB_FILE_POSTFIX.tar.bz2 *$DB_FILE_POSTFIX

##########################
#
#  上传部分 自动上传压缩包
#
##########################

if [ $AUTO_UPLOAD -eq 1 ]
then
echo "open $UPLOAD_HOST $UPLOAD_PORT
      user $UPLOAD_USER $UPLOAD_PASS
      binary
      cd $UPLOAD_PATH
      prompt off
      mput $DB_ARCH_PREFIX$DB_FILE_POSTFIX.tar.bz2
      printf "\n"
      close
      bye" | ftp -i -n
fi

##########################
#
#  清理部分
#
##########################

if [ $AUTO_CLEAN -eq 1 ]
then
    rm -vf *$DB_FILE_POSTFIX*
fi
