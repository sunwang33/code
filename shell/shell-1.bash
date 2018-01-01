shell脚本介绍

内容概要：
1. shell脚本是什么
它是一种脚本语言，并非编程语言
可以使用一些逻辑判断、循环等语法
可以自定义子函数
是系统命令的集合
shell脚本可以实现自动化运维，大大增加我们的工作效率

2. shell脚本结构以及执行方法
EG:
#mkdir -pv shell

#cd shell/
#vim first.sh

#!/bin/bash
##The first test shell  script .
##Writen by aming.
ls /tmp
echo "This is the first script."

:wq!

#chmod a+x first.sh
方法一：
#./first.sh
方法二（用绝对路径去执行）：
# /root/shell/first.sh 

方法三：
#sh  first.sh
**********************************************************************************************
[root@sunlocalhost shell]# ll  /bin/bash
-rwxr-xr-x. 1 root root 868692 7月  18 2013 /bin/bash
[root@sunlocalhost shell]# ll  /bin/sh
lrwxrwxrwx. 1 root root 4 11月 11 03:28 /bin/sh -> bash
//sh是bash的软连接。
***********************************************************************************************
#sh -x  first.sh

+ ls /tmp
12                           aminglinux.txt     pear                  test01                  yum.log
123                          from131to117.pcap  pulse-eedUOms49RfZ    test01.txt              yum_save_tx-2015-11-29-22-13eWvFng.yumtx
145.107.pcap                 map_pid            pulse-r0Vmk5PGGXAj    test02                  yum_save_tx-2015-11-29-22-23EiI96V.yumtx
1.ipt                        mysql2.sock        rsync                 +=_$.txt                yum_save_tx-2015-12-19-23-23Dnd6pE.yumtx
1.txt                        mysqld2.bak        rsync123              vmware-config0          yum_save_tx-2016-02-26-22-315VrBg9.yumtx
2.txt                        mysql.sock         sedfrom131to117.pcap  VMwareDnD               yum_save_tx-2016-03-14-23-15PU_VXW.yumtx
322                          new001.txt         snake_2015-12-01.sh   vmware-root             yum_save_tx-2016-04-02-17-19b4jnlb.yumtx
3.txt                        option_pid         sumwangtest.txt       vmware-root-4289509216
70-persistent-net.rules.bak  passwd             test001               xaa
+ echo 'This is the first script.'
This is the first script.
//查看脚本执行过程。
开头行指定bash路径: #! /bin/bash
以#开头的行作为解释说明
脚本的名字以.sh结尾，用于区分这是一个shell脚本
执行方式有两种：chmod +x 1.sh; ./1.sh 如果没有执行权限可以 bash 1.sh 
bash -x 1.sh 可以查看脚本执行过程

3. 学会date命令的用法

# date
2016年 04月 05日 星期二 22:12:38 CST
[root@sunlocalhost ~]# cal
      四月 2016     
日 一 二 三 四 五 六
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29 30

[root@sunlocalhost ~]# cal -y
                               2016                               

        一月                   二月                   三月        
日 一 二 三 四 五 六   日 一 二 三 四 五 六   日 一 二 三 四 五 六
                1  2       1  2  3  4  5  6          1  2  3  4  5
 3  4  5  6  7  8  9    7  8  9 10 11 12 13    6  7  8  9 10 11 12
10 11 12 13 14 15 16   14 15 16 17 18 19 20   13 14 15 16 17 18 19
17 18 19 20 21 22 23   21 22 23 24 25 26 27   20 21 22 23 24 25 26
24 25 26 27 28 29 30   28 29                  27 28 29 30 31
31
        四月                   五月                   六月        
日 一 二 三 四 五 六   日 一 二 三 四 五 六   日 一 二 三 四 五 六
                1  2    1  2  3  4  5  6  7             1  2  3  4
 3  4  5  6  7  8  9    8  9 10 11 12 13 14    5  6  7  8  9 10 11
10 11 12 13 14 15 16   15 16 17 18 19 20 21   12 13 14 15 16 17 18
17 18 19 20 21 22 23   22 23 24 25 26 27 28   19 20 21 22 23 24 25
24 25 26 27 28 29 30   29 30 31               26 27 28 29 30

        七月                   八月                   九月        
