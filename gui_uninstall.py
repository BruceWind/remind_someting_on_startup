# -*- coding: utf-8 -*-
# @weizongwei5
###############################################################################
import getpass
import os
import time

sp="/"

username = getpass.getuser()

userhome = sp+"home"+sp+ username
# config dir
config=".config"
config_dir = userhome + sp + config
# autostart dir
autostart="autostart"
autostart_dir = config_dir + sp + autostart


os.chdir(autostart_dir)

os.system("rm remind_someting_on_startup.desktop")
