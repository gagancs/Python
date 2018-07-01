#!/usr/bin/python3

import os
import time

#catching the no. od DataNodes the client wants
nodes=int(input("Enter how many data nodes you want to launch"))
#opening the file for IPs to run the ansible
file1 = "/etc/ansible/hosts"
f1=open(file1,"a+")

for i in range(nodes):
	if i==0:
		s=i+2
		i=str(i)
		s1=str(s)
		#creating conatiners for DataNodes OS
		os.system("docker run -itd --name node"+i+"  centos6:hadoopv1	" )
		os.system("docker exec node"+i+" service sshd restart")
		#os.system("docker exec node"+i+" hostnamectl set-hostname root@namenode")
		f1.write("\n[dockernns]\n")
		# getting ips and assigning
		#ip=str(os.system("docker exec node"+i+"  hostname -i"))
		#f1.write(ip)
		#f1.write("\n")
		f1.write("172.17.0."+s1)
		f1.write("\n")
		os.system("ssh-keyscan 172.17.0"+s1)
		#os.system("docker exec node"+i+"")
	else:
		s=i+2
		i=str(i)
		s1=str(s)
		#creating conatiners for DataNodes OS
		os.system("docker run -itd --name node"+i+"  centos6:hadoopv1	" )
		os.system("docker exec node"+i+" service sshd restart")
		#os.system("docker exec node"+i+" hostnamectl set-hostname root@datanode"+i)
		f1.write("\n[dockerdns]\n")
		# getting ips and assigning
		#ip=str(os.system("docker exec node"+i+"  hostname -i"))
		#f1.write(ip)
		#f1.write("\n")
		f1.write("172.17.0."+s1)
		f1.write("\n")
		os.system("ssh-keyscan 172.17.0"+s1)
		#os.system("docker exec node"+i+"")


f1.close()
#running playbook to setup
os.system("sudo ansible-playbook /root/Desktop/Python/nndocker.yml")
os.system("sudo ansible-playbook /root/Desktop/Python/dndocker.yml")


#killing all the container
#os.system("dockill")

#resoting the content of /etc/ansible/hosts
#os.system("cp /root/Desktop/Python/docker_setupfiles/hosts /etc/ansible/hosts")