日 一 二 三 四 五 六   日 一 二 三 四 五 六   日 一 二 三 四 五 六
                1  2       1  2  3  4  5  6                1  2  3
 3  4  5  6  7  8  9    7  8  9 10 11 12 13    4  5  6  7  8  9 10
10 11 12 13 14 15 16   14 15 16 17 18 19 20   11 12 13 14 15 16 17
17 18 19 20 21 22 23   21 22 23 24 25 26 27   18 19 20 21 22 23 24
24 25 26 27 28 29 30   28 29 30 31            25 26 27 28 29 30
31
        十月                  十一月                 十二月       
日 一 二 三 四 五 六   日 一 二 三 四 五 六   日 一 二 三 四 五 六
                   1          1  2  3  4  5                1  2  3
 2  3  4  5  6  7  8    6  7  8  9 10 11 12    4  5  6  7  8  9 10
 9 10 11 12 13 14 15   13 14 15 16 17 18 19   11 12 13 14 15 16 17
16 17 18 19 20 21 22   20 21 22 23 24 25 26   18 19 20 21 22 23 24
23 24 25 26 27 28 29   27 28 29 30            25 26 27 28 29 30 31
30 31

[root@sunlocalhost ~]# date
2016年 04月 05日 星期二 22:16:00 CST
[root@sunlocalhost ~]# date -s "2016-04-05 22:16:60"
date: 无效的日期"2016-04-05 22:16:60"
[root@sunlocalhost ~]# date -s "2016-04-05 22:16:50"
2016年 04月 05日 星期二 22:16:50 CST
[root@sunlocalhost ~]# date
2016年 04月 05日 星期二 22:16:55 CS

# yum -y install ntp

#ntpdate  时间服务器
EG:ntpdate   time.windows.com

#  ntpdate ntp.api.bz 
 5 Apr 22:31:26 ntpdate[21330]: step time server 61.153.197.226 offset 2.441799 sec
 
# date +%F
2016-04-05
# date +%T
22:35:40
# date +%Y
2016
# date +%y
16
# date +%m
04
# date +%d
05
]# date +%H
22
# date +%M
38
# date +%S
21

# date +%s            #时间戳
1459867238
# date -d @1459867238
2016年 04月 05日 星期二 22:40:38 CST

# date +"%Y-%m-%d %H:%M:%S"
2016-04-05 22:49:22

# date -d "-2 days" +%F
2016-04-03

# date -d "-2 month" +%F
2016-02-05

# date -d "-2 hour" +%T
20:54:38

# date -d  "-2  min" +%T
22:53:33

# date -d "-2 sec"  +%T
22:56:28

# date +%w        //显示周几，周日会显示成0。
2
# date +%W        //显示今年的第多少周。
14

#touch  `date +%F.log`
//用日期作为文件名。



*************************************************************
date  +%Y-%m-%d, date +%y-%m-%d 年月日
date  +%H:%M:%S = date +%T 时间
date +%s  时间戳
date -d @1434248742
date -d "+1day"一天后date -d "-1day"一天前
date -d  "-1month" 一月前
date -d  “-1min” 一分钟前
date +%w, date +%W 星期
***************************************************************
4. shell自定义变量

#echo $PATH $HOME $PWD
//以上是系统内置的变量。

[root@sunlocalhost ~]# a=1
[root@sunlocalhost ~]# echo $a
1
[root@sunlocalhost ~]# b=2
[root@sunlocalhost ~]# echo $b
2

#可以用数字、字母、下划线组成变量，但是变量不能以数字开头。

EG:
[root@sunlocalhost ~]# 1A=1
-bash: 1A=1: command not found

[root@sunlocalhost ~]# a_1=1
[root@sunlocalhost ~]# echo $a_1
1

#注意等号两边不能有空格.(PHP允许)

[root@sunlocalhost ~]# a_1 = 2
-bash: a_1: command not found

#写一个和用户交互的脚本。

#vim  2.sh

#!/bin/bash
##This  is  second scripts.
##writen by  aming.
read -p "please input a number:" number   #read是一个和用户交互的命令。
echo $number

:wq!

#chmod 700 !$

#./2.sh

#please input a number:2
2

