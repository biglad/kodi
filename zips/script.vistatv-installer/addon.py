import xbmc
import utils
import os
import platform
import xbmcgui
import sfile
import urllib
import urllib2
import time
import re
import downloader
import extractor
import xbmcvfs
import shutil
import base64
import xbmcaddon
import time
from uuid import getnode as get_mac
from resources.lib.kodion.impl import Context
from resources.lib.kodion.constants import setting
import subprocess
import random
import string
global UPDATE
from urllib2 import urlopen
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
if KODIV > 17:
    import zfile as zipfile #FTG mod for Kodi 18
else:
    import zipfile
dialog = xbmcgui.Dialog()  
mac = "00:00:00:00:00:00"
finalmac = "00:00:00:00:00:00"
xbmc.executeJSONRPC('{ "jsonrpc": "2.0", "id": 0, "method":"Settings.setSettingValue", "params": {"setting":"screensaver.mode", "value":""} } ' )
maclist = []






DATAHOME = base64.b64decode("c3BlY2lhbDovL2hvbWUv")





    
  



    


HOME        = xbmc.translatePath(DATAHOME)




file4     =  os.path.join(HOME, 'install4.zip')





def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))




context = Context()

version = context.get_system_version().get_version()
application = context.get_system_version().get_app_name()
settings = context.get_settings()

appversion = 0
if version >= (17, 6):
    appversion = "KODI"
elif version >= (17, 9):
    appversion = "KODI18"
else:
    appversion = "KODI-OUTDATED"
    
    
if appversion == "KODI18":
    Install="GO"
elif appversion == "KODI":
    Install="GO"
else:
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]EyePeaTV[/COLOR][/B]", "Kodi 18.x Supported ONLY", "Press OK to exit",'Please Use Correct Kodi Version..')
    os._exit(1)
    exit()





def platform():
    if xbmc.getCondVisibility('system.platform.android'):
        return 'android'
    elif xbmc.getCondVisibility('system.platform.linux'):
        return 'linux'
    elif xbmc.getCondVisibility('system.platform.windows'):
        return 'windows'
    elif xbmc.getCondVisibility('system.platform.osx'):
        return 'osx'
    elif xbmc.getCondVisibility('system.platform.atv2'):
        return 'atv2'
    elif xbmc.getCondVisibility('system.platform.ios'):
        return 'ios'

    
  






def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import os, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"

    # Ping
    return os.system("ping " + ping_str + " " + host) == 0
    
PART1 = "http://dl.mgawow.co.uk/www/201902121704.zip"
PART4  = "http://dl.mgawow.co.uk/www/kodi18.zip"  
#UPDATE = PART4
    
if not ping("google.com"):
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]EyePeaTV[/COLOR][/B]", "No Internet Connection Found!", "Press OK to exit",'Please Check Your Connection.')
    os._exit(1)
    exit()

   

    


    





   

def killxbmc():
    xbmc.executebuiltin("Notification(PLEASE WAIT, [B][COLOR=gold]KODI WILL NOW CLOSE[/COLOR] -- [COLOR=green]PLEASE WAIT[/COLOR][/B],,7000)")
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV[/COLOR]","CLOSING","PLEASE WAIT")
    xbmc.sleep(3000)
    os._exit(1)
            

def ServerError():
    dp = xbmcgui.DialogProgress()
    dp.create("[COLOR tomato]EyePeaTV[/COLOR]","[COLOR red][B]ERROR[/B][/COLOR]","EyePeaTV Servers Offline")
    xbmc.sleep(1500)
    dp.close()
    update = xbmcgui.Dialog().yesno("[COLOR gold]EyePeaTV Build Installer[/COLOR]","[COLOR yellow]Sorry Our Server Seems to be[/COLOR] [COLOR red][B]OFFLINE[/B][/COLOR]","Sorry For This Will Will Have It Fixed Soon!!","[COLOR tomato]Try Again NOW??[/COLOR]")
    if update:
        xbmc.executebuiltin('RunAddon(script.vistatv-installer)')
        exit()
    else:
        exit()  
        

