import sys
import getopt
import re
import json
import win32com.client as client
import slingplayerax
import sqlite3
from configparser import ConfigParser

def decryptPassword(encryptedPassword):
    #Calls the SlingPlayerAX plugin to decrypt password
    slingPlayer: slingplayerax.ISlingPlayer = client.Dispatch(slingplayerax.SlingPlayer.CLSID)
    return slingPlayer.DecryptPassword(encryptedPassword)

def encryptPassword(password):
    #Calls the SlingPlayerAX plugin to encrypt password
    slingPlayer: slingplayerax.ISlingPlayer = client.Dispatch(slingplayerax.SlingPlayer.CLSID)
    return slingPlayer.EncryptPassword(password)

argv = sys.argv[1:]
outputFile = ''
decrypt = False
try:
    options, args = getopt.getopt(argv, "de:s:m:o:",
                               ["decrypt",
                                "encrypt=",
                                "search=",
                                "db=",
                                "m3u=",
                                "output="])

    for name, value in options:
        if name in ['-o','--output']:
            outputFile = value
        elif name in ['-d', '--decrypt']:            
            if(len(sys.argv)>3):
                decrypt=True
            else:
                password = input('Enter password to decrypt:')
                if (password.startswith('E1:')==False):
                    password = "E1:" + password
                print('Input Password: [' + password+']')
                print('Decrypted Password: [' + decryptPassword(password)+']')
        elif name in ['-e', '--encrypt']:
            password = value
            print('Input Password: [' + password+']')
            print('Encrypted Password: [' + encryptPassword(password)+']')
        elif name in ['-s', '--search']:
            print('Searching file for Slingbox passwords')
            fp = open(value, encoding='utf8', mode='r')
            content = fp.read()
            fp.close()
            matches = re.findall("(?i)(?<=\"password\")(?:\s*:\s*)(\".*?(?=\")\")", content)
            #print(matches)
            matchSet = set(matches)
            print(len(matchSet), 'found in',value)
            for each in matchSet:
                #print(each)
                each = each.replace('\"','')
                if each.startswith('E1:') and decrypt==True:
                    try:
                        print(';password='+ each)
                        print('password=' + decryptPassword(each))
                    except:
                        print(';could not decrypt, check python version')
                        print('password='+ each)
                elif each:
                    print('password=' + each)
        elif name in ['--db']:
            print('Searching for slingbox accounts in localstorage: ['+value+']')
            conn = sqlite3.connect(value)
            cursor = conn.cursor()
            res = cursor.execute("SELECT value FROM ItemTable where key='accountBoxes'")
            ablob = res.fetchone()
            accountBoxes = json.loads(ablob[0])
            if accountBoxes:
                print("\nFound accountBoxes JSON string:")
                #print(accountBoxes)
                print(len(accountBoxes[0]['memberslingbox']),'boxes found')
                for each in accountBoxes[0]['memberslingbox']:
                    print(';'+each['displayName'])
                    adminPassword = each['adminPassword']
                    print(';password='+adminPassword)
                    if adminPassword.startswith('E1:') and decrypt==True:
                        try:
                            print('password=' + decryptPassword(adminPassword))
                        except:
                            print(';could not decrypt, check python version')

                    print(';finderid='+each['slingbox']['finderId'])
                    print('\n')
                    
                #for each in accountBoxes:
                #    print(each.get('memberslingbox'))
                if outputFile:
                    fp = open(outputFile,'w')
                    fp.write(str(accountBoxes))
                    fp.close()
                    print('JSON output file saved to', outputFile)
                else:
                    print('JSON Found in DB:')
                    print(accountBoxes)                
            else:
                print('No match')
                
            cursor.close()
            conn.close()
        elif name in ['--m3u']:
                host = input('Enter servername:')
                if not host:
                    host = 'localhost'
                boxName = input('Enter box name:')
                cp = ConfigParser()
                cp.read(value)
                serverinfo = cp['SERVER']
                start = 1
                end = 360
                m3uChannelListing = ''
                if cp.has_section('M3U'):
                    m3uOptions = cp['M3U']
                    start = int(m3uOptions.get('m3uStartRange', 1))
                    end = int(m3uOptions.get('m3uEndRange', 360))
                    m3uChannelListing = m3uOptions.get('m3uChannelListing', '')

                urlBase = serverinfo.get('URLbase', 'slingbox')
                port = serverinfo.get('port','8080')

                if cp.has_section(boxName):
                    # matched pattern for multiple boxes
                    path = f'{urlBase}/{boxName}'
                else:
                    path = 'slingbox'
                    boxName = 'Slingbox'
                
                #Construct M3U channels
                m3u = '#EXTM3U\n'
                if m3uChannelListing:
                    f = open(m3uChannelListing, 'r')
                    channelList= json.loads(f.read())
                    for each in channelList:
                        channel = each.get('channel')
                        affiliate = each.get('affiliate')
                        if affiliate:
                            channelName = affiliate
                        else:
                            channelName = each['name']
                        channelName = channelName.replace(',','')
                        m3u += f'#EXTINF:-1 tvg-chno=\"{channel}\" tvg-id=\"{channelName}\" CUID=\"{channel}\" tvg-name="{channelName}\" tvg-logo=\"\" group-title=\"{boxName}\",{channelName}\n'
                        m3u += f'http://{host}:{port}/{path}?channel={int(channel)}\n\n'
                else:
                    for i in range (start, end+1):
                        channel = i
                        channelName = f'{urlBase} {boxName} Channel {i}'
                        m3u += f'#EXTINF:-1 tvg-chno=\"{channel}\" tvg-id=\"{channelName}\" CUID=\"{channel}\" tvg-name="{channelName}\" tvg-logo=\"\" group-title=\"{boxName}\",{channelName}\n'
                        m3u += f'http://{host}:{port}/{path}?channel={i}\n\n'
                
                if outputFile:
                    fp = open(outputFile,'w')
                    fp.write(m3u)
                    fp.close()                  
                else:
                    print(m3u)

except Exception as e:
    print('Exception occurred:', e)
 