[root@sunlocalhost sbin]# ./2.sh
please input a number:sdfghjk
sdfghjk

#为了防止用户长时间不输入数字，给脚本加个定时。
#vim 2.sh
#!/bin/bash
##This  is  second scripts.
##writen by  aming.
read -t 10 -p "please input a number:" number   #加一个-t选项，10代表10秒。
echo $number

:wq!

# 变量$1 $2 $0.
#$0表示脚本的名字。
#vim  3.sh

#!/bin/bash
##This  is  third scripts.
##writen by  aming.

echo "\$1=$1"       #注意反斜杠，如果加脱义符的话，会认为$1就是$1，$1是一个变量值,而不是认为$1是一个变量名。
echo "\$2=$2"
echo "\$0=$0"
echo "\$3=$3"
:wq!

[root@sunlocalhost sbin]# sh 3.sh
$1=
$2=
$0=3.sh
$3=

[root@sunlocalhost sbin]# sh 3.sh  aa 11  dd
$1=aa
$2=11
$0=3.sh
$3=dd

[root@sunlocalhost sbin]# sh 3.sh  aa 11
$1=aa
$2=11
$0=3.sh
$3=

#用变量进行数学运算：
[root@sunlocalhost sbin]# a=1;b=2
[root@sunlocalhost sbin]# c=$[$a+$b]
[root@sunlocalhost sbin]# echo $c
3

#变量$#表示所有变量的个数。
[root@sunlocalhost sbin]# vim 3.sh
#!/bin/bash
##This  is  third scripts.
##writen by  aming.
echo "\$1=$1"
echo "\$2=$2"
echo "\$0=$0"
echo "\$3=$3"
echo "\$#=$#"
:wq!

[root@sunlocalhost sbin]# sh !$ aa bb cc
sh 3.sh aa bb cc
$1=aa
$2=bb
$0=3.sh
$3=cc
$#=3

补充：
当脚本中使用某个字符串较频繁并且字符串长度很长时就应该使用变量代替
使用条件语句时，常常使用变量    if [ $a -gt 1 ]; then ... ; fi
引用某个命令的结果时，用变量替代   n=`wc -l 1.txt`
写和用户交互的脚本时，变量也是必不可少的  read -p "Input a number: " n; echo $n   如果没写这个n，可以直接使用$REPLY
内置变量 $0, $1, $2…    $0表示脚本本身，$1 第一个参数，$2 第二个 ....       $#表示参数个数
数学运算a=1;b=2; c=$(($a+$b))或者$[$a+$b]

5. if逻辑判断

#vim   if.sh
#!/bin/bash

a=5
if [ $a -gt 3 ]
then 
     echo "a>3"
fi

:wq!

[root@sunlocalhost sbin]# sh if.sh 
a>3

#符号表示方法。
>:-gt
<:-lt
==:-eq
!=:-ne
>=:-ge
<=:-le

#vim   if2.sh
#!/bin/bash

a=5
if [ $a -gt 10 ]
then 
     echo "a>10"
else
     echo "a<10"
fi

:wq!

[root@sunlocalhost sbin]# ./!$
./if2.sh
a<10

vim if3.sh
	 
#!/bin/bash

a=5
if [ $a -gt 10 ]
then 
     echo "a>10"
elif [ $a -lt 4 ]
then
     echo "a<4"
else
     echo "4<a<10"
fi

:wq!

[root@sunlocalhost sbin]# chmod 700 !$
chmod 700 if3.sh
[root@sunlocalhost sbin]# ./!$
./if3.sh
4<a<10

补充：
格式1：if 条件 ; then 语句; fi
格式2：if 条件; then 语句; else 语句; fi
格式3：if …; then … ;elif …; then …; else …; fi
逻辑判断表达式：if [ $a -gt $b ]; if [ $a -lt 5 ]; if [ $b -eq 10 ]等 -gt (>); -lt(<); -ge(>=); -le(<=);-eq(==); -ne(!=) 注意到处都是空格
可以使用 && || 结合多个条件

6. if判断的几种用法：
#判断1.txt是否是一个文件。
if [ -f 1.txt ]; then echo ok; fi

