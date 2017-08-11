__author__ = "sun wang"
import sys
print (sys.getdefaultencoding())
s = "你好"
s_gb2312 = s.encode("gb2312")
print (s_gb2312)
print (type(s_gb2312))
s_gb2312_to_unicode = s_gb2312.decode("gb2312")
print (s_gb2312_to_unicode)
print (type(s_gb2312_to_unicode))
s_utf8 = s.encode("utf-8")
print (s_utf8)
print (type(s_utf8))
s_utf8_to_gbk = s_utf8.decode('utf-8').encode('gbk')
print (s_utf8_to_gbk)
print (type(s_utf8_to_gbk))

