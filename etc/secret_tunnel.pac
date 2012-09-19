/*
 * version 0.8
 * 2012年 09月 19日 星期三 14:03:00 CST
 * file:///home/yaoms/myHomeConfs/etc/secret_tunnel.pac
 */
function FindProxyForURL(url, host) {
  var PROXY = "SOCKS5 127.0.0.1:7070"; // autossh 开辟的秘密通道
  var HTTP_PROXY = "PROXY 127.0.0.1:8088"; // autossh 开辟的秘密通道
  var DEFAULT = "DIRECT";

  if(/google\.com/i.test(url)) return PROXY; // Google 谷歌
  if(/googleusercontent\.com/i.test(url)) return PROXY; // Google+ 上的用户产生内容
  if(/gstatic\.com/i.test(url)) return PROXY; // Google 静态文件域
  if(/blogspot\.com/i.test(url)) return PROXY; // Google Blog
  if(/bloger\.com/i.test(url)) return PROXY; // Google Bloger
  if(/youtube\.com/i.test(url)) return PROXY; // Youtube (Google Video)
  if(/ytimg\.com/i.test(url)) return PROXY; // Youtube 的图片资源服务器
  if(/wikipedia\.org/i.test(url)) return PROXY; // 维基百科
  if(/appspot\.com/i.test(url)) return PROXY; // Google app engine

  //if(/ip138\.com/i.test(url)) return PROXY;

  return DEFAULT;
}
