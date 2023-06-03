#config.py

'''hier moegliche ssid und passwort in der form
      SSID : Passwort 
eintragen'''
wifi={
    'ssid1':'pw1',
    'ssid2':'pw2',
    # SSID : Passwort 
}

class id:
    ssid= []
    pw  = []

for i in wifi.keys():
    id.ssid.append(i)
    id.pw.append(wifi.get(i))
