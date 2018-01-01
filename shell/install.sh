#！/bin/bash
ProjectName=qdzh
ActName=deploy
DirName1=${ProjectName}/`date +"%Y_%m_%d"`/
DirName2=${ProjectName}_${ActName}_`date +"%Y_%m_%d"`/
PackageName=${ProjectName}_${ActName}_`date +"%Y_%m_%d"`.tar.gz
ScriptName=${ActName}.sh


#ENSURE  FTP  TOOLS.
yum -y install ftp  >> /dev/null  2>1&

#DOWNLOAD  FILE FROM FTP.

ftp -n << EOF

open  9.54.8.217

user jyftp  jyftp

bin 

cd  ${DirName1}/

get  ${PackageName} 

bye

EOF

#UNCOMPRESS  THIS  PACKAGE.

if [ -f  ${PackageName} ]
then
	/bin/tar -zxvf  ${PackageName}  -C  /tmp >> /dev/null 2>1&
else
	echo "${PackageName}  is not exist." && exit
fi

#RUN  THIS SCRIPT.

#cd  /tmp/${DirName2}

if   [ -f  "/tmp/${DirName2}/${ScriptName}" ]
then
	/bin/bash  /tmp/${DirName2}/${ScriptName}  >> /dev/null 2>1&
else
	echo  "/tmp/${DirName2}/${ScriptName} is not exist." && exit
	
fi

exit 

