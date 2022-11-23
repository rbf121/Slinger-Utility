# Slinger-Utility
Python utility methods to help set up GerryDazoo/Slinger

Currently supports DecryptPassword, EncryptPassword and Discover. It uses Pywin32 to use the DLL/COM objects from WebSlingPlayer installation.

**Requirements**
- Windows machine
- Python 32 bit interpretor
- Pywin32
  - python -m pip install pywin32
- WebSlingPlayer 2.4.0.157
  - http://autoupdate.sling.com/plugin_binary/downloads/msi/2.4.0.157/WBSP_IE_Setup.exe
  
**Usage**

  slinger_utility.py --decrypt '028500CA99D23BDC00EA62B380DB1643'

  slinger_utility.py --encrypt 'admin'

**Sample**

  slinger_utility.py --decrypt '028500CA99D23BDC00EA62B380DB1643'

  Encrypted Password: [E1:028500CA99D23BDC00EA62B380DB1643]

  Decrypted Password: [admin]

**Instructions to generate the python code yourself**
- Run: python -m win32com.client.combrowse
- Confirm 'SlingPlayerAX 1.0 Type Library' is in the list
- Run: python -m win32com.client.makepy -i
- Select: SlingPlayerAX 1.0 Type Library [1.0]
- The python code should be available in your gen_py Temp folder
- Generated python file should match slingplayerax.py
