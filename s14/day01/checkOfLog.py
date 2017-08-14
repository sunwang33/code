# Author:Sun Wang
f = open("20170713.log","r+",encoding="utf-8")
for i in f.readlines():
    data = i.split("%")[0].split(" ")[-1]

    if data.isnumeric():
        data = int(data)
        if data > 50:
            print(data)
    """
    if data.isdigit():
        print (data)
       
        data = int(data.strip())
        
        if data > 90:
            ip_addr = data.split(":")[0]
            print (ip_addr)
"""
