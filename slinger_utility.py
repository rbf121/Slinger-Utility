import sys
import getopt
import re
import json
import win32com.client as client
import slingplayerax
import sqlite3
from configparser import ConfigParser
from ctypes import *

def decipher(v, k):
    'decipher method from GerryDazoo/Slinger'
    y = c_uint32(v[0])
    z = c_uint32(v[1])
    sum = c_uint32(0xc6ef3720)
    delta = 0x9e3779b9
    n = 32
    w = [0, 0]

    while (n > 0):
        z.value -= (y.value << 4) + k[2] ^ y.value + \
            sum.value ^ (y.value >> 5) + k[3]
        y.value -= (z.value << 4) + k[0] ^ z.value + \
            sum.value ^ (z.value >> 5) + k[1]
        sum.value -= delta
        n -= 1

    w[0] = y.value
    w[1] = z.value
    return w


def Decrypt(data, key):
    'Decrypt method from GerryDazoo/Slinger'
    bytes = b''
    info = [int.from_bytes(data[i:i+4], byteorder='little')
            for i in range(0, len(data), 4)]
    for i in range(0, len(info), 2):
        chunk = [info[i], info[i+1]]
        cleartext = decipher(chunk, key)
        bytes = bytes + \
            cleartext[0].to_bytes(4, byteorder='little') + \
            cleartext[1].to_bytes(4, byteorder='little')
    return bytes


def decryptPassword(encryptedPassword):
    'decryptPassword using methods from GerryDazoo/Slinger'
    skey = [0xBCDEAAAA, 0x87FBBBBA, 0x7CCCCFFA, 0xDDDDAABC]
    pw = encryptedPassword.upper().replace('E1:', '').strip()
    try:
        pw_bytes = bytearray.fromhex(pw)
        clear = Decrypt(pw_bytes, skey)
    except Exception as e:
        print('Bad E1: Password cannot decrypt. Missing/bad characters?', e)
    return clear.decode('utf8').replace('\u0000', '')


def decryptPasswordAX(encryptedPassword):
    'Calls the SlingPlayerAX plugin to decrypt password'
    slingPlayer: slingplayerax.ISlingPlayer = client.Dispatch(
        slingplayerax.SlingPlayer.CLSID)
    return slingPlayer.DecryptPassword(encryptedPassword)


def encryptPasswordAX(password):
    'Calls the SlingPlayerAX plugin to encrypt password'
    slingPlayer: slingplayerax.ISlingPlayer = client.Dispatch(
        slingplayerax.SlingPlayer.CLSID)
    return slingPlayer.EncryptPassword(password)


def searchConsoleLog(log):
    'Search console log for passwords and accountBox info'
    print('Searching log file for Slingbox passwords')
    fp = open(log, encoding='utf8', mode='r')
    content = fp.read()
    fp.close()
    #matches = re.findall("(?i)(?<=\"password\")(?:\s*:\s*)(\".*?(?=\")\")", content)
    matches = re.findall(
        "showMergeListInDirectory:.\[.*\],(\[.*\]),.*\n", content)
    #matches = re.findall("showMergeListInDirectory:.(\[.*\])\n", content)
    # print(matches)
    print(len(matches), "total entries found in", log)
    matchSet = set(matches)
    print(len(matchSet), 'unique entries found\n')

    for match in matchSet:
        #print('JSON string found in console log:\n', match, '\n')
        jsonString = json.loads(match)
        memberSlingbox = {}
        for each in jsonString:
            finderId = each['finderId']
            memberSlingbox[finderId.lower()] = each
            memberSlingbox[finderId.lower(
            )]['displayName'] = memberSlingbox[finderId.lower()]['name']
            memberSlingbox[finderId.lower(
            )]['adminPassword'] = memberSlingbox[finderId.lower()]['password']
            del memberSlingbox[finderId.lower()]['id']
            del memberSlingbox[finderId.lower()]['name']
            del memberSlingbox[finderId.lower()]['password']
        slingAccountBoxes = {}
        slingAccountBoxes['memberslingbox'] = memberSlingbox
        slingAccountBoxes['size'] = len(slingAccountBoxes['memberslingbox'])
        print('var sling_account_boxes=\n', slingAccountBoxes, '\n')
    # print(jsonSet)
    return slingAccountBoxes


