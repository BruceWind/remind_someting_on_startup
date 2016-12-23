# -*- coding: utf-8 -*-
# @weizongwei5
###############################################################################
import sys
import socket
import inspect
import os
import getpass
import time
import urllib2
import datetime


def is_am():
    currentTime = datetime.datetime.now()
    return currentTime.hour < 12



# cd to file dir
file_dir= os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(file_dir)

fp = open('remind.txt', 'r')
remind_text=fp.readline()
fp.close()
# if not set .
if(len(remind_text)==0):
    remind_text="1.今天打卡了吗？(y/n)"

i = 1
while (i <= 15 and  is_am()):
    time.sleep(1)
    str = raw_input("\n\t"+remind_text+"\n\t")
    if (str == "y" or str == "yes"):
        i = 15
        print("\n\t next second will exit!!")
        time.sleep(1)

    i += 1

# need some field
    username = getpass.getuser()
separator = "/"
