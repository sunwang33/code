__author__ = "sun wang"
import hashlib

m = hashlib.md5()
m.update(b"Hello")
print(m.hexdigest())
m.update(b"It's me")
print(m.hexdigest())
m2 = hashlib.md5()
m2.update(b"HelloIt's me")
print(m2.hexdigest())
m.update(b"It's been a long time since last time we ...")
print(m.digest())  # 2进制格式hash
print(m.hexdigest())
print(len(m.hexdigest()))  # 16进制格式hash