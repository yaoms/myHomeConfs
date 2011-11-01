# encoding: utf-8
from dbi_getdbhandle import dbi_getdbhandle
from confirm_ask import confirm_ask
# get db handle
dbh = dbi_getdbhandle()
cur = dbh.cursor()

# quest for resid
print u"请输入要删除的资源ID：",
resid = int(raw_input())

# get and show res info, reconfirm
cur.execute(u'SELECT RES_NAME,RES_AUTHOR,RES_DATE FROM ZZB_RES_INFO WHERE RES_ID=:resid',{'resid':resid})
resinfo = cur.fetchone()
print "%s\t%s\t%s" % resinfo
if not confirm_ask(u'是否继续？'):
    cur.close()
    dbh.commit()
    import sys
    sys.exit(0)

# del from zzb_res_info
print "删除 %d 相关的资源信息..." % resid
cur.execute(u'DELETE FROM ZZB_RES_INFO WHERE RES_ID=:resid',{'resid':resid})
if cur.rowcount:
    print "已删除 %d 条记录。\n" % cur.rowcount
else:
    print "未删除任何记录。\n"

## del previews
# del from zzb_res_url
print "删除 %d 相关的文件信息..." % resid
cur.execute(u'DELETE FROM ZZB_RES_URL WHERE RES_ID=:resid',{'resid':resid})
if cur.rowcount:
    print "已删除 %d 条记录。\n" % cur.rowcount
else:
    print "未删除任何记录。\n"

## del files
# del from wap_catalog_relation
print "删除 %d 相关的分类信息..." % resid
cur.execute(u'DELETE FROM wap_catalog_relation WHERE RES_ID=:resid',{'resid':resid})
if cur.rowcount:
    print "已删除 %d 条记录。\n" % cur.rowcount
else:
    print "未删除任何记录。\n"

# del from holpe_recommend_product
print "删除 %d 相关的推荐信息..." % resid
cur.execute(u'DELETE FROM holpe_recommend_product WHERE RES_ID=:resid',{'resid':resid})
if cur.rowcount:
    print "已删除 %d 条记录。\n" % cur.rowcount
else:
    print "未删除任何记录。\n"

# finish
cur.close()
dbh.commit()
