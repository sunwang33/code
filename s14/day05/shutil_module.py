__author__ = "sun wang"
import shutil
# f1 = open("p_test.py",'r',encoding="utf-8")
# f2 = open("shutil测试",'w',encoding="utf-8")
# shutil.copyfileobj(f1,f2)
# shutil.copyfile("shutil测试1","shutil测试2")
# shutil.copystat("shutil测试1","shutil测试2")
# shutil.copytree("test4","new_test4")
# shutil.rmtree("new_test4")
# shutil.make_archive("shutil_archive_test","zip","D:\git\s14\day05")
# import zipfile
# # z = zipfile.ZipFile('laxi.zip','w')
# # z.write("p_test.py")
# # z.write("test4")
# # z.close()
# z=zipfile.ZipFile('laxi.zip','r')
# z.extractall('D:/git/s14/day04/')
# z.close
import tarfile,sys,shutil
# print(sys.path)
# shutil.copy("laxi.zip","laxi2.zip")
# tar = tarfile.open('your.tar','w')
# tar.add("D:\git\s14\day05\laxi.zip",arcname='laxi.zip')
# tar.close()
tar = tarfile.open("your.tar",'r')
tar.extractall("D:\git\s14\day04")
tar.close()

