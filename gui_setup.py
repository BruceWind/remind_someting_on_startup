# -*- coding: utf-8 -*-
# @weizongwei5
###############################################################################
import getpass
import os
import time

username = getpass.getuser()
config=".config"
autostart="autostart"


sp="/"

userhome = "/home/"+ username
config_dir = userhome + sp + config
autostart_dir = config_dir + sp + autostart

pwd_dir=os.getcwd()

os.chdir(userhome)

os.system("mkdir "+config)
os.chdir(config_dir)

os.system("mkdir "+autostart)
os.chdir(autostart_dir)

fp = open('remind_someting_on_startup.desktop', 'w')
fp.write(
"[Desktop Entry] "+"\n"+
" Name=auto_push_ip "+"\n"+
" Comment=remind someting on startup "+"\n"+
" Exec=python "+pwd_dir+"/auto_remind.py" +"\n"+
"Terminal=true"+"\n"+
"MultipleArgs=false"+"\n"+
"Type=Application"+"\n"+
"Categories=Application;Development;"+"\n"+
"StartupNotify=true")

fp.close()
