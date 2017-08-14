# Author:Sun Wang
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
exit_flag = False
while not exit_flag :
    for item in menu:
        print (item)
    choise = input("Please input your choise: ")
    if choise in menu:
        while not exit_flag:
            for i in menu[choise]:
                print ("\t",i)
            choise1 = input("Please input your choise1: ")
            if choise1 in menu[choise]:
                while not exit_flag:
                    for i1 in menu[choise][choise1]:
                        print ("\t",i1)
                    choise2 = input("Please input your choise2: ")
                    if choise2 in menu[choise][choise1]:
                        while not exit_flag:
                            for i2 in menu[choise][choise1][choise2]:
                                print ("\t\t",i2)
                            choise3 = input("Please input your choise3: ")
                            if choise3 in menu[choise][choise1][choise2]:
                                while not exit_flag:
                                    for i3 in menu[choise][choise1][choise2][choise3]:
                                        print ("\t\t\t",i3)
                                    if choise3 == 'q':
                                        exit_flag = True
                                    elif choise3 == 'b':
                                        break
                            if choise2 == 'b':
                                break
                    if choise1 == 'b':
                        break
            if choise == 'b':
                break




