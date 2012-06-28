#!/usr/bin/env python
# coding: utf8
from urllib2 import urlopen
from urllib import urlencode
import simplejson
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

from bs4 import BeautifulSoup

# http://dict.youdao.com/search?ue=utf8&q=good
# http://fanyi.youdao.com/translate?type=AUTO&i=my%20name%20is%20yao&keyfrom=dict.top
# http://fanyi.youdao.com/openapi.do?keyfrom=<keyfrom>&key=<key>&type=data&doctype=<doctype>&version=1.1&q=要翻译的文本

# 版本：1.1，请求方式：get，编码方式：utf-8
# 主要功能：中英互译，同时获得有道翻译结果和有道词典结果（可能没有）
# 参数说明：
# 　type - 返回结果的类型，固定为data
# 　doctype - 返回结果的数据格式，xml或json或jsonp
# 　version - 版本，当前最新版本为1.1
# 　q - 要翻译的文本，不能超过200个字符，需要使用utf-8编码
# errorCode：
# 　0 - 正常
# 　20 - 要翻译的文本过长
# 　30 - 无法进行有效的翻译
# 　40 - 不支持的语言类型
# 　50 - 无效的key

# 有道翻译 fanyi@noreply.youdao.com
#
# 发送至 我 
# 尊敬的用户：
# 
# 您刚刚在有道翻译API官网上申请了API key，请妥善保管。 
# 
# 网站名称：yaoms-trans-bot 
# 网站地址：http://yaoms.blogspot.com 
# 网站说明：个人博客使用 
# 联系方式：yms541@gmail.com 
#
# 您的key：780445278 
# 您的keyfrom：yaoms-trans-bot

error = {"0":"正常", "20":"要翻译的文本过长", "30":"无法进行有效的翻译", "40":"不支持的语言类型", "50":"无效的key"}

def trans(words):
    base_url='http://fanyi.youdao.com/openapi.do?'
    params=urlencode( (('keyfrom','yaoms-trans-bot'), ('key', '780445278'), ('type', 'data'), ('doctype', 'xml'), ('version', '1.1'), ('q', words) ) )
    url=base_url+params
    response=urlopen(url)
    xml = response.read().decode('utf8')
    soup = BeautifulSoup(xml, features="xml")
    errorCode = '0'
    if soup.errorCode:
        errorCode = soup.errorCode.get_text()
    if errorCode=='0':
        # 成功
        if soup.basic and soup.basic.explains:
            return "\n".join([ i.get_text() for i in soup.basic.explains.find_all('ex') if i and len(i.get_text().strip())])
        elif soup.translation:
            return "\n".join([ i.get_text() for i in soup.translation.find_all('paragraph') if i and len(i.get_text().strip())])
        else:
            return None
    else:
        # 失败
        return "Error: %s" % error[errorCode]

if __name__ == '__main__':
    words=' '.join(sys.argv[1:])
    print trans(words)
