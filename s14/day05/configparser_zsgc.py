__author__ = "sun wang"
import configparser

config = configparser.ConfigParser()
config.read('i.cfg')

# ########## 读 ##########
# secs = config.sections()
# print (secs)
# options = config.options("section1")
# print (options)
#
# item_list = config.items('section2')
# print (item_list)
# #
# val = config.get('section1','k1')
# print(val)
# val = config.getint('section1','k3')
# print(val)
#改写
# sec = config.remove_section('section1')
# config.write(open('i2.cfg',"w"))

# sec = config.has_section('alex')
# print(sec)
# sec = config.add_section("alex")
# config.write(open('i.cfg','w'))

# config.set('alex','k1','1000')
# config.write(open('i2.cfg','w'))

config.remove_option('alex','k1')
config.write(open('i2.cfg','w'))