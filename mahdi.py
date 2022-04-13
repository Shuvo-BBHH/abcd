# Source Generated with Decompyle++
# File: out.pyc (Python 2.7)

import os
import time
import requests
import datetime
import random
import multiprocessing.pool as multiprocessing
import getpass
import json
import threading
import sys
import uuid
import shutil
import zlib
import base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

l1 = '100077'
l2 = '100078'
os.system('rm -rf token.txt')
g = '\x1b[1;92m'
r = '\x1b[1;91m'
w = '\x1b[1;97m'
y = '\x1b[1;93m'
n = '\x1b[1;94m'
gu = '\x1b[1;95m'
sm = '\x1b[1;96m'

try:
    import lolcat
except:
    os.system('pip2 install lolcat')

logo = "'\x1b[1;92m'  _____ ___  ___ _____  _____   ___   ______\n'\x1b[1;92m' |_   _||  \\/  ||_   _||_   _| / _ \\ |___  /\n'\x1b[1;91m'   | |  | .  . |  | |    | |  / /_\\ \\   / / \n'\x1b[1;97m'   | |  | |\\/| |  | |    | |  |  _  |  / /  \n'\x1b[1;93m'  _| |_ | |  | |  | |   _| |_ | | | |./ /___\n'\x1b[1;94m'  \\___/ \\_|  |_/  \\_/   \\___/ \\_| |_/\\_____/ \n\n'\x1b[1;91m'   Author      :     IMTIAZ KING     \n'\x1b[1;92m'   Github      :     AKING110  \n'\x1b[1;93m'   FB ID       :     IMTIAZ KING\n'\x1b[1;94m'   TOOL TYPE   :     PAID COMMANDS\n'\x1b[1;96m'   WAP NUMBER  :     03237528063            \n"
dec = '2'
server = '2'
rsauser = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header = {
    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
    'x-fb-sim-hni': str(random.randint(20000, 40000)),
    'x-fb-net-hni': str(random.randint(20000, 40000)),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': rsauser,
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')
fuck = []
idx = []
oks = []
cps = []

def main_apv():
    imt = '+IMTIAZ=='
    os.system('clear')
    print logo
    
    try:
        key1 = open('/sdcard/.android.txt', 'r').read()
    except IOError:
        os.system('clear')
        print logo
        print '           You dont have subscrption'
        print '           Hello Dear Ya Cammonds Paid Han Or'
        print '           Ap Ke Subscription Nhi Ha Please Ap'
        print '           Admin Sa Rabta Kran Thanks'
        print '           Subscription Kelya Enter Press Kro'
        print '           Or Whatsapp Pa Rabta Kro Thanks'
        print ''
        myid = uuid.uuid4().hex[:10]
        print '         YOUR KEY : ' + myid + imt
        kok = open('/sdcard/.android.txt', 'w')
        kok.write(myid + imt)
        kok.close()
        print ''
        print '           Ya Uper Wale Ap Ke KEY Ha'
        print '           Copy Kar Ka WhatsApp Pa Bhaj Dena'
        print ''
        print ''
        print ''
        print '     Agar Ap Na Subscription Kar Le Ha To'
        raw_input('    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio ')
        os.system('xdg-open https://wa.me/+923237528063')

    r1 = requests.get('https://raw.githubusercontent.com/Aradinhacker/new/main/imt.txt').text
    if key1 in r1:
        main_system()
    else:
        os.system('clear')
        print logo
        print '           You dont have subscrption'
        print '           Hello Dear Ya Cammonds Paid Han Or'
        print '           Ap Ke Subscription Nhi Ha Please Ap'
        print '           Admin Sa Rabta Kran Thanks'
        print '           Subscription Kelya Enter Press Kro'
        print '           Or Whatsapp Pa Rabta Kro Thanks'
        print ''
        print '         YOUR KEY : ' + key1
        print ''
        print '           Ya Uper Wale Ap Ke KEY Ha'
        print '           Copy Kar Ka WhatsApp Pa Bhaj Dena'
        print ''
        print ''
        print ''
        print '     Agar Ap Na Subscription Kar Le Ha To'
        raw_input('    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio ')
        os.system('xdg-open https://wa.me/+923237528063')


def main_system():
    
    try:
        token = open('token.txt', 'r').read()
    except:
        pass

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        m = q['name']
        print ''
    except requests.exceptions.ConnectionError:
        print logo
        print ''
        print 'Trun On Data An Then \t'
        print ''
    except:
        print '\x1b[1;91mToken on Chekpiont '
        os.system('rm -rf token.txt')

    os.system('clear')
    print logo
    print ''
    print 39 * '~'
    print '\x1b[1;93m[1]   Public Cloning      \x1b[1;92m(Login)'
    print '\x1b[1;91m[2]   Random Cloning     \x1b[1;92m (No Login)'
    print '\x1b[1;92m[3]   File Cloning       \x1b[1;92m (No Login)'
    print '\x1b[1;93m[4]   File Making Menu\x1b[1;92m    (Login)'
    print '\x1b[1;94m[5]   Check Subscription '
    print '\x1b[1;95m[6]   Update Tools'
    print '\x1b[1;96m[7]   For Any Help Massage WhatsApp'
    print 43 * '~'
    print '\x1b[1;92m[*]\x1b[1;95m For Need Any Help Type 7 And \x1b[1;92mWhatsApp Me  '
    print 43 * '~'
    main_input()


def main_input():
    mx = raw_input('\x1b[1;92m[*] Select :\x1b[1;93m ')
    if mx == '1':
        print ''
        print '\x1b[1;94m Cheking Subscription ....\x1b[1;92m'
        time.sleep(3)
        fb_menu()
    elif mx == '2':
        print ''
        print '\x1b[1;94m Cheking Subscription ....\x1b[1;97m'
        time.sleep(3)
        numcloning()
    elif mx == '3':
        print ''
        print ''
        print ''
        print ''
        print '        [ File Cloning ]'
        print ''
        print '    [ Clone With Auto 1 Pass Speed ]'
        print ''
        print '    [1] Cloning With 1 Pass'
        print '    [2] Cloning With Auto Pass'
        print '    [3] Cloning With Name + Pass'
        print '    [0] Back'
        print ''
        c = raw_input('   [*] Select : ')
        if c == '2':
            fileauto()
        elif c == '3':
            n_f_p_pass()
        elif c == '1':
            c_f_p_pass()
        else:
            main_system()
    elif mx == '4':
        print ''
        print '\x1b[1;94m Cheking Subscription ....\x1b[1;97m'
        time.sleep(3)
        grap()
    elif mx == '5':
        os.system('clear')
        print logo
        print ''
        print ''
        print ''
        print ''
        print '\x1b[1;92m        Congratulations Bro Your Pro'
        print '\x1b[1;92m        Member In Imtiaz Paid Commands '
        print '\x1b[1;91m        ENJOY  KRO BHI LOGO '
        time.sleep(3.5)
        main_system()
    elif mx == '6':
        os.system('rm -rf PAID')
        os.system('git clone https://github.com/AKING110/PAID')
        os.system('cp -f PAID/PAID \\.')
        os.system('rm -rf PAID')
        os.system(' cd PAID')
        os.system(' python2 Imtiaz.py')
        time.sleep(5)
        xox('\x1b[92;1m\n TOOL UPDATE SUCCESSFUL :)\n')
        time.sleep(2)
        main_system()
    elif mx == '7':
        os.system('xdg-open https://wa.me/+923237528063')
        time.sleep(3)
        main_system()
    else:
        print 'invild option'
        time.sleep(2)
        main_system()
