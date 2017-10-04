__author__ = "sun wang"
import configparser
conf = configparser.ConfigParser()
conf.read("example.ini")

print(conf.sections())
print(conf.defaults())

print(conf['bitbucket.org']['user'])
#改写
sec = conf.remove_section('bitbucket.org')
conf.write(open('example1.ini', 'w'))