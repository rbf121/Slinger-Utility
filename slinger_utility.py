import sys
import getopt
import win32com.client as client
import slingplayerax

argv = sys.argv[1:]
try:
    slingPlayer: slingplayerax.ISlingPlayer = client.Dispatch(slingplayerax.SlingPlayer.CLSID)

    options, args = getopt.getopt(argv, "d:e:l:",
                               ["decrypt",
                                "encrypt", "list"])
    for name, value in options:
        if name in ['-d', '--decrypt']:
            password = sys.argv[2]
            if (password.startswith('E1:')==False):
                password = "E1:" + password
            print("Encrypted Password: [" + password+']')
            print("Decrypted Password: [" + slingPlayer.DecryptPassword(password)+']')
        elif name in ['-e', '--encrypt']:
            password = sys.argv[2]

            print("Decrypted Password: [" + password+']')
            print("Encrypted Password: [" + slingPlayer.EncryptPassword(password)+']')
        elif name in ['-l','--list']:
            print(slingPlayer.Discover())
except Exception as e:
    print('Exception occurred:', e)
    print('Check version of python, win32com requires 32 bit version')
 

