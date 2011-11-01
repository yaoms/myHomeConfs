# coding: utf-8
import mysite.settings

from mysite.book import helper

def init():
	#init book catalogs
	catalog_names = [
			'玄幻',
			'魔法',
			'穿越',
			'架空',
			'言情',
			'耽美',
			'灵异',
			'侦探',
			'游戏',
			'动漫',
			'都市',
			'生活',
			'武侠',
			'仙侠',
			'科幻',
			'未来',
			'军事',
			'历史',
	]
	print "共需导入 %d 条数据。" % len(catalog_names)
	for catalog_name in catalog_names:
		catalog= helper.getNewCatalog(catalog_name)
		catalog.save()
		print "已导入分类：%s" % catalog_name
	print "导入完毕。"
	#init book styles
	style_names = [
			'悲剧',
			'正剧',
			'轻松',
			'爆笑',
			'暗黑',
	]
	print "共需导入 %d 条数据。" % len(style_names)
	for style_name in style_names:
		style= helper.getNewStyle(style_name)
		style.save()
		print "已导入分类：%s" % style_name
	print "导入完毕。"

if __name__ == "__main__":
	init()
