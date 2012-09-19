/*
 * version 0.9
 * 2012年 09月 19日 星期三 13:45:21 CST
 * https://github.com/yaoms/myHomeConfs/raw/master/etc/secret_tunnel.pac
 */
function FindProxyForURL(url, host) {

  var SOCKS_PROXY = "SOCKS5 127.0.0.1:7070"; // autossh 开辟的秘密通道
  var HTTP_PROXY = "PROXY 127.0.0.1:8088";
  var DEFAULT = "DIRECT";

  if(shExpMatch(url, '*.google.com/*')) return SOCKS_PROXY; // Google 谷歌
  if(shExpMatch(url, '*.googleusercontent.com/*')) return SOCKS_PROXY; // Google+ 上的用户产生内容
  if(shExpMatch(url, '*.gstatic.com/*')) return SOCKS_PROXY; // Google 静态文件域
  if(shExpMatch(url, '*.blogspot.com/*')) return SOCKS_PROXY; // Google Blog
  if(shExpMatch(url, '*.bloger.com/*')) return SOCKS_PROXY; // Google Bloger
  if(shExpMatch(url, '*.youtube.com/*') return SOCKS_PROXY; // Youtube (Google Video)
  if(shExpMatch(url, '*.ytimg.com/*')) return SOCKS_PROXY; // Youtube 的图片资源服务器
  if(shExpMatch(url, '*.wikipedia.org/*')) return SOCKS_PROXY; // 维基百科
  if(shExpMatch(url, '*.appspot.com/*') return SOCKS_PROXY; // Google app engine

  if(shExpMatch(url, '*.ip138.com/*')) return SOCKS_PROXY;

  //if(/101\.47\.94\.107/.test(url)) return HTTP_PROXY;


  return DEFAULT;
}
