#!/usr/bin/env python
print "                                                                               "
print "                                                                               "
print "             .o oOOOOOOOo                                            OOOo      "
print "             Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO     "
print "             OboOOOOOOOOOOOOO.OOo. .oOOOOOo.    OOOo.oOOOOOo..OOOOOOOOO'OO     "
print "             OOP.oOOOOOOOOOOO OPOOOOOOOOOOOo.   `OOOOOOOOOOP,OOOOOOOOOOOB'     "
print "             `O'OOOO'     `OOOOoOOOOOOOOOOOO` .adOOOOOOOOOOoOOO'    `OOOOo     "
print "             .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO     "
print "             OOOOO                 OOOOOOOOOOOOOOOOOOO`                oOO     "
print "            oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.   Ghost mode"
print "           oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO  "
print "          OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOOO`  OOOOOOOOOOOOOOO.OOOOOOOOOOOOOO   "
print "          OOOOOO       OYOoOOOOMOIONODOOO`  .   OOOOROAOPOEOOOoOYO     OOOO    "
print "             Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`     "
print "             :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?                "
print "                          oOOP0%OOOOOOOOoOOOOOOO?oOOOOO?OOOOOOOo               "
print "                          '%o  OOOOO%OOOO%O%OOOOOOOOOOOOOOOO':                 "
print "                               `$S  `OOOO' `OOY ' `OOOOO  oO                   "
print "                                      OPP          :Oo                         "
print "                                                                               "
print " [*] Coded by adnane tebbaa                                                    "
print " [*] for more info visit www.techni-world.com                                  "
print "                                                                               "
import requests, os, sys, tempfile, subprocess, base64, time

if len(sys.argv) != 2:
    print 'usage: ' + sys.argv[0] + ' [country name]'
    exit(1)
country = sys.argv[1]

if len(country) == 2:
    i = 6 
elif len(country) > 2:
    i = 5 
else:
    print 'Country is too short!'
    exit(1)

try:
    vpn_data = requests.get('http://www.vpngate.net/api/iphone/').text.replace('\r','')
    servers = [line.split(',') for line in vpn_data.split('\n')]
    labels = servers[1]
    labels[0] = labels[0][1:]
    servers = [s for s in servers[2:] if len(s) > 1]
except:
    print 'Cannot get VPN servers data'
    exit(1)

desired = [s for s in servers if country.lower() in s[i].lower()]
found = len(desired)
print 'Found ' + str(found) + ' servers for country ' + country
if found == 0:
    exit(1)

supported = [s for s in desired if len(s[-1]) > 0]
print str(len(supported)) + ' of these servers support ghostmodevpn'
winner = sorted(supported, key=lambda s: float(s[2].replace(',','.')), reverse=True)[0]

print "\n== Best server =="
pairs = zip(labels, winner)[:-1]
for (l, d) in pairs[:4]:
    print l + ': ' + d

print pairs[4][0] + ': ' + str(float(pairs[4][1]) / 10**6) + ' MBps'
print "Country: " + pairs[5][1]

print "\ -vpn connected "
_, path = tempfile.mkstemp()

f = open(path, 'w')
f.write(base64.b64decode(winner[-1]))
f.write('\nscript-security 2\nup /etc/openvpn/update-resolv-conf\ndown /etc/openvpn/update-resolv-conf')
f.close()


try:
    while True:
        time.sleep(1)

except:
    try:
        x.kill()
    except:
        pass
        time.sleep(1)
    print '\nVPN terminated'