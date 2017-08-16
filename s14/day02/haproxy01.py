#!/usr/bin/python
#Author:xiaojie
# -*- coding:utf-8 -*-
import json
import os

def fetch(data):
    ###www.oldboy.org
    #print("\033[35m配置存在将输出,'不存在无输出,请重新选择'\033[0m")
    #print(data2)
    with open('haproxy', 'r', encoding='utf-8') as f:
        for line in f:
            i = line.strip('\n')
            # print(i)
            if data in i:
                print(i)###backend www.oldboy.org
                print(f.readline())  ##记录
            else:
                #print("\033[35m配置存在将输出,'不存在无输出,请重新选择'\033[0m")
                continue


#增加去重未完成
def add(data):
    '''data={'record': {'maxconn': '3000', 'weight': '20', 'server': '100.1.7.9'}, 'backend': 'www.oldboy.org'}'''
    backend = data["backend"]  ##www.oldboy.org
    #record = data["record"]  ##{'maxconn': '3000', 'weight': '20', 'server': '100.1.7.9'}
    #record = data['record']['server'],data['record']['server'],data['record']['weight'],data['record']['maxconn']
    # print(backend) www.baidu.com
    #print(record) ('192.168.1.1', '192.168.1.1', '20', '3000')

    record = "server %s %s weight %s maxconn %s" %(data['record']['server'],data['record']['server'],data['record']['weight'],data['record']['maxconn'])

    record1 = ''.join(record)
    #print(record1)
    with open('haproxy','r+',encoding='utf-8') as f:
        f.seek(0,2)
        f.write('\nbackend ' + backend +'\n')
        f.write('\t\t' + record1)


def remove(data):
    #print(data){'backend': 'www.baidu.com', 'record': {'server': '100.1.7.9', 'maxconn': '3000', 'weight': '20'}}
    backend = data["backend"]
    record = "server %s %s weight %s maxconn %s" % (data['record']['server'], data['record']['server'], data['record']['weight'], data['record']['maxconn'])
    record1 = ''.join(record)
    #print(backend)  #www.baidu.com
    #print(record1)
    record2 = '\t\t' + record1
    #print(record2)
    record3 = 'backend ' + backend + ' ' + record2
    record3 = ''.join(record3)

    f= open('haproxy', 'r', encoding='utf-8')
    f1 = open('1111', 'w', encoding='utf-8')
    for line in f.readlines():
        #i = line.strip('\n')
        if backend not in line.strip('\n'):
            f1.write(line)
    f.close()
    f1.close()

    f = open('1111', 'r', encoding='utf-8')
    f1 = open('haproxy', 'w', encoding='utf-8')

    for line1 in f.readlines():
        if record2 not in line1.strip('\n'):
            f1.write(line1)
    f.close()
    f1.close()
    os.remove('1111')










if __name__ == '__main__':
    msg = '''
    1: 查询
    2: 添加
    3: 删除
    '''
    menu_dic={
        '1':fetch,
        '2':add,
        '3':remove,
    }
    print(msg)
    while True:
        choice = input("请选择操作1,2,3: ").strip()
        if choice == "1":
            data = input("请输入查询语句: ")##www.oldboy.org
            fetch(data)


        elif choice == "2":
            print('''语句格式{"backend":"www.oldboy6.org","record":{"server":"192.168.1.6","weight":"20","maxconn":"3000"}}''')
            data = json.loads(input("请输入语句>>> "))
            add(data)

        elif choice == "3":
            print('''语句格式{"backend":"www.oldboy6.org","record":{"server":"192.168.1.6","weight":"20","maxconn":"3000"}}''')
            data = json.loads(input("请输入语句>>> "))
            remove(data)
        else:
            print("\33[31m输入错误,请重新选择\33[0m")










