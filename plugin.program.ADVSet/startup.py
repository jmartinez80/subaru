import xbmc, xbmcaddon, xbmcgui, xbmcplugin, os, sys, xbmcvfs, glob
import shutil
import urllib2,urllib
import re
import uservar
from datetime import date, datetime, timedelta
from resources.libs import extract, downloader, notify, wizard as wiz # loginit, debridit, traktit, skinSwitch, uploadLog, 

ADDON_ID       = uservar.ADDON_ID
ADDONTITLE     = uservar.ADDONTITLE
ADDON          = wiz.addonId(ADDON_ID)
VERSION        = wiz.addonInfo(ADDON_ID,'version')
ADDONPATH      = wiz.addonInfo(ADDON_ID,'path')
ADDONID        = wiz.addonInfo(ADDON_ID,'id')
DIALOG         = xbmcgui.Dialog()
DP             = xbmcgui.DialogProgress()
HOME           = xbmc.translatePath('special://home/')
PROFILE        = xbmc.translatePath('special://profile/')
KODIHOME       = xbmc.translatePath('special://xbmc/')
ADDONS         = os.path.join(HOME,     'addons')
KODIADDONS     = os.path.join(KODIHOME, 'addons')
USERDATA       = os.path.join(HOME,     'userdata')
PLUGIN         = os.path.join(ADDONS,   ADDON_ID)
PACKAGES       = os.path.join(ADDONS,   'packages')
ADDONDATA      = os.path.join(USERDATA, 'addon_data', ADDON_ID)
FANART         = os.path.join(ADDONPATH,'fanart.jpg')
ICON           = os.path.join(ADDONPATH,'icon.png')
ART            = os.path.join(ADDONPATH,'resources', 'art')
SKIN           = xbmc.getSkinDir()
BUILDNAME      = wiz.getS('buildname')
DEFAULTSKIN    = wiz.getS('defaultskin')
DEFAULTNAME    = wiz.getS('defaultskinname')
DEFAULTIGNORE  = wiz.getS('defaultskinignore')
BUILDVERSION   = wiz.getS('buildversion')
BUILDLATEST    = wiz.getS('latestversion')
BUILDCHECK     = wiz.getS('lastbuildcheck')
DISABLEUPDATE  = wiz.getS('disableupdate')
AUTOCLEANUP    = wiz.getS('autoclean')
AUTOCACHE      = wiz.getS('clearcache')
AUTOPACKAGES   = wiz.getS('clearpackages')
AUTOTHUMBS     = wiz.getS('clearthumbs')
AUTOFEQ        = wiz.getS('autocleanfeq')
AUTONEXTRUN    = wiz.getS('nextautocleanup')
TRAKTSAVE      = wiz.getS('traktlastsave')
REALSAVE       = wiz.getS('debridlastsave')
LOGINSAVE      = wiz.getS('loginlastsave')
KEEPTRAKT      = wiz.getS('keeptrakt')
KEEPREAL       = wiz.getS('keepdebrid')
KEEPLOGIN      = wiz.getS('keeplogin')
INSTALLED      = wiz.getS('installed')
EXTRACT        = wiz.getS('extract')
EXTERROR       = wiz.getS('errors')
NOTIFY         = wiz.getS('notify')
NOTEDISMISS    = wiz.getS('notedismiss')
NOTEID         = wiz.getS('noteid')
BACKUPLOCATION = ADDON.getSetting('path') if not ADDON.getSetting('path') == '' else HOME
MYBUILDS       = os.path.join(BACKUPLOCATION, 'My_Builds', '')
NOTEID         = 0 if NOTEID == "" else int(NOTEID)
AUTOFEQ        = int(AUTOFEQ) if AUTOFEQ.isdigit() else 0
TODAY          = date.today()
TOMORROW       = TODAY + timedelta(days=1)
TWODAYS        = TODAY + timedelta(days=2)
THREEDAYS      = TODAY + timedelta(days=3)
ONEWEEK        = TODAY + timedelta(days=7)
KODIV          = float(xbmc.getInfoLabel("System.BuildVersion")[:4])
EXCLUDES       = uservar.EXCLUDES
BUILDFILE      = uservar.BUILDFILE
UPDATECHECK    = uservar.UPDATECHECK if str(uservar.UPDATECHECK).isdigit() else 1
NEXTCHECK      = TODAY + timedelta(days=UPDATECHECK)
NOTIFICATION   = uservar.NOTIFICATION
ENABLE         = uservar.ENABLE
HEADERMESSAGE  = uservar.HEADERMESSAGE
AUTOUPDATE     = uservar.AUTOUPDATE
WIZARDFILE     = uservar.WIZARDFILE
AUTOINSTALL    = uservar.AUTOINSTALL
REPOID         = uservar.REPOID
REPOADDONXML   = uservar.REPOADDONXML
REPOZIPURL     = uservar.REPOZIPURL
COLOR1         = uservar.COLOR1
COLOR2         = uservar.COLOR2
WORKING        = True if wiz.workingURL(BUILDFILE) == True else False
FAILED         = False