def searchLocalDB(localstorage):
    'Search Slingplayer Desktop SQLite3 localstorage'
    print(
        'Searching for slingbox accounts in localstorage: ['+localstorage+']')
    conn = sqlite3.connect(localstorage)
    cursor = conn.cursor()
    res = cursor.execute(
        "SELECT value FROM ItemTable where key='accountBoxes'")
    ablob = res.fetchone()
    accountBoxes = json.loads(ablob[0])
    if accountBoxes:
        print("\nFound accountBoxes JSON string:")
        # print(accountBoxes)
        if type(accountBoxes) is list:
            print(len(accountBoxes[0]['memberslingbox']), 'boxes found')
            #memberSlingbox = accountBoxes[0]
            memberSlingbox = {}
            for each in accountBoxes[0]['memberslingbox']:
                finderId = each['slingbox']['finderId']
                memberSlingbox[finderId.lower()] = each
                memberSlingbox[finderId.lower()]['finderId'] = each['slingbox']['finderId']
                if 'productSignature' in each['slingbox']:
                    productId = int(str(each['slingbox']['productSignature']),16)
                    memberSlingbox[finderId.lower()]['productSignature'] = productId
                del memberSlingbox[finderId.lower()]['slingbox']
                    
            slingAccountBoxes = {}
            slingAccountBoxes['memberslingbox'] = memberSlingbox
            slingAccountBoxes['size'] = accountBoxes[0]['size']
            print(slingAccountBoxes)
    else:
        print('No match')
    cursor.close()
    conn.close()
    return slingAccountBoxes


def checkAccountBoxes(accountBoxes, localBoxes):
    'Uses finderids to combine account box info with local box info found via Slinger (ip, port)'
    print('Attempting to match local found boxes with memberslingbox data')
    print(len(accountBoxes['memberslingbox']), 'sling boxes found in memberslingbox')
    print(len(localBoxes), 'boxes found on local network')

    print('Creating Slinger unified_config.ini settings:\n')
    unified_config = '[SLINGBOXES]\n'
    for i in range(len(accountBoxes['memberslingbox'])):
        unified_config += 'sb'+str(i+1)+'=BOX'+str(i+1)+'\n'

    j = 1
    unified_config += '\n'
    for each in accountBoxes['memberslingbox']:
        unified_config += '[BOX'+str(j)+']\n'
        j+=1
        #print(accountBoxes['memberslingbox'][each])
        box = accountBoxes['memberslingbox'][each]

        #Product ID mapping
        productIdDict ={
        "UNKNOWN": "Slingbox",
        0: "Slingbox Classic",
        1: "Slingbox PRO",
        2: "Slingbox Classic",
        3: "Slingbox AV",
        4: "Slingbox TUNER",
        5: "Slingbox Classic",
        6: "Sling MODEM",
        7: "Slingbox SOLO",
        8: "Slingbox PRO-HD",
        9: "922",
        12: "HDS-600RS",
        13: "Slingbox 120",
        14: "Sling Adapter",
        17: "Slingbox 350",
        18: "Slingbox 500",
        32: "Slingbox M1",
        "M2": "Slingbox M2"
    }
        unified_config += ';'+box['displayName']+'\n'

        if 'productSignature' in box:
            productId = box['productSignature']
            unified_config += ';'+ productIdDict[productId] + '\n'
        elif 'productId' in box:
            productId = box['productId']
            unified_config += ';'+ productIdDict[productId]+'\n'


        if productId in [17,18,32]:
            unified_config += 'sbtype=\"350/500/M1\"\n'
        else:
            unified_config += 'sbtype=\"Solo/Pro/ProHD\"\n'


        adminPassword = box['adminPassword']
        unified_config += ';password='+adminPassword + '\n'
        if adminPassword.startswith('E1:') and decrypt == True:
            try:
                box['adminPassword'] = decryptPassword(adminPassword)
                if 'userPassword' in box:
                    box['userPassword'] = decryptPassword(box['userPassword'])
                unified_config += 'password=' + box['adminPassword'] + '\n'
            except:
                unified_config += ';could not decrypt\n'
        else:
            unified_config += 'password='+adminPassword+'\n'
        finderid = box['finderId']
        unified_config += ';finderid=' + finderid +'\n'
        #match = next((i for i in localBoxes if finderid==localBoxes[i][3]),None)

        slingip = ''
        slingport = ''
        if localBoxes:
            for i in localBoxes:
                if finderid.lower() == i[3].lower():
                    slingip = i[0]
                    slingport = i[1]

                    box['ipaddress'] = slingip
                    box['port'] = slingport
                    break
        unified_config += 'ipaddress='+slingip+'\n'
        unified_config += 'port='+str(slingport)+'\n'
        
        unified_config += '\n\n'
    print(unified_config)
    return accountBoxes


