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

# get current dir
pwd_dir=os.getcwd()

os.chdir(userhome)

os.system("mkdir "+config)
os.chdir(config_dir)

os.system("mkdir "+autostart)
os.chdir(autostart_dir)

fp = open('remind_someting_on_startup.desktop', 'w')
fp.write(
"[Desktop Entry] "+"\n"+
" Name=remind_someting_on_startup "+"\n"+
" Comment=Remind someting on startup "+"\n"+
" Exec=python "+pwd_dir+"/auto_remind.py" +"\n"+
"Terminal=true"+"\n"+
"MultipleArgs=false"+"\n"+
"Type=Application"+"\n"+
"Categories=Application;Development;"+"\n"+
"StartupNotify=true")

fp.close()
