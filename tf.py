#________LIBRARIES________#
import requests
import os
import time
import samino
import hamino
#__________COLOR__________#
BK = "\033[1;30m" #اسود
RE = "\033[1;31m" #احمر
GR = "\033[1;32m" #اخضر
YE = "\033[1;33m" #اصفر
BL = "\033[1;34m" #ازرق
PU = "\033[1;35m" #وردي
CY = "\033[1;36m" #سماوي
WH = "\033[1;37m" #ابيض
SQ = "\033[1;45m" #مربع
NO = "\033[1;40m" #العادي
LI = "━" #خط
#__________LOGO__________#
LOGO=requests.get('https://pastebin.com/raw/6VL5eeYf')
#__________________________#
print(RE+LOGO.text)
print(PU+LI*60)
link = input(YE+"Community-:"+GR)
print(PU+LI*60)
e = input(YE+"Email-:"+GR)
p = input(YE+"Password-:"+GR)

c=samino.Client()
h=hamino.Client()
c.login(e,p)
h.login(e,p)
print(PU+LI*60)
print(RE+"Starting...")
id = c.get_from_link(link)
comId=id.comId
lok = samino.Local(comId)

def tzr():
    localhour=time.strftime("%y", time.gmtime()); localminute=time.strftime("%b", time.gmtime()); 
    UTC={"GMT0":'+0', "GMT1":'+60', "GMT2":'+120', "GMT3":'+180', "GMT4":'+240', "GMT5":'+300', "GMT6":'+360', "GMT7":'+420', "GMT8":'+480', "GMT9":'+540', "GMT10":'+600', "GMT11":'+660', "GMT12":'+720', "GMT13":'+780', "GMT-1":'-60', "GMT-2":'-120', "GMT-3":'-180',"GMT-4":'-240', "GMT-5":'-300', "GMT-6":'-360', "GMT-7":'-420', "GMT-8":'-480', "GMT-9":'-540', "GMT-10":'-600', "GMT-11":'-660'}; hour = [localhour, localminute]
    if hour[0]=="00":tz=UTC["GMT-1"];return int(tz)
    if hour[0]=="01":tz=UTC["GMT-2"];return int(tz)
    if hour[0]=="02":tz=UTC["GMT-3"];return int(tz)
    if hour[0]=="03":tz=UTC["GMT-4"];return int(tz)
    if hour[0]=="04":tz=UTC["GMT-5"];return int(tz)
    if hour[0]=="05":tz=UTC["GMT-6"];return int(tz)
    if hour[0]=="06":tz=UTC["GMT-7"];return int(tz)
    if hour[0]=="07":tz=UTC["GMT-8"];return int(tz)
    if hour[0]=="08":tz=UTC["GMT-9"];return int(tz)
    if hour[0]=="09":tz=UTC["GMT-10"];return int(tz)
    if hour[0]=="10":tz=UTC["GMT13"];return int(tz)       #UTC["GMT-11"]
    if hour[0]=="11":tz=UTC["GMT12"];return int(tz)
    if hour[0]=="12":tz=UTC["GMT11"];return int(tz)
    if hour[0]=="13":tz=UTC["GMT10"];return int(tz)
    if hour[0]=="14":tz=UTC["GMT9"];return int(tz)
    if hour[0]=="15":tz=UTC["GMT8"];return int(tz)
    if hour[0]=="16":tz=UTC["GMT7"];return int(tz)
    if hour[0]=="17":tz=UTC["GMT6"];return int(tz)
    if hour[0]=="18":tz=UTC["GMT5"];return int(tz)
    if hour[0]=="19":tz=UTC["GMT4"];return int(tz)
    if hour[0]=="20":tz=UTC["GMT3"];return int(tz)
    if hour[0]=="21":tz=UTC["GMT2"];return int(tz)
    if hour[0]=="22":tz=UTC["GMT1"];return int(tz)
    if hour[0]=="23":tz=UTC["GMT0"];return int(tz)
    
def trr():
    return [{"start": int(time.time()), "end": int(time.time() + 300)} for _ in range(50)]

for i in range(24):
 lok.send_active_time(tz=tzr(),timers=trr())
 print(YE+f"{i+1} - Done")
 time.sleep(2)
 
print(GR+"Finished")