EG:
[root@sunlocalhost sbin]# if [ -f 1.txt ]; then echo ok; fi
ok
[root@sunlocalhost sbin]# if [ -f /tmp/1.txt ]; then echo ok; fi
ok

#判断1.txt是否是一个目录。
if [ -d 1.txt ]; then echo ok; fi
EG:
[root@sunlocalhost sbin]# if [ -d /tmp/ ]; then echo ok; fi
ok
#判断1.txt是否是可读。
if [ -r 1.txt ]; then echo ok; fi

#判断1.txt是否是可写。
if [ -w 1.txt ]; then echo ok; fi

#判断1.txt是否是可执行。
if [ -x 1.txt ]; then echo ok; fi

EG:
[root@sunlocalhost sbin]# if [ -r 1.txt ]; then echo ok; fi
ok
[root@sunlocalhost sbin]# if [ -w 1.txt ]; then echo ok; fi
ok
[root@sunlocalhost sbin]# if [ -x 1.txt ]; then echo ok; fi
××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
补充：
[ -f file ]判断是否是普通文件，且存在 
[ -d file ] 判断是否是目录，且存在
[ -e file ] 判断文件或目录是否存在
[ -r file ] 判断文件是否可读
[ -w file ] 判断文件是否可写
[ -x file ] 判断文件是否可执行
[ -z  $a ]代表的是该变量是否有值。变量为空，则为真。
×××××××××××××××××××××××××××××××××××××××××××××××××××××××××
#判断字符串是否不为空，若不为空，则条件成立。
#vim if22.sh

#!/bin/bash
read -p "Please input a number:" n
m=`echo $n|sed 's/[0-9]//g'`
if [ -n "$m" ]                    #判断字符串是否不为空，若不为空，则条件成立。
then  
    echo "The character you input is not a number,please retry."
else
    echo  $n
fi

:wq!
#在编写If语句的时候要注意空格。
[root@sunlocalhost sbin]# ./!$
./././if22.sh
Please input a number:asd
The character you input is not a number,please retry.
[root@sunlocalhost sbin]# ./if22.sh
Please input a number:123
123
[root@sunlocalhost sbin]# ./if22.sh
Please input a number:123asd
The character you input is not a number,please retry.	
#判断字符串是否为空，若为空，则条件成立。
#vim if33.sh

#!/bin/bash
read -p "Please input a number:" n
m=`echo $n|sed 's/[0-9]//g'`
if [ -z "$m" ]                    #判断字符串是否为空，若为空，则条件成立。
then  
    echo $n
else
    echo "The character you input is not a number,please retry."
fi

:wq!

[root@sunlocalhost sbin]# chmod 700 !$
chmod 700 if33.sh
[root@sunlocalhost sbin]# ./!$
./if33.sh
Please input a number:asd123
The character you input is not a number,please retry.
[root@sunlocalhost sbin]# ./if33.sh
Please input a number:123
123

#判断文本中是否有某个关键字。
grep '^aming:' /etc/passwd    #通常我们采用这条命令去判断。

#if  grep -q '^aming:' /etc/passwd ；then echo "aming exist.";fi           //-q选项，只判断结果，但不输出结果。

EG:
[root@sunlocalhost sbin]# if  grep -q '^aming:' /etc/passwd ; then echo "aming exist." ;fi

#采用多个判断条件：
#if [ -d /tmp/ ] && [ -f 1.txt ]; then echo ok ; fi

EG:
[root@sunlocalhost sbin]# if [ -d /tmp/ ] && [ -f 1.txt ]; then echo ok ; fi
ok
[root@sunlocalhost sbin]#rm -rf 1.txt
[root@sunlocalhost sbin]# if [ -d /tmp/ ] && [ -f 1.txt ]; then echo ok ; fi
[root@sunlocalhost sbin]# 
[root@sunlocalhost sbin]# if [ -d /tmp/ ] || [ -f 1.txt ]; then echo ok ; fi
ok
[root@sunlocalhost sbin]# if [ -d /tmp/  -o  -f 1.txt ]; then echo ok ; fi
//-o选项就是OR的意思。
[root@sunlocalhost sbin]# if [ -d /tmp/  -a  -f 1.txt ]; then echo ok ; fi
//-a选项就是AND的意思。

