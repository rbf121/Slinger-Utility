# Slinger-Utility
Python utility methods to help set up GerryDazoo/Slinger

Currently supports DecryptPassword, EncryptPassword from SlingplayerAX COM library. It uses Pywin32 to use the DLL/COM objects from WebSlingPlayer installation.

Latest version also include decryption methods used in slinger which does not require SlingplayerAX to be installed.  As well as helper search functions to find the JSON string in the console.log or .localstorage file (part of Slingplayer Desktop output).  It can also take a .json input containing the "memberslingbox" JSON that was obtained before Nov 9 shutdown.  Search utility will then output each box into a format used in Slinger.  It will decrypt all passwords by including -d option.  It can also identify which type of slingbox it is.

## **Memberslingbox Search**
To use:
```
python slinger_utility.py -d --search console.log
python slinger_utility.py -d --search http_apollo.slingbox.com_0.localstorage
python slinger_utility.py -d --search memberslingbox.json

Or directly accessing install location:
python slinger_utility.py -d --search "%appdata%\Sling Media\Slingplayer Desktop\Logs\console.log"  
python slinger_utility.py -d --search "%appdata%\Sling Media\Slingplayer Desktop\cefCache\Local Storage\http_apollo.slingbox.com_0.localstorage"
```
Example output:
```
Searching file for Slingbox passwords
Searching log file for Slingbox passwords
313 total entries found in console.log
1 unique entries found

var sling_account_boxes=
 {'memberslingbox': [removed]

Attempting to match local found boxes with memberslingbox data
3 sling boxes found in memberslingbox
0 boxes found on local network
Creating Slinger unified_config.ini settings:

[SLINGBOXES]
sb1=BOX1
sb2=BOX2
sb3=BOX3

[BOX1]
;My Slingbox
;Slingbox 500
sbtype="350/500/M1"
;password=E1:[removed]
password=[removed]
;finderid=[removed]
ipaddress=
port=


[BOX2]
;Living room slingbox
;Slingbox M1
sbtype="350/500/M1"
;password=E1:[removed]
password=[removed]
;finderid=[removed]
ipaddress=
port=


[BOX3]
;Basement Slingbox
;Slingbox M1
sbtype="350/500/M1"
;password=E1:[removed]
password=[removed]
;finderid=[removed]
ipaddress=
port=
```

## **Requirements for Slingplayer AX decryption**
- Windows machine
- Python 3.x 32 bit interpretor
- Pywin32
  - python -m pip install pywin32
- WebSlingPlayer 2.4.0.157
  - http://autoupdate.sling.com/plugin_binary/downloads/msi/2.4.0.157/WBSP_IE_Setup.exe
  
### **Decrypt / Encrypt Usage**

  ```python slinger_utility.py --decrypt```
  
  - Enter password to decrypt: 028500CA99D23BDC00EA62B380DB1643

  ```python slinger_utility.py --encrypt 'admin'```
  
  
#### **Sample Output**
```
  python slinger_utility.py -d
  
  Enter password to decrypt:E1:028500CA99D23BDC8BDD941805EC7468

  Input Password: [E1:028500CA99D23BDC8BDD941805EC7468]

  Decrypted Password: [admin]
```

### **Instructions to generate the SlingplayerAX python code yourself**
- Run: python -m win32com.client.combrowse
- Confirm 'SlingPlayerAX 1.0 Type Library' is in the list
- Run: python -m win32com.client.makepy -i
- Select: SlingPlayerAX 1.0 Type Library [1.0]
- The python code should be available in your gen_py Temp folder
- Generated python file should match slingplayerax.py
