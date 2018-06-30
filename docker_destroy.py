#!/usr/bin/python3

# you can use dockillnew instead to run this file
import os

#killing all the container
os.system("dockill")

#resoting the content of /etc/ansible/hosts
os.system("cp /root/Desktop/Python/docker_setupfiles/hosts /etc/ansible/hosts")

