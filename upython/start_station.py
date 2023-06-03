import network
import time
import socket

from config import id


sta_if = network.WLAN(network.STA_IF);
sta_if.active(True)

#gefunden
def start(ssid,pw):
    sta_if.connect(ssid,pw)
    c=False
    for i in range(10):           
        time.sleep(1)
        c=sta_if.isconnected()
        print('.', end='')
        if c:
            x= sta_if.ifconfig()[0]
            print( f"\nverbunden als :{x} mit {sta_if.ifconfig()[2]}" )
            break


# suchen
stns=sta_if.scan()    # Scan for available access points

#sortieren nach feldstaerke
stns_sorted= sorted(stns, key=lambda x: x[3], reverse=True) 

ssid_gefunden=[]
for i in stns_sorted:
    ssid_gefunden.append(i[0].decode())
#print (ssid_gefunden)

#pruefen ,ob für die gefundene ssid ein pw in der list ist

pw1=None
id1=None
for i in range(len(id.ssid)):
    for s2 in ssid_gefunden:
        if id.ssid[i] == s2:
            pw1=id.pw[i]
            id1=id.ssid[i]
if id1==None:
    assert 0,' kein bekanntes wlan gefunden, bitte "config.py" anpassen'
else:
    #gefunden
    s= f' wlan "{id1}"; "{pw1}" gefunden'
    print (s)
    start(id1,pw1)



