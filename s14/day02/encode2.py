__author__ = "sun wang"

s = "你哈"
s_gbk = s.encode("gbk")

print(s)
print(s.encode())
#gbk转成utf8
gbk_to_utf8 = s_gbk.decode("gbk").encode("utf-8")
print ("utf8",gbk_to_utf8)