补充：
> 表示正确输出
2> 表示错误输出
&1 表示前面 > 后面的文件。 
比如： cat 1.txt > /tmp/1.log 2>&1 
这样会把正确和错误的日志全部输入到/tmp/1.log

1.7case选择
EG:
case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;                         #以两个分号结束。
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart)
        $1
        ;;
    reload)
        rh_status_q || exit 7
        $1
        ;;
    force-reload)
        force_reload
        ;;
    status)
        rh_status
        ;;
    condrestart|try-restart)
        rh_status_q || exit 0
        restart
        ;;
    *)	                           #其他情况用星号代替。
	  echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload}"
        exit 2
esac		
#写一个case案例：
#vim   case.sh

#!/bin/bash
read -p "please input a number: " n   #注意n前方一定要有空格，没有空格会报错。
m=$[$n%2]
case $m in
    1)
	  echo "The number is  jishu."
	  ;;
	0)
	   echo "The number is  oushu."
	   ;;
	*)
	   echo "It is not jishu or oushu."
	   ;;
esac

:wq!

#加入我们输入abcd，会出现什么情况。
#vim   case2.sh

#!/bin/bash
read -p "please input a number: " n   #注意n前方一定要有空格，没有空格会报错。
m=$[$n%2]
echo $m          #加入这句。
case $m in
    1)
	  echo "The number is  jishu."
	  ;;
	0)
	   echo "The number is  oushu."
	   ;;
	*)
	   echo "It is not jishu or oushu."
	   ;;
esac

:wq!
[root@sunlocalhost shell]# chmod 700 !$
chmod 700 case2.sh
[root@sunlocalhost shell]# ./case2.sh 
please input a number: abcd
0
The number is  oushu.

1.8for循环

#vim  for.sh

#!/bin/bash
for i in `seq 1 10`    #seq是产生序列的一个命令。
   do
     echo $i
   done

:wq!

[root@sunlocalhost shell]# ./for.sh
1
2
3
4
5
6
7
8
9
10
**************************************************
#seq命令
[root@sunlocalhost shell]# seq 1 10
1
2
3
4
5
6
7
8
9
10
[root@sunlocalhost shell]# seq 1 2 10    #可以设置步长。
1
3
5
7
9
[root@sunlocalhost shell]# seq 10 -2 1   #倒序。
10
8
6
4
2
#按照指定的格式生产序列。
[root@sunlocalhost shell]# seq -w 1 10
01
02
03
04
05
06
07
08
09
10
[root@sunlocalhost shell]# seq -w 01 10   #它会按照最大的数的长度去设置位数。
01
02
03
04
05
06
07
08
09
10

************************************************************

#vim  for2.sh

#!/bin/bash
for i in {1..10}   #{1..10} 表示1-10.
   do
     echo $i
   done

:wq!
[root@sunlocalhost shell]# chmod 700 !$
chmod 700 for2.sh
[root@sunlocalhost shell]# ./!$
./for2.sh
1
2
3
4
5
6
7
8
9
10

#vim  for3.sh

#!/bin/bash
sum=0
for i in {1..10}  
   do
     sum=$[$sum+$i]
   done
echo $sum
:wq!
                                                                                  
[root@sunlocalhost shell]# chmod 700 !$
chmod 700 for3.sh
[root@sunlocalhost shell]# ./!$
./for3.sh
55
#以文件内容的每一行作为循环条件。
#touch 1.txt
#cat /etc/passwd > 1.txt
#vim  for4.sh
for l in `cat 1.txt`
do  
    echo $l
done

:wq!

#vim  3.txt
1.1.1.1
2.2.2.2
3.3.3.3

:wq!

#for  ip  in `cat 3.txt` ;do  echo $ip ; done
1.1.1.1
2.2.2.2
3.3.3.3

EG:
#for  ip  in `cat 3.txt` ;do  echo $ip ;ssh $ip "w" ; done
EG2:
#touch 444.txt;echo "192.168.31.107">444.txt
[root@sunlocalhost shell]# for ip in `cat 444.txt` ;do echo $ip;ssh $ip "w";done
192.168.31.107
The authenticity of host '192.168.31.107 (192.168.31.107)' can't be established.
RSA key fingerprint is d0:9e:ee:4c:27:14:d9:8c:91:1c:f3:42:32:cc:03:95.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.31.107' (RSA) to the list of known hosts.
root@192.168.31.107's password: 
 22:57:37 up 22:11,  2 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
