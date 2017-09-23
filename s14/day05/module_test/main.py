# __author__ = "sun wang"
# #import  module_alex
# #from module_alex import *
# from module_alex import logger as logger_alex
import sys,os
print(sys.path)
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
import module_alex
print (module_alex.name)
# #say_hello()
#
# def logger():
#      print ("in the main")
#
# logger_alex()
# logger()
