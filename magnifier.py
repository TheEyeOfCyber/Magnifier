#!/usr/bin/env python
# magnifier . Version 1.0
# magnifier - Information Gathering Tool
############################################
# Coder   : Humayun Ali Khan @ Black Tiger
############################################
from urllib2 import *
from platform import system
import sys
def clear():
    if system() == 'Linux':
        os.system("clear")
    if system() == 'Windows':
        os.system('cls')
        os.system('color a')
    else:
        pass
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
banner = '''
\033[37m
                      ```.--:::::::--..```                                                          
                 `.-::/+++oooo++++///:::---..``                                                     
              .-:///++//::---.......------..```...                                                  
           .://////:--....................--..````--.                                               
         .//////:-.......``````````````.......--.``.-:.                                             
       .//////:-....````````````````````````````.---.-::.                                           
      -/////:....`````````            `````      `.:::-:/-                                          
    `:///+/-...```````                           ``..:/://:`                                        
   `://++:...``````                           ```    .:+//+:`                                       
  `://+o-...`````                                `    `-++++:`                                      
  -/++o-...`````                                  ` ```.-oooo-                                      
 `/+++:...````                                    ````...:oss+`                                     
 -+++/...````                                      ````.../oso-                                     
 /+o/-..`````                                      `````..-+oo/                                     
`+oo:...````                                        ````...:oo+`                                    
-oo+-...````                                        ````...-+++.                                    
-o+/....````                                        ````..../+/-                                    
:++/....````                                        ````....///-                                    
-///`...````                                        ````...`//:-                                    
./::.....````                                      ````....-::/.                                    
 /:--....`````                                    `````....:::/                                     
 ./-..-...`````                                  `````...-:::/.                                     
  ::.`.-...`````                                `````...-::-/:                                      
   /-``.:.`.``````                            ``````...::--:/                                       
    :-``.:-``.``````                        ``````...-::--::                                        
     -:``.::.``.````````                ````````.``.:/---/-                                         
      `:-..-/:.``````````````````````````````````.:/:--:/`                                          
        .:---:/:-``````````````````````````````-:/:---:-.-....                                      
          .-:::///-..``````````````````````..-::----:/:-...-`:y:                                    
            `.://+++/:-..``````````````..---------.``-//:-.`-..oy:                                  
               `.-/+oosso+/::---------:::::---..`     -:/::oss/.-os:                                
                   `.-:/++++++++////:::--..``         ./sysoosss/.-os:                              
                         ```......`````                `/yhysoosso/.-os-                            
                                                         `/yhysoosso/.-os-                          
                                                           `/yhyooosso:.-os-                        
                                                             ./yhyoossso:.-ss-                      
                                                               .+yhyoossso:.:so-                    
                                                                 .+yhyoossso:.:so-                  
                                                                   .+yhyoossso:.:so-                
                                                                     .+hhyoossso:.:so.              
                                                                       .+hhyoossso:.:so.            
                                                                         .+hhyoossso-.:so.          
                                                                           .ohhyoossso-./s+.        
                                                                             .ohhyoossso-./y+.      
                                                                               -ohhyoosss+-./y+.    
                                                                                 -ohhsoosss+-`/y+   
                                                                                   -ohhsoosss+-.s   
                                                                                     -shhsoossy+`    \033[37m             
|'....      ....\033[93m magnifier \033[91m - \033[92m Information Gathering Tool \033[91m
==[[ .:: Name : magnifier ::.]]==\033[91m
==[[ .:: Version: 1.0 ::.]]==\033[96m
==[[ .:: Author : Humayun Ali Khan @ Black Tiger::.]]==\033[92m
'''
print (banner)
def menu():
   print'''
\033[91m 1 \033[96m} \033[91m ==\033[93m> \033[92m DNS Lookup 
\033[91m 2 \033[96m} \033[91m ==\033[93m> \033[92m Whois Lookup
\033[91m 3 \033[96m} \033[91m ==\033[93m> \033[92m GeoIP Lookup
\033[91m 4 \033[96m} \033[91m ==\033[93m> \033[92m Subnet Lookup
\033[91m 5 \033[96m} \033[91m ==\033[93m> \033[92m Port Scanner
\033[91m 6 \033[96m} \033[91m ==\033[93m> \033[92m Extract Links 
\033[91m 7 \033[96m} \033[91m ==\033[93m> \033[92m Zone Transfer
\033[91m 8 \033[96m} \033[91m ==\033[93m> \033[92m HTTP Header
\033[91m 9 \033[96m} \033[91m ==\033[93m> \033[92m Host Finder
\033[91m 10\033[96m} \033[91m ==\033[93m> \033[92m IP-Locator
\033[91m 11\033[96m} \033[91m ==\033[93m> \033[92m Traceroute
\033[91m 12\033[96m} \033[91m ==\033[93m> \033[92m Robots.txt
\033[91m 13\033[96m} \033[91m ==\033[93m> \033[92m Host DNS Finder
\033[91m 14\033[96m} \033[91m ==\033[93m> \033[92m Revrse IP Lookup
\033[91m 15\033[96m} \033[91m ==\033[93m> \033[92m Collection Email
\033[91m 16\033[96m} \033[91m ==\033[93m> \033[92m Subdomain Finder 
\033[91m 17\033[96m} \033[91m ==\033[93m> \033[92m Install & Update
\033[91m 18\033[96m} \033[91m ==\033[93m> \033[92m About Me 
\033[91m 00\033[96m} \033[91m ==\033[93m> \033[92m Exit
'''