root     tty1     -                29Mar16  2days  0.07s  0.07s -bash
root     pts/0    192.168.31.176   21:26   14.00s  0.23s  0.16s ssh 192.168.31.	 
EG3:
#for file in `ls`;do echo $file;done
1.txt
3.txt
444.txt
case2.sh
case.sh
first.sh
for2.sh
for3.sh
for4.sh
for.sh


1.9while循环

#vim   while.sh

#!/bin/bash
#这是一个死循环。
while :
do
   data +%T
   sleep 3
done   

:wq!
chmod  700 !$
sh  !$

#从1到10进行累加。
#vim  while2.sh

#!/bin/bash
n=0                    #不加这句会报"[: =: unary operator expected"。
while  [ $n -le 10 ]
do 
     echo $n
	 $n=$[$n+1]
done

:wq!

补充：
 ×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
    shell脚本报错："[: =: unary operator expected"

    在匹配字符串相等时，我用了类似这样的语句：

if [ $STATUS == "OK" ]; then     

echo "OK"

fi

    在运行时出现了 [: =: unary operator expected 的错误，就一直找不到原因，尝试了删除等号两侧的空格和括号里的空格都不管用，最后baidu了一下，才找到原因。把语句改成这样就不会出错了.

if [[ $STATUS = "OK" ]]; 

then     

echo "OK"

fi

    究其原因，是因为如果变量STATUS值为空，那么就成了 [ = "OK"] ，显然 [ 和 "OK" 不相等并且缺少了 [ 符号，所以报了这样的错误。当然不总是出错，如果变量STATUS值不为空，程序就正常了，所以这样的错误还是很隐蔽的。

    或者用下面的方法也能避免这种错 误：if [ "$STATUS"x == "OK"x ]; then     echo

"OK"fi。当然，x也可以是其他字符。顺便提一点，shell中有没有双引号在很多情况下是一致的。

 ××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
 
 #vim  while3.sh
 #!/bin/bash
 n=1
 while [ -n "$n" ]
 do
   read -p "Please input a number: " m
   n=`echo $m |sed 's/[0-9]//g'`
   echo "Your input is not a number."
 done
 
 :wq!
 [root@sunlocalhost shell]# sh while3.sh 
Please input a number: nnn
Your input is not a number.
Please input a number: 111
Your input is not a number.
[root@sunlocalhost shell]# sh while3.sh 
Please input a number: 111nnn
Your input is not a number.
Please input a number: 12234
Your input is not a number.

 #vim  while4.sh
 #/bin/bash
n=1
while [ ! -z "$n" ]
do 
    read -p "Please input a number: " m
    n=`echo $m |sed 's/[0-9]//g'`
    if [ -z "$n" ]
    then
        echo $m
		exit
	fi
done

:wq!
[root@sunlocalhost shell]# ./while4.sh
Please input a number:123nnn
Please input a number:122333
122333

		
 2.0shell中断继续退出
 控制循环关键词break\continue\exit
 
 EG:
 #vim  for002.sh
 
 #!/bin/bash
 for  i  in `seq 1 10`
 do 
     echo $i
	 if [ $i -eq 4 ]
	 then 
	      break          #break只是退出当前循环。
	 fi
	 echo $i
done
echo "for done"
:wq!

 [root@sunlocalhost shell]# chmod 700 !$
chmod 700 for002.sh
[root@sunlocalhost shell]# ./!$
./for002.sh
1
1
2
2
3
3
4
for done

EG2:
#vim  for003.sh
 
 #!/bin/bash
 for  i  in `seq 1 10`
 do 
     echo $i
	 if [ $i -eq 4 ]
	 then 
	      continue         #注意此处执行到continue时，没有继续往下执行，而是结束本次循环，并且继续后面的循环。
	 fi
	 echo $i
done
echo "for done"
:wq!

 [root@sunlocalhost shell]# chmod 700 !$
chmod 700 for002.sh
[root@sunlocalhost shell]# ./!$
./for003.sh
1
1
2
2
3
3
4   #注意此处执行到continue时，没有继续往下执行，而是结束本次循环，并且继续后面的循环。
5
5
6
6
7
7
8
8
9
9
10
10
for done

EG3:
 #vim  for004.sh
 
 #!/bin/bash
 for  i  in `seq 1 10`
 do 
     echo $i
	 if [ $i -eq 4 ]
	 then 
	     exit        #跳出整个shell.
	 fi
	 echo $i
done
echo "for done"
:wq!

 [root@sunlocalhost shell]# chmod 700 !$
 [root@sunlocalhost shell]# ./!$
././for004.sh
1
1
2
2
3
3
4

个人理解：
****************************
continue  #结束这一次循环后，继续执行当前循环。
break      #结束当前整个循环，继续执行其他语句。
exit       #结束当前shell.
****************************

2.1shell函数
理解：函数可以被认为是shell中的小单元，我们可以调用这个小单元。


#vim  fun.sh

#!/bin/bash
function    mysum()  {   #mysum()是函数名。
     sum=$[$1+$2]
	 echo $sum
}

a=1
b=2
mysum  $a $b      #调用mysum.

：wq!

[root@sunlocalhost shell]# chmod 700 !$
chmod 700 fun.sh
[root@sunlocalhost shell]# ./!$
./fun.sh
3

EG2:
#vim  fun2.sh

#!/bin/bash
function    mysum()  {   #mysum()是函数名。这个function可以省略。
     sum=$[$1+$2]
	 echo $sum
}

a=1
b=2
mysum  $a $b      #调用mysum.
echo $sum         #函数里面的变量也可以在函数外面去使用。
：wq!

[root@sunlocalhost shell]# ./!$
./fun2.sh
3
3

EG3:
EG2:
#vim  fun3.sh

#!/bin/bash
function    mysum()  {   
    local  sum=$[$1+$2]   #加上local后，这个变量变成局部变量，只能在函数内使用。
	 echo $sum
}

a=1
b=2
mysum  $a $b      
echo $sum         
：wq!
[root@sunlocalhost shell]# chmod 700 !$
chmod 700 ./fun3.sh
[root@sunlocalhost shell]# ./!$
./fun3.sh
3
#此时这个变量就无法在函数外部生效。

2.2shell数组

#数组定义方式

[root@sunlocalhost shell]# a=(1 2 3 4)
[root@sunlocalhost shell]# echo $a
1
//这样是无法显示整个数组的值的。
[root@sunlocalhost shell]# echo ${a[@]}
1 2 3 4
[root@sunlocalhost shell]# echo ${a[*]}
1 2 3 4
[root@sunlocalhost ~]# echo ${a[1]}
2
[root@sunlocalhost ~]# echo ${a[0]}
1
[root@sunlocalhost ~]# echo ${a[2]}
3
[root@sunlocalhost ~]# echo ${a[3]}
4
#增加一个数组：
[root@sunlocalhost ~]# a[4]=9
[root@sunlocalhost ~]# echo ${a[4]}
9
[root@sunlocalhost ~]# echo ${a[*]}
1 2 3 4 9

#更改其中某一个元素：
[root@sunlocalhost ~]# a[2]=7
[root@sunlocalhost ~]# echo  ${a[*]}
1 2 7 4 9

#统计属组中元素个数的脚本
×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
[root@sunlocalhost ~]# echo  ${a[*]}
#touch  0.txt;echo ${a[*]}>0.txt
[root@sunlocalhost ~]# vim !$
vim ././sum.sh
#!/bin/bash
##writen by sunwang

for n in `cat 0.txt`
do
  i=$[$i+1]
done
echo $i
:wq!
[root@sunlocalhost ~]# ./!$
./././sum.sh
5
×××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××××
#统计属组中元素个数的命令
[root@sunlocalhost ~]# echo ${#a[@]}
5

#比较10个随机数大小。
#for  i in `seq 0 9`;do a[$i]=$RANDOM;done;echo ${a[@]} |sed 's/ /\n/g'

#$RANDOM表示4位或者5位随机数字。
EG1:
[root@sunlocalhost ~]# for  i in `seq 0 9`;do a[$i]=$RANDOM;done;echo ${a[@]}
10708 9708 21739 10049 21124 30834 5472 30673 16833 1991
[root@sunlocalhost ~]# for  i in `seq 0 9`;do a[$i]=$RANDOM;done;echo ${a[@]} |sed 's/ /\n/g'
12686
31020
14426
18807
21376
32199
7920
19016
28394
25232
[root@sunlocalhost ~]# for  i in `seq 0 9`;do a[$i]=$RANDOM;done;echo ${a[@]} |sed 's/ /\n/g'|sort
12964
13025
14427
18943
22401
22785
2408
25165
26292
2902
[root@sunlocalhost ~]# for  i in `seq 0 9`;do a[$i]=$RANDOM;done;echo ${a[@]} |sed 's/ /\n/g'|sort -n
1857
4016
7864
8146
13373
14958
15356
18527
21263
31633
#清除数组
[root@sunlocalhost ~]# unset a     #unset用来删除一个变量。
[root@sunlocalhost ~]# echo ${a[@]}

[root@sunlocalhost ~]# 

#清除其中一个元素
[root@sunlocalhost ~]# for  i in `seq 0 9`;do a[$i]=$RANDOM;done;echo ${a[@]}
942 10873 28614 15556 29356 31869 32724 24324 11257 2924
[root@sunlocalhost ~]# unset a[4]d
[root@sunlocalhost ~]# echo ${a[*]}
942 10873 28614 15556 31869 32724 24324 11257 2924

#只显示局部的元素
[root@sunlocalhost ~]# echo ${a[*]:0:3}   #“:0:3”表示从第一个数开始，一共是3个数。
942 10873 28614
[root@sunlocalhost ~]# echo ${a[*]:0:4}
942 10873 28614 15556

shell中的select用法

#!/bin/bash
echo "Please chose a number, 1: run w, 2: run top, 3: run free, 4: quit"
echo
select command in w top free quit
do
    case $command in
    w)
        w
        ;;
    top)
        top
        ;;
    free)
        free
        ;;
    quit)
        exit
        ;;
    *)
        echo "Please input a number:(1-4)."
        ;;
    esac
