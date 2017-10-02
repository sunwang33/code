# # # __author__ = "sun wang"
# # # import sys
# # # # #print(sys.argv)
# # # # print(sys.platform)
# # # # import time
# # # # for i in range(100):
# # # #     sys.stdout.write('\r%s' %('#' * i))
# # # #     sys.stdout.flush()
# # # #     time.sleep(0.5)
# # import sys,time
# # for i in range(100):
# #     time.sleep(0.5)
# #     print('\r%s' %('# '* i),end='',file=sys.stdout,flush=True)
# import sys
# import time
# def progress(percent,width=50):
#     if percent >= 100:
#         percent=100
#
#     show_str=('[%%-%ds]' %width) %(int(width * percent / 100) * "#") #字符串拼接的嵌套使用
#     print("\r%s %d%%" %(show_str, percent),end='',file=sys.stdout,flush=True)
#
# progress(60,width=50)

data_size=3030333
recv_size=0
while recv_size < data_size:
    time.sleep(0.001) #模拟数据的传输延迟
    recv_size+=1024 #每次收1024

    recv_per=int(100*(recv_size/data_size)) #接收的比例
    progress(recv_per,width=30) #进度条的宽度30