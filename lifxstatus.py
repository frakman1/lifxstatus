import re
import os
import sys
import commands
import lazylights
from colour import Color
import binascii
import time


#------------------------------------------------------------------------------------------------------------
# I use this to manually create a bulb using IP and MAC address. 
def createBulb(ip, macString, port = 56700):        
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
#------------------------------------------------------------------------------------------------------------	
myBulb1 = createBulb('192.168.1.x','xx:xx:xx:xx:xx:xx')  
myBulb2 = createBulb('192.168.1.x','xx:xx:xx:xx:xx:xx')  
myBulb3 = createBulb('192.168.1.x','xx:xx:xx:xx:xx:xx')  
bulbs=[myBulb1,myBulb2,myBulb3]


ans=True
while ans:
    print ("""
    1.Microsoft Lync
    2.Cisco Jabber
    q.Exit/Quit
    """)
    ans=raw_input("Which Mac IM Client do you wish to support? ") 
    if ans=="1": 
      print("\n Microsoft Lync.") 
      break
    elif ans=="2":
      print("\n Cisco Jabber.") 
      break
    elif ans=="q":
      print("\n Goodbye.") 
      exit(0)
    elif ans !="":
      print("\n Not Valid Choice Try again") 



#============= Run once =================================
if ans=="1":
    cmd = 'osascript Lync.applescript'
elif ans =="2":
    cmd = 'osascript Jabber.applescript'
appleout = (commands.getstatusoutput(cmd))
status = appleout[1]
savedStatus = status
firstTime = True
N = 0;  # counter to fire every Nth time
#==============================================

while True:
    time.sleep(1)
    #Get Lync Status
    #cmd = 'osascript Lync.applescript'  
    appleout = (commands.getstatusoutput(cmd))

    try:
        status = appleout[1]
    except IndexError:
        print "error parsing"
    
    
    print status
    N += 1
    if (status == savedStatus) and (firstTime == False) and ( N % 10):
        print "No Change."
        continue
   
    print "********************** Periodic Check  *******************"  
    try:
        lazylights.set_power(bulbs,True)
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print("Unexpected error:", sys.exc_info()[0])
    
      
    if (status == 'Available'):
        print "Status Detected!(%s)" % status
        c = Color("green")

    elif (status == 'Busy') or (status == 'Do Not Disturb') or (status == 'In a Meeting'):
        print "Status Detected!(%s)" % status
        c = Color("red")
        
    elif (status == 'Away') or (status == 'Be Right Back') or (status == 'Off Work'):
        print "Status Detected(%s)" % status
        c = Color("yellow")

    try:
        lazylights.set_state(bulbs,c.hue*360,(c.saturation),1,0,(1000),False);
    except: # catch *all* exceptions
        e = sys.exc_info()[0]
        print("Unexpected error:", sys.exc_info()[0])


    savedStatus = status
    firstTime = False
    