done

执行结果如下：
sh select.sh
Please chose a number, 1: run w, 2: run top, 3: run free, 4: quit

1) w
2) top
3) free
4) quit
#? 1
16:03:40 up 32 days,  2:42,  1 user,  load average: 0.01, 0.08, 0.08
USER     TTY      FROM              LOGIN@   IDLE   JCPU   PCPU WHAT
root     pts/0    61.135.172.68    15:33    0.00s  0.02s  0.00s sh select.sh

#? 3
             total       used       free     shared    buffers     cached
Mem:       1020328     943736      76592          0      86840     263624
-/+ buffers/cache:     593272     427056
Swap:      2097144      44196    2052948
#?


我们发现，select会默认把序号对应的命令列出来，每次输入一个数字，则会执行相应的命令，命令执行完后并不会退出脚本。它还会继续让我们再次输入序号。序号前面的提示符，我们也是可以修改的，利用变量PS3即可，再次修改脚本如下：

#!/bin/bash
PS3="Please select a number: "
echo "Please chose a number, 1: run w, 2: run top, 3: run free, 4: quit"
echo

select command in w top free quit
do
    case $command in
    w)
        w
        ;;
    top)
        top
        ;;
    free)
        free
        ;;
    quit)
        exit
        ;;
    *)
        echo "Please input a number:(1-4)."
    esac
done

如果想要脚本每次输入一个序号后就自动退出，则需要再次更改脚本如下：

#!/bin/bash
PS3="Please select a number: "
echo "Please chose a number, 1: run w, 2: run top, 3: run free, 4: quit"
echo

select command in w top free quit
do
    case $command in
    w)
        w;exit
        ;;
    top)
        top;exit
        ;;
    free)
        free;exit
        ;;
    quit)
        exit
        ;;
    *)
        echo "Please input a number:(1-4).";exit
    esac
done


######################################################################
shell 的风格，用倒序的字母单词和 正序的单词配对。
比如 if 语句， 结束时用 fi 来配对
esac是和case配对的，是多路分支的语句，类似于C中的 switch/case 语句，大致形式如
case $VAR in
xxx) 
   执行动作
;;
yyy)
 执行动作
;;
esac
######################################################################
