def recoverPasswords(file):
    'Returns account box info from Slingplayer Desktop files, supports console.log, *.localstorage or json'
    accountBoxes = {}
    if file.endswith('console.log'):
        accountBoxes = searchConsoleLog(file)
    elif file.endswith('.localstorage'):
        accountBoxes = searchLocalDB(file)
    elif file.endswith('json'):
        f = open(file, encoding='utf8', mode='r')
        accountBoxes = json.load(f)
        f.close()
        print('json')
    else:
        print('Not sure what do with this file.')
    return accountBoxes


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
        if name in ['-o', '--output']:
            outputFile = value
        elif name in ['-d', '--decrypt']:
            if (len(sys.argv) > 3):
                decrypt = True
            else:
                password = input('Enter password to decrypt:')
                if (password.startswith('E1:') == False):
                    password = "E1:" + password
                print('Input Password: [' + password+']')
                print('Decrypted Password: [' + decryptPasswordAX(password)+']')
        elif name in ['-e', '--encrypt']:
            password = value
            print('Input Password: [' + password+']')
            print('Encrypted Password: [' + encryptPasswordAX(password)+']')
        elif name in ['-s', '--search']:
            print('Searching file for Slingbox passwords')
            accountBoxes = recoverPasswords(value)
            localBoxes = []
            #localBoxes.append(('192.168.117.110', '5201', 'Box Name', 'paste_finderid_here'))
            #localBoxes.append(('192.168.117.101', '5203', 'Box Name', 'paste_finderid_here'))
            #localBoxes matches format in Slinger code for later integration
            checkAccountBoxes(accountBoxes, localBoxes)
            if outputFile:
                fp = open(outputFile, 'w')
                fp.write(json.dumps(accountBoxes, indent=4))
                fp.close()
                print('JSON output file saved to', outputFile)
            else:
                print('JSON output:')
                print(json.dumps(accountBoxes, indent=4))
        elif name in ['-p', '--pwsearch']:
            print('Searching file for Slingbox passwords')
            fp = open(value, encoding='utf8', mode='r')
            content = fp.read()
            fp.close()
            matches = re.findall(
                "(?i)(?<=\"password\")(?:\s*:\s*)(\".*?(?=\")\")", content)
            # print(matches)
            matchSet = set(matches)
            print(len(matchSet), 'found in', value)
            for each in matchSet:
                # print(each)
                each = each.replace('\"', '')
                if each.startswith('E1:') and decrypt == True:
                    try:
                        print(';password=' + each)
                        print('password=' + decryptPassword(each))
                    except:
                        print(';could not decrypt, check python version')
                        print('password=' + each)
                elif each:
                    print('password=' + each)
        elif name in ['--db']:
            accountBoxes = searchLocalDB(value)
            localBoxes = []
            checkAccountBoxes(accountBoxes, localBoxes)
            if outputFile:
                fp = open(outputFile, 'w')
                fp.write(json.dumps(accountBoxes, indent=4))
                fp.close()
                print('JSON output file saved to', outputFile)
            else:
                print('JSON Found in DB:')
                print(json.dumps(accountBoxes, indent=4))
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
            port = serverinfo.get('port', '8080')

            if cp.has_section(boxName):
                # matched pattern for multiple boxes
                path = f'{urlBase}/{boxName}'
            else:
                path = 'slingbox'
                boxName = 'Slingbox'

            # Construct M3U channels
            m3u = '#EXTM3U\n'
            if m3uChannelListing:
                f = open(m3uChannelListing, 'r')
                channelList = json.loads(f.read())
                for each in channelList:
                    channel = each.get('channel')
                    affiliate = each.get('affiliate')
                    if affiliate:
                        channelName = affiliate
                    else:
                        channelName = each['name']
                    channelName = channelName.replace(',', '')
                    m3u += f'#EXTINF:-1 tvg-chno=\"{channel}\" tvg-id=\"{channelName}\" CUID=\"{channel}\" tvg-name="{channelName}\" tvg-logo=\"\" group-title=\"{boxName}\",{channelName}\n'
                    m3u += f'http://{host}:{port}/{path}?channel={int(channel)}\n\n'
            else:
                for i in range(start, end+1):
                    channel = i
                    channelName = f'{urlBase} {boxName} Channel {i}'
                    m3u += f'#EXTINF:-1 tvg-chno=\"{channel}\" tvg-id=\"{channelName}\" CUID=\"{channel}\" tvg-name="{channelName}\" tvg-logo=\"\" group-title=\"{boxName}\",{channelName}\n'
                    m3u += f'http://{host}:{port}/{path}?channel={i}\n\n'

            if outputFile:
                fp = open(outputFile, 'w')
                fp.write(m3u)
                fp.close()
            else:
                print(m3u)

except Exception as e:
    print('Exception occurred:', e)
