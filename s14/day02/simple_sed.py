__author__ = "sun wang"
#简单实现sed替换功能。
import sys
with open("yesterday2",'r',encoding="utf-8") as f , \
    open("yesterday02",'w',encoding="utf-8") as f_new:
    word1 = sys.argv[1]
    word2 = sys.argv[-1]+"\n"
    for line in f:
        if word1 in line :
            line = word2
        f_new.write(line)



