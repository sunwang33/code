# Author:Sun Wang
import  sys
print (sys.getdefaultencoding())
msg = '我爱洗澡'
msg_gb2312=msg.encode('gb2312')
print (msg_gb2312)
msg_gb2312_to_unicode=msg_gb2312.decode('gb2312')
print(msg_gb2312_to_unicode)
msg_gb2312_to_utf8=msg_gb2312.decode('gb2312').encode("utf-8")
print(msg_gb2312_to_utf8)