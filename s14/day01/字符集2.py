# Author:Sun Wang
import sys
print(sys.getdefaultencoding())


msg = "我爱北京天安门"
#msg_gb2312 = msg.decode("utf-8").encode("gb2312")
msg_gb2312 = msg.encode("gb2312") #默认就是unicode,不用再decode,喜大普奔
gb2312_to_unicode = msg_gb2312.decode("gb2312")
gb2312_to_utf8 = msg_gb2312.decode("gb2312").encode("utf-8")

print(msg)
print(msg_gb2312)
print(gb2312_to_unicode)
print(gb2312_to_utf8)