def install():

    global UPDATE   
    ###downloader . download(PART1,file1,"Downloading Build Data")
    ###extractor . extract(file1,HOME,"Installing Build Data")
    #downloader . download(PART2,file2,"Downloading Build Data Part 2")
    #extractor . extract(file2,HOME,"Unpacking Part 2")
    #downloader . download(PART3,file3,"Downloading Build Data Part 3")
    #extractor . extract(file3,HOME,"Unpacking Part 3")
    downloader . download(UPDATE,file4,"Downloading EyePeaTV Build Info")
    extractor . extract(file4,HOME,"Installing EyePeaTV Data")
    #xbmc.Player().stop()
    #xbmc.executebuiltin( "XBMC.SetVolume(100)" )
    dialog = xbmcgui.Dialog()
    dialog.ok("[COLOR=red][B]EyePeaTV[/COLOR][/B]", "Installer Now Configured", "Kodi will now Exit","Open kodi agin to continue install")
    killxbmc()
    exit()
 

def setplayermodes():
    #dp.close()
    if platform == "windows":
        xbmc.executebuiltin('ActivateWindow(10040,"addons://repository.xbmc.org/kodi.inputstream",return)')
        dialog = xbmcgui.Dialog()
        dialog.ok("[COLOR=red][B]INFORMATION[/COLOR][/B]", "ENABLE!!!", "[COLOR=yellow]ALL OPTIONS","These need to be on for best playback[/COLOR]")
    
        while xbmc.getCondVisibility("Window.IsActive(10040)"):
            xbmc.sleep(1000)        
    #install()
    exit()  



dialog = xbmcgui.Dialog()

install1 = "http://dl.mgawow.co.uk/www/kodi18.zip"  
install2 = "http://dl.mgawow.co.uk/www/NEW-BUILD.zip"  
install3 = "http://dl.mgawow.co.uk/www/NEW-SKYQ.zip"  
install4 = "http://dl.mgawow.co.uk/www/TITAN-BUILD.zip"


def menuoptions():
    global UPDATE
    dialog = xbmcgui.Dialog()
    funcs = (
        function1,
        function2,
        function3,
        function4
		)
        
    call = dialog.select('[B][COLOR=yellow]EPTV Kodi Build Installer[/COLOR][/B]', [
    "[B][COLOR=orange]      Smarters For Kodi[/COLOR][/B] (Gold & Normal)", #1
    "[B][COLOR=orange]      Simple For Kodi[/COLOR][/B] (Gold ONLY!)",#2
    "[B][COLOR=orange]      SkyQ Theme[/COLOR][/B] (Gold ONLY!)",#3
    "[B][COLOR=orange]      Titan Theme[/COLOR][/B] (Gold ONLY!)",#4
    ])
    # dialog.selectreturns
    #   0 -> escape pressed
    #   1 -> first item
    #   2 -> second item
    if call:
        # esc is not pressed
        if call < 0:
            return
        func = funcs[call-4]
        #if myplatform == 'windows':
        #    func = funcs[call-23]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]VistaTV[/COLOR]",""+str(func)+" -3","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    else:
        func = funcs[call]
        #dp = xbmcgui.DialogProgress()
        #dp.create("[COLOR tomato]VistaTV[/COLOR]",""+str(func)+" +0","PLEASE EXIT KODI OR PULL THE POWER LEAD")
        #xbmc.sleep(1000)
        return func()
    return 



def function1():
    UPDATE = install1
    downloader . download(UPDATE,file4,"Downloading EyePeaTV Build Info")
    extractor . extract(file4,HOME,"Installing EyePeaTV Data")
    #setplayermodes()
    killxbmc()	
	
def function2():
    UPDATE = install2
    downloader . download(UPDATE,file4,"Downloading EyePeaTV Build Info")
    extractor . extract(file4,HOME,"Installing EyePeaTV Data")
    #install()
    #setplayermodes()
    killxbmc()
    
def function3():
    UPDATE = install3
    downloader . download(UPDATE,file4,"Downloading EyePeaTV Build Info")
    extractor . extract(file4,HOME,"Installing EyePeaTV Data")
    #install()
    #setplayermodes()
    killxbmc()
    
def function4():
    UPDATE = install4
    downloader . download(UPDATE,file4,"Downloading EyePeaTV Build Info")
    extractor . extract(file4,HOME,"Installing EyePeaTV Data")
    #install()
    #setplayermodes()
    killxbmc()
		
#addon_id = "plugin.video.eyepeatv.2"
#__settings__=xbmcaddon.Addon(id=addon_id); __language__=__settings__.getLocalizedString
#def get_setting(name): dev=__settings__.getSetting(name); return dev
#username=get_setting("Username")
#password=get_setting("Password")
#if username =="":
menuoptions()

 
 
