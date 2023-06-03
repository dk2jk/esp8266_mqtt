from time import ctime

t=ctime()      #'Wed May 31 21:22:24 2023'
t1= t.split()  #['Wed', 'May', '31', '21:22:24', '2023']

monat={'Jan':'Januar',
       'Feb':'Februar',
       'Mar':'März',
       'Apr':'April',
       'May':'Mai',
       'Jun':'Juni',
       'Jul':'Juli',
       'Aug':'August',
       'Sep':'September',
       'Oct':'Oktober',
       'Nov':'November',
       'Dec':'Dezember'}
wochentag={'Mon':'Montag',
           'Tue':'Dienstag',
           'Wed':'Mittwoch',
           'Thu':'Donnerstag',
           'Fri':'Freitag',
           'Sat':'Samstag',
           'Sun':'Sonntag',}

#monat.get('Jan') # 'Januar'
m= monat.get(t1[1])
w= wochentag.get(t1[0])
s= f'{w}, {t1[2]}.{m} {t1[4]} {t1[3]}'
print(s)