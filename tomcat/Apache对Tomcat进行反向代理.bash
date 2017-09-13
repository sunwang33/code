Apache+Tomcat环境搭建(已验证)
#安装JDK
#创建安装目录
mkdir  /java
tar -zxvf  jdk-7u80-linux-x64.gz  -C  /java/
vim  /etc/profile.d/java.sh
#添加以下变量，并用export宣告给所有子shell。
JAVA_HOME=/java/jdk1.7.0_80/

JAVA_BIN=/java/jdk1.7.0_80/bin

PATH=$PATH:$JAVA_HOME/bin

export JAVA_HOME JAVA_BIN PATH

:wq
source /etc/profile.d/java.sh

# 如果存在openjdk,删除openjdk
 rpm -e openjdk  --nodeps
 
 #验证新装jdk版本
 java -version

#安装tomcat
groupadd  -g GID  GROUPNAME
useradd  -u UID  -g  GID  -m -d /home/XXXX    XXXX
chown -R  UID:GID  /tomcat
 tar -zxvf apache-tomcat-8.0.46.tar.gz -C /tomcat/
cd  /tomcat
mv apache-tomcat-8.0.46/*   ./
vim /etc/profile.d/tomcat.sh
export CATALINA_HOME=/tomcat
export PATH=$CATALINA_HOME/bin:$PATH
:wq
source   /etc/profile.d/tomcat.sh
#用命令catalina.sh version进行测试。
#手动添加一个测试程序
cd   /tomcat/webapps
mkdir myapp1
vim ./myapp1/index.jsp
<%@ page language="java"%>
<%@ page import="java.util.*" %>
<html>
<head>
<title>JSP TEST PAGE</title>
</head>
<body>
<%  out.println("hello world.（from myapp1)");%>
</body>
</html>
:wq
#配置webapp管理工具和virtualHost管理工具
cd  /tomcat/conf
vim tomcat-users.xml
 <role rolename="manager-gui"/>
  <role rolename="admin-gui"/>
  <user username="tcadmin" password="tcadmin" roles="manager-gui,admin-gui"/>
:wq
vim   server.xml
#连接器配置如下（采用nio运行模式）：
 <Connector port="8080" protocol="org.apache.coyote.http11.Http11NioProtocol" 
        connectionTimeout="20000" 
        URIEncoding="UTF-8" 
        useBodyEncodingForURI="true" 
        enableLookups="false" 
        redirectPort="8443" />

#虚拟主机配置如下：
  <Host name="www.jiuyingtec.com" appBase="/tomcat/webapps"  
            unpackWARs="false" autoDeploy="true" xmlValidation="false" 
            xmlNamespaceAware="false">
           <Context path="/myapp1" docBase="/tomcat/webapps/myapp1" debug="0" reloadable="true" crossContext="true"/>
           <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
                  prefix="www.jiuyingtec.com_access_log." suffix=".log"
                  pattern="%h %l %u %t &quot;%r&quot; %s %b"  />

      </Host>

:wq
mkdir -p  /naslog/TESTAP1/logs
cp web1/index.jsp myapp1
catalina.sh stop
catalina.sh start
在浏览器上访问http://www.jiuyingtec.com:8080/myapp1/ 

#安装apache
方法一：用rpm包安装
镜像自带httpd包信息：httpd-2.2.15-29.el6_4.x86_64
cd /etc/httpd/conf
vim  httpd.conf
ServerName web1.jiutingtec.com:80
#DocumentRoot "/var/www/html"
Include conf/extra/httpd-vhosts.conf
:wq
 mkdir conf.d
vim conf.d/vhosts.conf
<VirtualHost *:80>
        ServerName www.jiuyingtec.com
        ProxyVia   On
        ProxyRequests Off
        ProxyPreserveHost On
        <Proxy *>
            AllowOverride None
            Order deny,allow
            Allow from all
        </Proxy>
        ProxyPass /  http://192.168.137.142:8080/
        ProxyPassReverse  / http://192.168.137.142:8080/
        <Location />
            Order deny,allow
            Allow from all
        </Location>
</VirtualHost>
:wq
#检查配置文件语法
httpd -t
#设置开机启动
chkconfig --level 2345 httpd on
#启动服务
service httpd restart

方法二：用源码包安装apache  （Apache 版本2.4.25）
#安装相关依赖包
 yum -y install pcre pcre-devel wget  gcc zlib zlib-devel make openssl-devel expat-devel perl  
#安装 apr-1.6.2
cd  /usr/local/src
 tar -zxf  apr-1.6.2.tar.gz
cd  apr-1.6.2
./configure  --prefix=/usr/local/apr && make && make install
#安装apr-util-1.6.0 
cd  /usr/local/src
tar -zxf apr-util-1.6.0.tar.gz
cd  apr-util-1.6.0
./configure  --prefix=/usr/local/apr-util --with-apr=/usr/local/apr && make && make install
#安装apache2.4.25
cd  /usr/local/src
tar -zxf httpd-2.4.25.tar.gz
cd  httpd-2.4.25
./configure  --prefix=/usr/local/apache2  --with-apxs2=/usr/local/apache2/bin/apxs  --with-libxml-dir   --with-gd  --with-jpeg-dir  --with-png-dir --enable-so  --enable-rewrite  --enable-ssl  --with-ssl=/usr/lib  --enable-auth-digest  --enable-cgi  --with-freetype-dir  --with-iconv-dir --with-zlib-dir  --with-bz2 --with-openssl --with-mcrypt  --enable-soap  --enable-gd-native-ttf  --enable-mbstring  --enable-mbstring  --enable-sockets --enable-exif  --disable-ipv6  --enable-http --enable-proxy    --enable-proxy-ajp --enable-proxy-connect  --enable-proxy-http --enable-lbmethod-byrequests  --enable-proxy-balancer  --with-suexec-caller=daemon  --with-suexec-docroot=/usr/local/apache2/htdocs   --with-apr=/usr/local/apr   --with-apr-util=/usr/local/apr-util && make && make install
#修改配置文件
cd /etc/httpd/conf
vim  httpd.conf
ServerName www.jiutingtec.com:80
#DocumentRoot "/var/www/html"
Include conf/extra/httpd-vhosts.conf    #把注释去掉
:wq
 mkdir conf.d
vim conf/extra/httpd-vhosts.conf
<VirtualHost *:80>
        ServerName www.jiuyingtec.com
        ProxyVia   Off 
        ProxyRequests  Off
        ProxyPreserveHost On
        <Proxy *>
            Require all granted
        </Proxy>
        ProxyPass /  http://192.168.137.142:8080/
        ProxyPassReverse  / http://192.168.137.142:8080/
        <Location />
            Require all granted
        </Location>
</VirtualHost>
:wq
#检查配置文件语法
httpd -t
#设置开机启动
chkconfig --level 2345 httpd on
#启动服务
service httpd restart