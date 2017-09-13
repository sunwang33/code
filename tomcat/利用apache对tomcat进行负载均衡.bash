#分别在两台TOMCATAP上安装JDK7
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
 
#在TOMCATAP1上
vim  ~/tomcat/conf/server.xml
<Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000" jvmRoute="TomcatA"/>

<Engine name="Catalina" defaultHost="web1.test.com">
<Host name="web1.test.com"  appBase="/tomcat/webapps"
            unpackWARs="true" autoDeploy="false">
        <Context path="" docBase="/tomcat/webapps/web1" />
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="/naslog/$HOSTNAME/logs"
               prefix="JYDCSTESTAP1_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />

 </Host>
 
 </Engine>
 
 :wq
 
 mkdir  /tomcat/webapps/web1
 cat >> /tomcat/webapps/web1/index.jsp << EOF
 <%@ page language="java"%>
<html>
	<head>
		<title>Tomcat A</title>
	</head>
	<body>
		<h1><font> color="blue">web1.test.com</font></h1>
		<table align="centre" border="1">
			<tr>
					<td>Session ID</td>
		<% session.setAttribute("test.com","test.com");%>
					<td><%=session.getId() %></td>
			</tr>
			<tr>
				<td>Created on</td>
				<td><%=session.getCreationTime()%></td>
			</tr>
		</table>
	</body>
</html>
EOF

#设置环境变量
cat >> /etc/profile.d/tomcat.sh << EOF
export CATALINA_HOME=/tomcat
export PATH=$CATALINA_HOME/bin:$PATH
EOF
source  /etc/profile.d/tomcat.sh

catalina.sh stop
catalina.sh  start

#在TOMCATAP2上
vim  ~/tomcat/conf/server.xml
<Connector port="9090" protocol="HTTP/1.1"
               connectionTimeout="20000" jvmRoute="TomcatB"/>

<Engine name="Catalina" defaultHost="web1.test.com">
<Host name="web1.test.com"  appBase="/tomcat1/webapps"
            unpackWARs="true" autoDeploy="false">
        <Context path="" docBase="/tomcat1/webapps/web1" />
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="/naslog/$HOSTNAME/logs"
               prefix="JYDCSTESTAP1_access_log" suffix=".txt"
               pattern="%h %l %u %t &quot;%r&quot; %s %b" />

 </Host>
 
 </Engine>
 
 :wq
 
 mkdir  /tomcat1/webapps/web1
#文件/tomcat1/webapps/web1/index.jsp从TOMCATAP1上拷贝过来。
sed  -i "s/TomcatA/TomcatB/" /tomcat1/webapps/web1/index.js
#设置环境变量
cat >> /etc/profile.d/tomcat1.sh << EOF
export CATALINA_HOME=/tomcat1
export PATH=$CATALINA_HOME/bin:$PATH
EOF
source  /etc/profile.d/tomcat1.sh

mv /tomcat1/bin/catalina.sh   /tomcat1/bin/catalina1.sh
catalina1.sh stop
catalina1.sh  start

#APACHEAP1上
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
Header add Set-Cookie "ROUTEID=.%{BALANCER_WORKER_ROUTE}e; path=/" env=BALANCER_ROUTE_CHANGED
<proxy balancer://lbcluster1>
	BalancerMember  "http://192.168.137.142:8080" loadfactor=10 route=TomcatA
	BalancerMember  "http://192.168.137.142:9090" loadfactor=10 route=TomcatB
	ProxySet  stickysession=ROUTEID
</proxy>
        
<VirtualHost *:80>
	ServerName web1.test.com
	ProxyVia   On
	ProxyRequests Off
	ProxyPreserveHost On
	<Proxy *>
	    AllowOverride None
	    Order deny,allow
            Allow from all
        </Proxy>
        ProxyPass "/"  "balancer://lbcluster1/"
	ProxyPassReverse  "/"  "balancer://lbcluster1/"
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





