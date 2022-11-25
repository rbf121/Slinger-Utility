# Slinger-Utility
Python utility methods to help set up GerryDazoo/Slinger

Currently supports DecryptPassword, EncryptPassword and Discover. It uses Pywin32 to use the DLL/COM objects from WebSlingPlayer installation.

**Requirements for decryption **
- Windows machine
- Python 3.11 32 bit interpretor
- Pywin32
  - python -m pip install pywin32
- WebSlingPlayer 2.4.0.157
  - http://autoupdate.sling.com/plugin_binary/downloads/msi/2.4.0.157/WBSP_IE_Setup.exe
  
**Decrypt / Encrypt Usage**

  python slinger_utility.py --decrypt
  
  - Enter password to decrypt: 028500CA99D23BDC00EA62B380DB1643

  python slinger_utility.py --encrypt 'admin'
  
**Password Search**
  
  python slinger_utility.py --search console.log
  
  python slinger_utility.py --db http_apollo.slingbox.com_0.localstorage
  
  **Or if you are on Windows and want to try and have it access your Slingplayer Desktop files directly**
  
  python slinger_utility.py --search "%appdata%\Sling Media\Slingplayer Desktop\Logs\console.log"
  
  python slinger_utility.py --db "%appdata%\Sling Media\Slingplayer Desktop\cefCache\Local Storage\http_apollo.slingbox.com_0.localstorage"
  
  You can also add -d to also decrypt the password in the output:
  ex. 
  python slinger_utility.py -d --search "%appdata%\Sling Media\Slingplayer Desktop\Logs\console.log"
  
  python slinger_utility.py -d --db "%appdata%\Sling Media\Slingplayer Desktop\cefCache\Local Storage\http_apollo.slingbox.com_0.localstorage"
  
**Sample**

  python slinger_utility.py -d
  
  Enter password to decrypt:E1:028500CA99D23BDC8BDD941805EC7468

  Input Password: [E1:028500CA99D23BDC8BDD941805EC7468]

  Decrypted Password: [admin]

**Instructions to generate the python code yourself**
- Run: python -m win32com.client.combrowse
- Confirm 'SlingPlayerAX 1.0 Type Library' is in the list
- Run: python -m win32com.client.makepy -i
- Select: SlingPlayerAX 1.0 Type Library [1.0]
- The python code should be available in your gen_py Temp folder
- Generated python file should match slingplayerax.py