slowprint("\033[1;91mThis Is Simple Script By :\033[92m Humayun Ali Khan @ Black Tiger" + "\n \033[93m Let's Start \033[96m --> --> --> \033[91m ")

menu()
def ext():
    ex = raw_input ('\033[92mContinue/Exit->-> ')
    if ex[0].upper() == 'E' :
           print 'Good-bye!!!'
           exit()
    else:
           clear()
           print (banner)
           menu()
           select()

def  select():
  try:
    magnifier = input("\033[96mEnter \033[92m00/\033[91m18 => =>  ")
    if magnifier == 2:
      dz = raw_input('\033[91mEnter IP Address : \033[91m')
      whois = "http://api.hackertarget.com/whois/?q=" + dz
      dev = urlopen(whois).read()
      print (dev)
      ext()
    elif magnifier == 14:
      dz = raw_input('\033[92mEnter IP Address : \033[92m')
      revrse = "http://api.hackertarget.com/reverseiplookup/?q=" + dz
      lookup = urlopen(revrse).read()
      print (lookup)
      ext()
    elif magnifier == 1:
      dz = raw_input('\033[96mEnter Your Domain :\033[96m')
      dns = "http://api.hackertarget.com/dnslookup/?q=" + dz
      magnifier = urlopen(dns).read()
      print (magnifier)
      ext()
    elif magnifier == 3:
      dz = raw_input('\033[91mEnter IP Address : \033[91m')
      geo = "http://api.hackertarget.com/geoip/?q=" + dz
      ip = urlopen(geo).read()
      print (ip)
      ext()
    elif magnifier == 4:
      dz = raw_input('\033[92mEnter IP Address : \033[92m')
      sub = "http://api.hackertarget.com/subnetcalc/?q=" + dz
      net = urlopen(sub).read()
      print (net)
      ext()
    elif magnifier == 5:
      dz = raw_input('\033[96mEnter IP Address : \033[96m')
      port = "http://api.hackertarget.com/nmap/?q=" + dz
      scan = urlopen(port).read()
      print (scan)
      ext()
    elif magnifier == 6:
      dz = raw_input('\033[91mEnter Your Domain :\033[91m')
      get = "https://api.hackertarget.com/pagelinks/?q=" + dz
      page = urlopen(get).read()
      print(page)
      ext()
    elif magnifier == 7:
      dz = raw_input('\033[92mEnter Your Domain :\033[92m')
      zon = "http://api.hackertarget.com/zonetransfer/?q=" + dz
      tran = urlopen(zon).read()
      print (tran)
      ext()
    elif magnifier == 8:
      dz = raw_input('\033[96mEnter Your Domain :\033[96m')
      hea = "http://api.hackertarget.com/httpheaders/?q=" + dz
      der =  urlopen(hea).read()
      print (der)
      ext()
    elif magnifier == 9:
      dz = raw_input('\033[91mEnter Your Domain :\033[91m')
      host = "http://api.hackertarget.com/hostsearch/?q=" + dz
      finder = urlopen(host).read()
      print (finder)
      ext()
    elif magnifier == 10:
      dz = raw_input('\033[91mEnter Your IP Address :\033[91m')
      host = "http://ip-api.com/json/" + dz
      kader = urlopen(host).read()
      print (kader)
      ext()
    elif magnifier== 11:
      dz = raw_input('\033[1;91mEnter Domain: \033[1;m')
      host = "http://api.hackertarget.com/findshareddns/?q=" + dz
      dns = urlopen(host).read()
      print (dns)
      ext()
    elif magnifier == 13:
      dz = raw_input('\033[91mEnter Your Domain :\033[91m')
      get = "https://api.hackertarget.com/mtr/?q=" + dz
      page = urlopen(get).read()
      print(page)
      ext()
    elif magnifier == 12:
      dz = raw_input('\033[91mEnter Your Domain :\033[91m')
      path = os.getcwd()
      os.system('cd ' +  path  + '/modules && python2 goofile.py -d %s -f txt' % dz)
      ext()
    elif magnifier == 15:
      dz = raw_input('\033[91mEnter Your Domain :\033[91m')
      path = os.getcwd()
      os.system('cd ' +  path  + '/modules && python2 theHarvester.py -d %s -b all' % dz)
      ext()
    elif magnifier == 16:
      dz = raw_input('\033[91mEnter Your Domain :\033[91m')
      print '-+-+-+-+-+-+-+-+-+-+-+-+-+-+-'
      path = os.getcwd() 
      os.system('cd ' +  path  + '/modules && python2 sub.py -t %s -l fr ' % dz)    
      ext()
    elif magnifier == 17:
      path = os.getcwd() 
      os.system('cd ' +  path  + ' && bash install')     
      os.system('cd ' +  path  + ' && python2 update.py')
      ext()
    elif magnifier == 18:
      slowprint("............... ")
      slowprint("Name : magnifier \033[92m")
      slowprint("...............")
      slowprint("Version : 1.0 \033[91m")
      slowprint(".............")
      slowprint("Author: Humayun Ali Khan @ magnifier \033[96m")
      slowprint("......................")
      slowprint("GitHub: https://github.com/TheEyeOfCyber/Magnifier")
      slowprint("......................")
      slowprint("YouTube: https://www.youtube.com/channel/UCEkclbUf3LMNkVOJ9_ln-mA")
      slowprint("......................")
      slowprint("Facebook: https://www.facebook.com/theeyeofcyber1")
      slowprint("......................")
      ext()
    elif  magnifier == 00:
      print "Allah Hafiz!!"
  except(KeyboardInterrupt):
    print "\nCtrl + C -> Exiting!!"
select()
