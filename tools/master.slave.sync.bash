#!/bin/bash
# master.slave.sync.bash
# 导出要主从复制的数据库并记录 log-bin 和 pos 等信息

# 主数据库和从数据库都必须可以使用如下命令登录管理
MYSQL_CLI="mysql --default-character-set=utf8 -uroot"
MYSQL_DUMP_CLI="mysqldump --default-character-set=utf8 -uroot --databases douwan3 douwan3android"

cat >master.slave.start.bash<<EOF
#!/bin/bash
# master.slave.start.bash
# 将主数据库导出的数据导入从数据库
echo stop slave
echo "stop slave;" | $MYSQL_CLI
echo import data to slave db
bzcat master.dump.sql.bz2 | $MYSQL_CLI
echo change master ...
cat master.slave.sync.info | $MYSQL_CLI
echo start slave
echo "start slave;" | $MYSQL_CLI
echo fetch slave status
echo "show slave status\G" | $MYSQL_CLI
EOF
chmod +x master.slave.start.bash

# 从服务器都可以使用当前系统用户同过ssh管理，配置公钥认证
SLAVES="dw-mysql2"

echo lock master db tables
echo 'FLUSH TABLES WITH READ LOCK' | $MYSQL_CLI
echo dump master db to master.dump.sql.bz2
$MYSQL_DUMP_CLI | bzip2 > master.dump.sql.bz2
echo fetch master status
echo 'show master status' | $MYSQL_CLI | tail -1 | xargs printf "change master to master_log_file='%s', master_log_pos=%s;\n" > master.slave.sync.info
echo unlock master db tables
echo 'UNLOCK TABLES' | $MYSQL_CLI

echo send to slaves
for h in $SLAVES
do
    echo scp to $h
    scp master.dump.sql.bz2 master.slave.sync.info master.slave.start.bash $h:
    echo apply to $h
    ssh $h "bash master.slave.start.bash"
done
