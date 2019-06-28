#import base64;exec base64.b64decode('
import os, xbmc, xbmcaddon

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[B]ADVSet[/B]'
EXCLUDES       = [ADDON_ID, 'plugin.program.ADVSet']
BUILDFILE      = 'http://'
UPDATECHECK    = 0
APKFILE        = 'https://'
YOUTUBETITLE   = 'https://'
YOUTUBEFILE    = 'https://'
ADDONFILE      = 'https://'
ADVANCEDFILE   = 'https://dl.dropbox.com/s/rb80c4bkvuysrpb/advanced.txt'

PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

ICONBUILDS     = 'http://'
ICONMAINT      = 'http://'
ICONSPEED      = 'http://'
ICONAPK        = 'http://'
ICONRETRO      = 'http://'
ICONADDONS     = 'http://'
ICONYOUTUBE    = 'http://'
ICONSAVE       = 'http://'
ICONTRAKT      = 'http://'
ICONREAL       = 'http://'
ICONLOGIN      = 'http://'
ICONCONTACT    = 'http://'
ICONSETTINGS   = 'http://'

HIDESPACERS    = 'No'

SPACER         = '*'

COLOR1         = 'gold'
COLOR2         = 'white'
COLOR3         = 'lime'

THEME1         = '[B][COLOR '+COLOR3+']([COLOR '+COLOR1+']*[/COLOR])[/COLOR]  [COLOR '+COLOR2+']%s[/COLOR][/B]'
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR1+']%s[/COLOR]'
THEME3         = '[COLOR '+COLOR3+']%s[/COLOR]'
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR]  [COLOR '+COLOR2+']%s[/COLOR]'
THEME5         = '[COLOR '+COLOR3+']Current Theme:[/COLOR]  [COLOR '+COLOR2+']%s[/COLOR]'

HIDECONTACT    = 'Yes'
CONTACT        = ''
CONTACTICON    = 'http://'
CONTACTFANART  = 'http://'

AUTOUPDATE     = 'No'
WIZARDFILE     = 'http://'#zip

AUTOINSTALL    = 'No'
REPOID         = ''
REPOADDONXML   = 'http://'
REPOZIPURL     = 'http://'
ENABLE         = 'No'
NOTIFICATION   = 'http://'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = ''
HEADERIMAGE    = 'http://'
BACKGROUND     = 'http://'
#########################################################')