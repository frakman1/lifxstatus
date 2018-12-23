# lifxstatus
LIFX IM Status Updater.

Continuously monitors your IM status and sets your LIFX colour to match it. 

e.g. Available = Green Light, Away = Yellow Light etc.

**Never miss a meeting again.** See [demo](https://youtu.be/FoNCXtaVobA)


- Currently only supports Microsoft Lync and Cisco Jabber IM clients.
- Works on the MAC Only. 
- Tested with python 2.7.11 on MacBookPro running El Capitan.
- Uses applescript to extract IM client's status info. Python script then handles output and controls lights accordingly.


## Prerequisites:

* colour - Colour Convertions and Manipulations  (https://pypi.python.org/pypi/colour/)

* lazylights - The actual LIFX driver.  https://github.com/mpapi/lazylights/tree/2.0

(Be sure to install the 2.0 branch of lazylights)
```pip install git+https://github.com/mpapi/lazylights@2.0```

* Around line 16 *(createBulb('192.168.1.x','XX:XX:XX:XX:XX:XX'))* , Replace both the IP address and **'XX:XX:XX:XX:XX:XX'** with the MAC addresses of your bulbs. You should be able to find the MAC Address on the bulb itself, or on your router page, or by using my iOS app [LIFX Ambience](https://itunes.apple.com/us/app/lifx-ambience/id1012474625?mt=8)

(a couple of other small python utlities but you can just 'pip install' those easily)

## Syntax:

```
python lifxscreen.py
```