while xbmc.Player().isPlayingVideo():
	xbmc.sleep(1000)

if KODIV >= 17:
	NOW = datetime.now()
	temp = wiz.getS('kodi17iscrap')
	if not temp == '':
		if temp > str(NOW - timedelta(minutes=2)):
			wiz.log("Killing Start Up Script")
			sys.exit()
	wiz.log("%s" % (NOW))
	wiz.setS('kodi17iscrap', str(NOW))
	xbmc.sleep(1000)
	if not wiz.getS('kodi17iscrap') == str(NOW):
		wiz.log("Killing Start Up Script")
		sys.exit()
	else:
		wiz.log("Continuing Start Up Script")

wiz.log("[Path Check] Started", xbmc.LOGNOTICE)
path = os.path.split(ADDONPATH)
if not ADDONID == path[1]: DIALOG.ok(ADDONTITLE, '[COLOR %s]Please make sure that the plugin folder is the same as the ADDON_ID.[/COLOR]' % COLOR2, '[COLOR %s]Plugin ID:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, ADDONID), '[COLOR %s]Plugin Folder:[/COLOR] [COLOR %s]%s[/COLOR]' % (COLOR2, COLOR1, path)); wiz.log("[Path Check] ADDON_ID and plugin folder doesnt match. %s / %s " % (ADDONID, path))
else: wiz.log("[Path Check] Good!", xbmc.LOGNOTICE)

if KODIADDONS in ADDONPATH:
	wiz.log("Copying path to addons dir", xbmc.LOGNOTICE)
	if not os.path.exists(ADDONS): os.makedirs(ADDONS)
	newpath = xbmc.translatePath(os.path.join('special://home/addons/', ADDONID))
	if os.path.exists(newpath):
		wiz.log("Folder already exists, cleaning House", xbmc.LOGNOTICE)
		wiz.cleanHouse(newpath)
		wiz.removeFolder(newpath)
	try:
		wiz.copytree(ADDONPATH, newpath)
	except Exception, e:
		pass
	wiz.forceUpdate(True)

try:
	mybuilds = xbmc.translatePath(MYBUILDS)
	if not os.path.exists(mybuilds): xbmcvfs.mkdirs(mybuilds)
except:
	pass




wiz.log("[Auto-Limpieza] Iniciada", xbmc.LOGNOTICE)
if AUTOCLEANUP == 'true':
	service = False
	days = [TODAY, TOMORROW, THREEDAYS, ONEWEEK]
	feq = int(float(AUTOFEQ))
	if AUTONEXTRUN <= str(TODAY) or feq == 0:
		service = True
		next_run = days[feq]
		wiz.setS('nextautocleanup', str(next_run))
	else: wiz.log("[Auto-Limpieza] Siguiente en %s" % AUTONEXTRUN, xbmc.LOGNOTICE)
	if service == True:
		AUTOCACHE      = wiz.getS('clearcache')
		AUTOPACKAGES   = wiz.getS('clearpackages')
		AUTOTHUMBS     = wiz.getS('clearthumbs')
		if AUTOCACHE == 'true': wiz.log('[Auto-Limpieza] Cache: On', xbmc.LOGNOTICE); wiz.clearCache(True)
		else: wiz.log('[Auto-Limpieza] Cache: Off', xbmc.LOGNOTICE)
		if AUTOTHUMBS == 'true': wiz.log('[Auto-Limpieza] viejos Thumbs: On', xbmc.LOGNOTICE); wiz.oldThumbs()
		else: wiz.log('[Auto-Limpieza] viejos Thumbs: Off', xbmc.LOGNOTICE)
		if AUTOPACKAGES == 'true': wiz.log('[Auto-Limpieza] Packages: On', xbmc.LOGNOTICE); wiz.clearPackagesStartup()
		else: wiz.log('[Auto-Limpieza] Packages: Off', xbmc.LOGNOTICE)
else: wiz.log('[Auto-Limpieza] Apagada', xbmc.LOGNOTICE)

wiz.setS('kodi17iscrap', '')#')