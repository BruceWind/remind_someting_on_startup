# -*- coding: utf-8 -*-
# @weizongwei5
###############################################################################


import sys
import socket
import os
import getpass
import time
import urllib2


def clear_all_cache_file():
    os.system("rm *~")

# one minute countdown....
i = 1
while (i <= 15):
    str = raw_input("\n\t"+"今天打卡了吗？")
    if (str == "y" or str == "yes"):
        i = 15
        print("\n\t next second will exit!!")
    time.sleep(1)
    i += 1

# need some field
    username = getpass.getuser()
separator = "/"
