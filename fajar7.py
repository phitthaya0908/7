# -*- coding: utf-8 -*-
# Support <-> ZNF TEAM BOTZ ===>##
import angrust
from angrust import *
from ang.ttypes import *
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, goslate, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
import pyimgflip

#==============================================================================#

loop = asyncio.get_event_loop()
with open('tokenku.json', 'r') as bolo:
     pin = json.load(bolo)

#==============[ token 1 ]==============#
if pin['token'] == "":
    line = LINE()
else:
     try:
         line = LINE(pin['token'])
     except:
         pin['token'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         line = LINE()

pin['token'] = line.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#==============[ token 2 ]==============#
if pin['token2'] == "":
    ka = LINE()
else:
     try:
         ka = LINE(pin['token2'])
     except:
         pin['token2'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         ka = LINE()

pin['token2'] = ka.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#==============[ token 3 ]==============#
if pin['token3'] == "":
    kb = LINE()
else:
     try:
         kb = LINE(pin['token3'])
     except:
         pin['token3'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         kb = LINE()

pin['token3'] = kb.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#============[ token 4 ]=================#
if pin['token4'] == "":
    kc = LINE()
else:
     try:
         kc = LINE(pin['token4'])
     except:
         pin['token4'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         kc = LINE()

pin['token4'] = kc.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#==============[ token 5 ]==============#
if pin['token5'] == "":
    kd = LINE()
else:
     try:
         kd = LINE(pin['token5'])
     except:
         pin['token5'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         kd = LINE()

pin['token5'] = kd.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#==============[ token 6 ]==============#
if pin['token6'] == "":
    ke = LINE()
else:
     try:
         ke = LINE(pin['token6'])
     except:
         pin['token6'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         ke = LINE()

pin['token6'] = ke.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)

#============[ token 7 ]=================#
if pin['token7'] == "":
    ke = LINE()
else:
     try:
         k1 = LINE(pin['token7'])
     except:
         pin['token7'] = ""
         with open('tokenku.json', 'w') as fp:
             json.dump(pin, fp, sort_keys=True, indent=4)
         k1 = LINE()

pin['token7'] = k1.authToken
with open('tokenku.json', 'w') as fp:
    json.dump(pin, fp, sort_keys=True, indent=4)
#==============[●●●●●●]==============#
print ("Login proces 5menit boss")

cl = line
oepoll = OEPoll(cl)
Bismillah=[cl,ka,kb,kc,kd]
Amin=[ka,kb,kc,kd]
Aakun=[kb,kc,kd,ke]
Bakun=[ka,kc,kd,ke]
Cakun=[ka,kb,kd,ke]
Dakun=[ka,kc,kb,ke]
Eakun=[ka,kb,kd,kc]
mid = cl.getProfile().mid
Amid = ka.getProfile().mid
Bmid = kb.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kd.getProfile().mid
Emid = ke.getProfile().mid
Smid = k1.getProfile().mid
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Smid]
Ang = ["uf0716516721c4897fd2b536284a206a6","ubdfea3cad8d0093238cfa2f496ce3f0c"]
Angrust = Bots+Ang
msg_dict = {}
msg_dict1 = {}
#==============[ Main Json ]==============#
main = codecs.open("Znfwait.json","r","utf-8")
Znfwait = json.load(main)
boters = codecs.open("Znfbot.json","r","utf-8")
Znfbot = json.load(boters)
zblacklist = codecs.open("Znfblacklist.json","r","utf-8")
Znfbl = json.load(zblacklist)

wait = Znfwait

settings = {
    "gPicture":False,
    "cPicture":False,
    "likeStat":True,
    "LikeOn":True,
    "Jscancel":True,
    "like":4,
    "autoJoinTicket":False,
    "postingan":{},
    "Picture":False,
    "group":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

listTimeLiking = time.time()

def autolike():
   if settings['LikeOn'] == True:
     like = 1000+Znfwait['like']
     koment = Znfwait['comment']
     for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          try:    
            cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=like)
            cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],koment+"\n\nBy: kingEyes\nhttp://line.me/ti/p/~fajarsambodja27")
            print ("Liked")
          except:
            pass
        else:
            print ("Already Liked")
   else:
    pass

def autoLike():
    listTimeLiking = time.time()
    if time.time() - listTimeLiking >= 60*60:
        listLikeType = [1001, 1002, 1003, 1004, 1005, 1006]
        myComment = "[Auto Like]"+\
                    "\nThis is AutoLike And Comment by: kingEyes Bot✡Team"
        #feed = channel.getFeed()
        feed = cl.getFeed()
        if feed['message'] != 'success':
            listTimeLiking = time.time()
            return True
        del feed["result"]["feedInfos"]
        result = feed["result"]["feeds"]
        for res in result:
            postInfo = res["post"]["postInfo"]
            homeId = postInfo["homeId"]
            postId = postInfo["postId"]
            if settings["likeStat"] == True:
                continue
            else:
                #channel.likePost(homeId, postId, random.choice(listLikeType))
                client.likepost(homeId, postId, random.choice(listLikeType))
                #channel.createComment(homeId, postId, myComment)
                client.createComment(homeId, postId, myComment)
        listTimeLiking = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > timedelta(1):
            if "path" in msg_dict[data]:
                cl.deleteFile(msg_dict[data]["path"])
            del msg_dict[data]

def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > timedelta(1):
            del msg_dict1[msg_id]

def atend():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)

def atend1():
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
atexit.register(atend)


def cek(mid):
    if mid in (Bots):
        return True
    else:
        return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def mentionMembers(to, mid):
    try:
        arrData = ""
        ginfo = cl.getGroup(to)
        textx = "╔═════[ Sider Members ]═══════\n║ Sini Gabung Chat kak jgan diem aja 😅😅..\n╠☛ Haii ➳♥︻╦̵̵͇̿̿̿̿╤───➳ 1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "╠☛  {}. ".format(str(no))
            else:
                textx += "╚══════════════════\n╔══════════════════\n  「 ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀ : {} 」\n╚══════════════════".format(str(len(mid)))
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "「reader {} member」\nhai ka..➳♥︻╦̵̵͇̿̿̿̿╤───➳  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Znfwait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "「Member Join {}」\Wellcome ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+Znfwait["welcome"]+"\ndi group : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\nNama Group : "+str(len(gid))+"\nTeman : "+str(len(teman))+"\nExpired : In "+hari+"\n Version :「Gaje Bots」  \nTanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\nRuntime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def command(text):
    pesan = text.lower()
    if pesan.startswith(Znfwait["keyCmd"]):
        cmd = pesan.replace(Znfwait["keyCmd"],"")
    else:
        cmd = "command"
    return cmd

def help():
    key = Znfwait["keyCmd"]
    key = key.title()
    helpMessage = "═════🔰◈kingEyes◈🔰════╗\n║「bot✡Team」\n╠═════🔰kingEyes🔰═════╝\n" + \
                  "║┍✡∘·" + key + "Me\n" + \
                  "║┝✡∘·" + key + "Mid「@」\n" + \
                  "║┝✡∘·" + key + "Info「@」\n" + \
                  "║┝✡∘·" + key + "Eyes kick「@」\n" + \
                  "║┝✡∘·" + key + "Cium「@」\n" + \
                  "║┝✡∘·" + key + "Bot kick「@」\n" + \
                  "║┝✡∘·" + key + "F5 kick「@」\n" + \
                  "║┝✡∘·" + key + "Syg\n" + \
                  "║┝✡∘·" + key + "Status\n" + \
                  "║┝✡∘·" + key + "About\n" + \
                  "║┝✡∘·" + key + "/reboot\n" + \
                  "║┝✡∘·" + key + "Runtime\n" + \
                  "║┝✡∘·" + key + "Creator\n" + \
                  "║┝✡∘·" + key + "Sp\n" + \
                  "║┝✡∘·" + key + ".sp\n" + \
                  "║┝✡∘·" + key + "hay\n" + \
                  "║┝✡∘·" + key + "Come -out\n" + \
                  "║┝✡∘·" + key + "Eyes join\n" + \
                  "║┝✡∘·" + key + "Eyes bye\n" + \
                  "║┝✡∘·" + key + "Leave「Namagrup」\n" + \
                  "║┝✡∘·" + key + "Ginfo\n" + \
                  "║┝✡∘·" + key + "ourl\n" + \
                  "║┝✡∘·" + key + "Vourl\n" + \
                  "║┝✡∘·" + key + "curl\n" + \
                  "║┝✡∘·" + key + ".join\n" + \
                  "║┝✡∘·" + key + "out.p\n" + \
                  "║┝✡∘·" + key + "Fall urlgrup\n" + \
                  "║┝✡∘·" + key + "Gruplist\n" + \
                  "║┝✡∘·" + key + "Absen-respon2\n" + \
                  "║┝✡∘·" + key + "Infogrup「angka」\n" + \
                  "║┝✡∘·" + key + "Infomem「angka」\n" + \
                  "║┝✡∘·" + key + "hc\n" + \
                  "║┝✡∘·" + key + "Rechat\n" + \
                  "║┝✡∘·" + key + "Lurk「on/off」\n" + \
                  "║┝✡∘·" + key + "Lurkers\n" + \
                  "║┝✡∘·" + key + "Intip「on/off」\n" + \
                  "║┝✡∘·" + key + "Mepict\n" + \
                  "║┝✡∘·" + key + "Uppict\n" + \
                  "║┝✡∘·" + key + "Pictgrup\n" + \
                  "║┝✡∘·" + key + "Bcg:「Text」\n" + \
                  "║┝✡∘·" + key + "Setkey「New Key」\n" + \
                  "║┝✡∘·" + key + "Mykey\n" + \
                  "║┝✡∘·" + key + ".join\n" + \
                  "║┝✡∘·" + key + "F1 kick @\n" + \
                  "║┝✡∘·" + key + "F2 kick @\n" + \
                  "║┝✡∘·" + key + "F3 kick @\n" + \
                  "║┝✡∘·" + key + "F4 kick @\n" + \
                  "║┝✡∘·" + key + "Music:「Judul Lagu」\n" + \
                  "║┝✡∘·" + key + "Lirik:「Judul Lagu」\n" + \
                  "║┝✡∘·" + key + "Yt3:「Judul Lagu」\n" + \
                  "║┝✡∘·" + key + "Yt4:「Judul Video」\n" + \
                  "║┝✡∘·" + key + "Profileig:「Nama IG」\n" + \
                  "║┝✡∘·" + key + "Cekdate:「tgl-bln-thn」\n" + \
                  "║┝✡∘·" + key + "max:「angka」\n" + \
                  "║┝✡∘·" + key + "Spamtag「@」\n" + \
                  "║┝✡∘·" + key + "Scall:「jumlahnya」\n" + \
                  "║┕✡∘·" + key + "Scall \n" + \
                  "╠═════🔰◈kingEyes◈🔰═════╗\n║「http://line.me/ti/p/~fajarsambodja27」\n╚════🔰◈kingEyes◈🔰════╝"
    return helpMessage

def helpset():
    key = Znfwait["keyCmd"]
    key = key.title()
    helpMessage1 = "═════◈kingEyes◈═════╗\n║「kingEyes」\n╠═════◈kingEyes◈═════╝\n" + \
                  "║┍🔰∘·" + key + "Notag「on/off」\n" + \
                  "║┝🔰∘·" + key + "Protect「on/off」\n" + \
                  "║┝🔰∘·" + key + "Proqr「on/off」\n" + \
                  "║┝🔰∘·" + key + "Projoin「on/off」\n" + \
                  "║┝🔰∘·" + key + "Autokick「on/off」\n" + \
                  "║┝🔰∘·" + key + "Procancel「on/off」\n" + \
                  "║┝🔰∘·" + key + "Sticker「on/off」\n" + \
                  "║┝🔰∘·" + key + "Respon「on/off」\n" + \
                  "║┝🔰∘·" + key + "Contact「on/off」\n" + \
                  "║┝🔰∘·" + key + "Autojoin「on/off」\n" + \
                  "║┝🔰∘·" + key + "Autoadd「on/off」\n" + \
                  "║┝🔰∘·" + key + "Welcome「on/off」\n" + \
                  "║┝🔰∘·" + key + "Autoleave「on/off」\n" + \
                  "║┝🔰∘·" + key + "Jticket「on/off」\n" + \
                  "║┝🔰∘·" + key + "Eyes「on/off」\n" + \
                  "║┝🔰∘·" + key + "Bot:on\n" + \
                  "║┝🔰∘·" + key + "Bot:dell\n" + \
                  "║┝🔰∘·" + key + "addbot「@」\n" + \
                  "║┝🔰∘·" + key + "delbot「@」\n" + \
                  "║┝🔰∘·" + key + "Refresh\n" + \
                  "║┝🔰∘·" + key + "Syg\n" + \
                  "║┝🔰∘·" + key + "admin list\n" + \
                  "║┕🔰∘·" + key + "prolist\n" + \
                  "╠═════🔰◈kingEyes◈🔰═════╗\n║「http://line.me/ti/p/~fajarsambodja27」\n╚═════◈kingEyes◈═════╝"
    return helpMessage1

def helpbot():
    key = Znfwait["keyCmd"]
    key = key.title()
    helpMessage2 = "═════◈kingEyes◈═════╗\n║「bot✡Team」\n╠═════◈kingEyes◈═════╝\n" + \
                  "║┍✔∘·" + key + "Cban\n" + \
                  "║┝✔∘·" + key + "Ban:on\n" + \
                  "║┝✔∘·" + key + "Unban:on\n" + \
                  "║┝✔∘·" + key + "Ban「@」\n" + \
                  "║┝✔∘·" + key + "Unban「@」\n" + \
                  "║┝✔∘·" + key + "Tban「@」\n" + \
                  "║┝✔∘·" + key + "Utban「@」\n" + \
                  "║┝✔∘·" + key + "Tban:on\n" + \
                  "║┝✔∘·" + key + "Utban:on\n" + \
                  "║┝✔∘·" + key + "Banlist\n" + \
                  "║┝✔∘·" + key + "Tbanlist\n" + \
                  "║┝✔∘·" + key + "Refresh\n" + \
                  "║┝✔∘·" + key + "cekmsg\n" + \
                  "║┝✔∘·" + key + "sider:「Text」\n" + \
                  "║┝✔∘·" + key + "spam:「Text」\n" + \
                  "║┝✔∘·" + key + "add:「Text」\n" + \
                  "║┝✔∘·" + key + "tag:「Text」\n" + \
                  "║┝✔∘·" + key + "welcome:「Text」\n" + \
                  "║┝✔∘·" + key + "zname:「Nama」\n" + \
                  "║┝✔∘·" + key + "v1cn:「Nama」\n" + \
                  "║┝✔∘·" + key + "v2cn:「Nama」\n" + \
                  "║┝✔∘·" + key + "v3cn:「Nama」\n" + \
                  "║┝✔∘·" + key + "v4cn:「Nama」\n" + \
                  "║┝✔∘·" + key + "v5cn:「Nama」\n" + \
                  "║┝✔∘·" + key + "Kicker cn:「Nama」\n" + \
                  "║┝✔∘·" + key + "Kickerpict「K fhoto」\n" + \
                  "║┝✔∘·" + key + "f1pict「Kirim fhoto」\n" + \
                  "║┝✔∘·" + key + "f2pict「Kirim fhoto」\n" + \
                  "║┝✔∘·" + key + "f3pict「Kirim fhoto」\n" + \
                  "║┝✔∘·" + key + "f4pict「Kirim fhoto」\n" + \
                  "║┝✔∘·" + key + "f5pict「Kirim fhoto」\n" + \
                  "║┝✔∘·" + key + "Gift:「Mid」「Jumlah」\n" + \
                  "║┕✔∘·" + key + "Spam:「Mid」「Jumlah」\n" + \
                  "╠═════◈kingEyes◈═════╗\n║「http://line.me/ti/p/~fajarsambodja27」\n╚═════◈kingEyes◈═════╝"
    return helpMessage2

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11:
            if op.param1 in Znfbl["proqr"]:
                if cl.getGroup(op.param1).preventedJoinByTicket == False:
                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                        Znfbl["blacklist"][op.param2] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                    X = random.choice(Bismillah).getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    Z = random.choice(Bismillah).getGroup(op.param1)
                    Z.preventedJoinByTicket = True
                    random.choice(Bismillah).updateGroup(Z)

        if op.type == 11:
            if op.param1 in Znfbl["pQr"]:
                if cl.getGroup(op.param1).preventedJoinByTicket == False:
                    if op.param2 not in Znfbl["blacklist"] and op.param2 not in Angrust:
                        Znfbl["blacklist"][op.param2] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                    X = random.choice(Bismillah).getGroup(op.param1)
                    X.preventedJoinByTicket = True
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    Z = random.choice(Bismillah).getGroup(op.param1)
                    Z.preventedJoinByTicket = True
                    random.choice(Bismillah).updateGroup(Z)

        if op.type == 11:
            if op.param2 in Znfbl["blacklist"]:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            cl.updateGroup(X)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                except:
                    try:
                        if ka.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                                ka.reissueGroupTicket(op.param1)
                                X = ka.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ka.updateGroup(X)
                                ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                                    kb.reissueGroupTicket(op.param1)
                                    X = kb.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kb.updateGroup(X)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                                            kd.reissueGroupTicket(op.param1)
                                            X = kd.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kd.updateGroup(X)
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                                                ke.reissueGroupTicket(op.param1)
                                                X = ke.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                ke.updateGroup(X)
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 11:
            if op.param1 in Znfbl["intaPoint"]:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                    pass
                else:
                    X = cl.getGroup(op.param1)
                    if X.preventedJoinByTicket == True:
                        pass
                    else:
                        cl.updateGroup(X)
                        invsend = 0
                        Ti = cl.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)

        if op.type == 13:
            if op.param1 in Znfbl["pInvite"]:
               if op.param2 in Angrust:
                  pass
               else:
                   if op.param2 not in Znfbl["blacklist"] and op.param2 not in Angrust:
                      Znfbl["blacklist"][op.param2] = True
                      f=codecs.open('Znfblacklist.json','w','utf-8')
                      json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                   anu = random.choice(Bismillah).getCompactGroup(op.param1)
                   if anu.invitee is not None:
                         pipo = [a.mid for a in anu.invitee]
                         for target in pipo:
                             if target in op.param3:
                                random.choice(Bismillah).cancelGroupInvitation(op.param1,[target])
                                random.choice(Amin).kickoutFromGroup(op.param1,[target])
                         random.choice(Bismillah).kickoutFromGroup(op.param1,[op.param2])          

        if op.type == 32:
           if op.param1 in Znfbl["pCancel"]:
              if op.param2 in Angrust:
                 pass
              else:
                if op.param2 not in Znfbl["blacklist"] and op.param2 not in Angrust:
                  Znfbl["blacklist"][op.param2] = True
                  f=codecs.open('Znfblacklist.json','w','utf-8')
                  json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                  try:
                    random.choice(Bismillah).getCompactGroup(op.param1)
                    random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                    random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Bismillah).acceptGroupInvitation(op.param1)
                  except:
                      pass

        if op.type == 32:
           if op.param2 in Znfbl["blacklist"]:
              if op.param2 in Angrust:
                 pass
              else:
                 random.choice(Bismillah).getCompactGroup(op.param1)
                 random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                 random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                 random.choice(Bismillah).acceptGroupInvitation(op.param1)
                 random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 13:
            if mid in op.param3:
                if Znfwait["autoJoin"] == True:
                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                        cl.acceptGroupInvitation(op.param1)
                        anu = cl.getContact(op.param2)
                        cl.sendMessageWithMention(op.param1,"maaf {} autoLeaveku on..send link aja " + str(anu.displayName))
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Znfbl["blacklist"]:
                            cl.kickoutFromGroup(op.param1,[_mid])
            if Amid in op.param3:
                if Znfwait["autoJoin"] == True:
                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                        ka.acceptGroupInvitation(op.param1)
                        anu = ka.getContact(op.param2)
                        ka.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        ka.leaveGroup(op.param1)
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        group = ka.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Znfbl["blacklist"]:
                            ka.kickoutFromGroup(op.param1,[_mid])
            if Bmid in op.param3:
                if Znfwait["autoJoin"] == True:
                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                        kb.acceptGroupInvitation(op.param1)
                        anu = kb.getContact(op.param2)
                        kb.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        group = kb.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Znfbl["blacklist"]:
                            kb.kickoutFromGroup(op.param1,[_mid])
            if Cmid in op.param3:
                if Znfwait["autoJoin"] == True:
                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                        kc.acceptGroupInvitation(op.param1)
                        anu = kc.getContact(op.param2)
                        kc.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        group = kc.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Znfbl["blacklist"]:
                            kc.kickoutFromGroup(op.param1,[_mid])
            if Dmid in op.param3:
                if Znfwait["autoJoin"] == True:
                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                        kd.acceptGroupInvitation(op.param1)
                        anu = kd.getContact(op.param2)
                        kd.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        group = kd.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Znfbl["blacklist"]:
                            kd.kickoutFromGroup(op.param1,[_mid])
            if Emid in op.param3:
                if Znfwait["autoJoin"] == True:
                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                        ke.acceptGroupInvitation(op.param1)
                        anu = ke.getContact(op.param2)
                        ke.sendMessageWithMention(op.param1,"{} majikanku diluar sem " + str(anu.displayName))
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        group = ke.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.members]
                        for _mid in gMembMids:
                          if _mid in Znfbl["blacklist"]:
                            ke.kickoutFromGroup(op.param1,[_mid])

            if op.param1 in Znfbl["proInvite"]:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    try:
                        if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                            Znfbl["blacklist"][op.param2] = True
                            f=codecs.open('Znfblacklist.json','w','utf-8')
                            json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                            random.choice(Bismillah).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                                Znfbl["blacklist"][op.param2] = True
                                f=codecs.open('Znfblacklist.json','w','utf-8')
                                json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                group = cl.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _mid in gMembMids:
                                  if _mid not in Angrust and _mid not in Znfbot["Bots"] and _mid not in Znfbot["admin"]:
                                    random.choice(Bismillah).cancelGroupInvitation(op.param1,[_mid])
                                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
            if op.param2 in Znfbl["blacklist"]:
               if op.param2 in Angrust:
                  pass
               else:
                  try:
                      anu = random.choice(Bismillah).getCompactGroup(op.param1)
                      if anu.invitee is not None:
                            pipo = [a.mid for a in anu.invitee]
                            for target in pipo:
                                if target in op.param3:
                                    random.choice(Bismillah).cancelGroupInvitation(op.param1,[target])
                                    random.choice(Amin).kickoutFromGroup(op.param1,[target])
                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                  except:
                      pass
            if op.param3 in Znfbl["blacklist"]:
               if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                  pass
               else:
                    try:
                        if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                            Znfbl["blacklist"][op.param2] = True
                            f=codecs.open('Znfblacklist.json','w','utf-8')
                            json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                            random.choice(Bismillah).cancelGroupInvitation(op.param1,[op.param3])
                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass

        if op.type == 15:
            if op.param1 in Znfbl["leaveMsg"]:
                if op.param2 in Angrust and op.param2 not in Znfbot["admin"] and op.param2 not in Znfbot["Bots"]:
                    return
                else:
                    cl.sendMessage(op.param1, Znfwait["leftmsg"])

        if op.type == 17:
            if op.param2 in Znfbl["blacklist"]:
                random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])

            if op.param1 in Znfbl["welcome"]:
                if op.param2 in Angrust or op.param2 in ["Bots"] or op.param2 in ["admin"]:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)

            if op.param1 in Znfbl["proJoin"]:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                if op.param2 not in Znfbl["blacklist"]:
                    pass
                else:
                    try:
                        if op.param2 in Znfbl["blacklist"]:
                            ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param2 in Znfbl["blacklist"]:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param2 in Znfbl["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param2 in Znfbl["blacklist"]:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param2 in Znfbl["blacklist"]:
                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass
                return

        if op.type == 0:
            return

        if op.type == 5:
            if Znfwait["autoAdd"] == True:
                if op.param2 not in Angrust:
                    if (Znfwait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.findAndAddContactsByMid(op.param1)
                        cl.sendMessage(op.param1, Znfwait["message"])

        if op.type == 19:
            if op.param1 in Znfbl["proKick"]:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in Znfbl["blacklist"]:
                            ke.findAndAddContactsByMid(op.param3)
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in Znfbl["blacklist"]:
                                ka.findAndAddContactsByMid(op.param3)
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in Znfbl["blacklist"]:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param3 not in Znfbl["blacklist"]:
                                        kc.findAndAddContactsByMid(op.param3)
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param3 not in Znfbl["blacklist"]:
                                            kd.findAndAddContactsByMid(op.param3)
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        pass

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Angrust:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        k1.acceptGroupInvitation(op.param1)
                        k1.findAndAddContactsByMid(op.param3)
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        k1.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        x = k1.getGroup(op.param1)
                        x.preventedJoinByTicket = False
                        k1.updateGroup(x)
                        invsend = 0
                        Ti = k1.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ti)
                        ka.acceptGroupInvitationByTicket(op.param1,Ti)
                        kb.acceptGroupInvitationByTicket(op.param1,Ti)
                        kc.acceptGroupInvitationByTicket(op.param1,Ti)
                        kd.acceptGroupInvitationByTicket(op.param1,Ti)
                        ke.acceptGroupInvitationByTicket(op.param1,Ti)
                        Ticket = k1.reissueGroupTicket(op.param1)
                        k1.leaveGroup(op.param1)
                        random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                    except:
                        random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                        random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Angrust:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kd.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kd.updateGroup(x)
                                    invsend = 0
                                    Ti = kd.reissueGroupTicket(op.param1)
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Amin).findAndAddContactsByMid(op.param3)
                                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])
                                            cl.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Amid in op.param3:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        kb.findAndAddContactsByMid(op.param3)
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        ka.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kc.findAndAddContactsByMid(op.param3)
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ka.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kd.findAndAddContactsByMid(op.param3)
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                ka.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = ke.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    ke.updateGroup(x)
                                    invsend = 0
                                    Ti = ke.reissueGroupTicket(op.param1)
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        ka.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Aakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Aakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Aakun).inviteIntoGroup(op.param1,[op.param3])
                                            ka.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Bmid in op.param3:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        kc.findAndAddContactsByMid(op.param3)
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kd.findAndAddContactsByMid(op.param3)
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ke.findAndAddContactsByMid(op.param3)
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = ka.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    ka.updateGroup(x)
                                    invsend = 0
                                    Ti = ka.reissueGroupTicket(op.param1)
                                    ka.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Bakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Bakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Bakun).inviteIntoGroup(op.param1,[op.param3])
                                            kb.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Cmid in op.param3:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        kd.findAndAddContactsByMid(op.param3)
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ke.findAndAddContactsByMid(op.param3)
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                ka.findAndAddContactsByMid(op.param3)
                                ka.kickoutFromGroup(op.param1,[op.param2])
                                ka.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Cakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Cakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Cakun).inviteIntoGroup(op.param1,[op.param3])
                                            kc.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Dmid in op.param3:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        ke.findAndAddContactsByMid(op.param3)
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kc.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kc.updateGroup(x)
                                    invsend = 0
                                    Ti = kc.reissueGroupTicket(op.param1)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kd.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Dakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Dakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Dakun).inviteIntoGroup(op.param1,[op.param3])
                                            kd.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Emid in op.param3:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                            except:
                                try:
                                    x = kd.getGroup(op.param1)
                                    x.preventedJoinByTicket = False
                                    kd.updateGroup(x)
                                    invsend = 0
                                    Ti = kd.reissueGroupTicket(op.param1)
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                                    k1.kickoutFromGroup(op.param1,[op.param2])
                                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                                    G = k1.getGroup(op.param1)
                                    G.preventedJoinByTicket = True
                                    k1.updateGroup(G)
                                    k1.leaveGroup(op.param1)
                                    random.choice(Bismillah).inviteIntoGroup(op.param1,[Smid])
                                except:
                                    try:
                                        cl.findAndAddContactsByMid(op.param3)
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                    except:
                                        try:
                                            random.choice(Eakun).findAndAddContactsByMid(op.param3)
                                            random.choice(Eakun).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Eakun).inviteIntoGroup(op.param1,[op.param3])
                                            ke.acceptGroupInvitation(op.param1)
                                        except:
                                            pass
                return
            if Smid in op.param3:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        ke.findAndAddContactsByMid(op.param3)
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            ka.findAndAddContactsByMid(op.param3)
                            ka.kickoutFromGroup(op.param1,[op.param2])
                            ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kb.findAndAddContactsByMid(op.param3)
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kc.findAndAddContactsByMid(op.param3)
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        kd.findAndAddContactsByMid(op.param3)
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            random.choice(Amin).findAndAddContactsByMid(op.param3)
                                            random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                return
            if op.param3 in Znfbot["Bots"]:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                                            random.choice(Bismillah).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                return
            if op.param3 in Znfbot["admin"]:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    Znfbl["blacklist"][op.param2] = True
                    try:
                        ka.findAndAddContactsByMid(op.param3)
                        ka.kickoutFromGroup(op.param1,[op.param2])
                        ka.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            kb.findAndAddContactsByMid(op.param3)
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                kc.findAndAddContactsByMid(op.param3)
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    kd.findAndAddContactsByMid(op.param3)
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        ke.findAndAddContactsByMid(op.param3)
                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        try:
                                            random.choice(Bismillah).findAndAddContactsByMid(op.param3)
                                            random.choice(Bismillah).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(Bismillah).inviteIntoGroup(op.param1,[op.param3])
                                        except:
                                            pass
                return

        if op.type == 32:
            if op.param1 in Znfbl["proCancel"]:
                if op.param2 in Angrust and op.param2 in Znfbot["Bots"] and op.param2 in Znfbot["admin"]:
                    pass
                else:
                    if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                        Znfbl["blacklist"][op.param2] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                        user = cl.getContact(op.param2)
                        random.choice(Amin).sendMessage(op.param1,"In protection ,, you not admin!! " + str(user.displayName))
                        random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                        try:
                            if op.param3 in Angrust:
                                ka.findAndAddContactsByMid(op.param3)
                                ka.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                if op.param3 in Znfbot["Bots"]:
                                    kb.findAndAddContactsByMid(op.param3)
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                try:
                                    if op.param3 in Znfbot["admin"]:
                                        kc.findAndAddContactsByMid(op.param3)
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                except:
                                    try:
                                        if op.param3 not in Znfbl["blacklist"]:
                                            kd.findAndAddContactsByMid(op.param3)
                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                    except:
                                        pass

            if Smid in op.param3:
                if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                    Znfbl["blacklist"][op.param2] = True
                    f=codecs.open('Znfblacklist.json','w','utf-8')
                    json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    cl.findAndAddContactsByMid(op.param3)
                    cl.inviteIntoGroup(op.param1,[Smid])
            if op.param3 in Angrust:
                if op.param2 not in Angrust and op.param2 not in Znfbot["Bots"] and op.param2 not in Znfbot["admin"]:
                    Znfbl["blacklist"][op.param2] = True
                    f=codecs.open('Znfblacklist.json','w','utf-8')
                    json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(Amin).findAndAddContactsByMid(op.param3)
                    random.choice(Amin).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 55:
            try:
                if op.param1 in Znfwait["readPoint"]:
                   if op.param2 in Znfwait["readMember"][op.param1]:
                       pass
                   else:
                       Znfwait["readMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])

            if op.param2 in Znfbl["blacklist"]:
                if op.param2 not in Angrust and op.param2 not in Znfbot["admin"] and op.param2 not in Znfbot["Bots"]:
                    random.choice(Amin).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 65:
            if Znfwait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "「 Gambar Dihapus nah kan balikin lah🤣🤣😜😜😜」\n• Pelaku : "
                                ret_ = "• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "「 Pesan Dihapus  balikin lah😜😜😜😜」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n• Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if Znfwait["Unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "「 Sticker Dihapus kan di hapus balkin lah😜😜😜 」\n"
                                ret_ += "• Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n• Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n• Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != cl.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if Znfwait["checkmid"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][msg.to]:
                        read["ROM"][msg.to][sender] = True
                if Znfwait["Unsend"] == True:
                    try:
                        msg = op.message
                        if msg.toType == 0:
                            cl.log("[{} : {}]".format(str(msg._from), str(msg.text)))
                        else:
                            cl.log("[{} : {}]".format(str(msg.to), str(msg.text)))
                            msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                    except Exception as error:
                        print (error)
                if msg.contentType == 0:
                    msg_dict[msg.id] = {"text": msg.text, "from": msg._from, "createdTime": msg.createdTime, "contentType": msg.contentType, "contentMetadata": msg.contentMetadata}
                if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
                if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 Sticker Info 」"
                   ret_ += "\n• Sticker ID : {}".format(stk_id)
                   ret_ += "\n• Sticker Version : {}".format(stk_ver)
                   ret_ += "\n• Sticker Package : {}".format(pkg_id)
                   ret_ += "\n• Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}

        if op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 and msg.toType == 2:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
                if "MENTION" in msg.contentMetadata.keys() != None:
                  if Znfwait['detectMention'] == True:
                      contact = cl.getContact(msg._from)
                      cName = contact.pictureStatus
                      balas = ["http://dl.profile.line-cdn.net/" + cName]
                      ret_ = random.choice(balas)
                      mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                      mentionees = mention["MENTIONEES"]
                      for mention in mentionees:
                            if mention["M"] in mid:
                                   cl.sendMessage(msg.to, Znfwait["msgTag"])
                                   cl.sendMessage(msg.to, None, contentMetadata={"STKID":"14857911","STKPKGID":"1379734","STKVER":"1"}, contentType=7)
                                   break
                if 'MENTION' in msg.contentMetadata.keys() != None:
                  if Znfwait["Mentionkick"] == True:
                      contact = cl.getContact(msg._from)
                      mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                      mentionees = mention['MENTIONEES']
                      for mention in mentionees:
                            if mention['M'] in mid:
                                   cl.mentiontag(msg.to,[msg._from])
                                   cl.sendMessage(msg.to,"don't tag me...")
                                   cl.kickoutFromGroup(msg.to,[msg._from])
                                   break

            if msg.contentType == 7:
              if Znfwait["sticker"] == True:
                  msg.contentType = 0
                  cl.sendMessage(msg.to,"•「Check ID Sticker」•\n STKID : " + msg.contentMetadata["STKID"] + "\n STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])

            if msg.contentType == 13:
              if Znfwait["contact"] == True:
                 msg.contentType = 0
                 cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                 if 'displayName' in msg.contentMetadata:
                     contact = cl.getContact(msg.contentMetadata["mid"])
                     path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                     image = 'http://dl.profile.line.naver.jp'+path
                     cl.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                     cl.sendImageWithURL(msg.to, image)
            if msg.contentType == 16:
              if settings['LikeOn'] == True:
                  try:
                      typel = [1001,1002,1003,1004,1005,1006]
                      url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                      st = url['result']["homeId"]
                      for i in range(len(st)):
                          test = st[i]
                          result = test['posts']['postInfo']['postId']
                          cl.like(str(st), str(result), likeType=random.choice(typel))
                          cl.comment(str(st), str(result), 'like by: kingEyes')
                  except:
                      pass
            if msg.contentType == 16:
              if Znfwait["checkPost"] == True:
                  try:
                      ret_ = "╔════[ Post Detail ]"
                      if msg.contentMetadata["serviceType"] == "GB":
                          contact = cl.getContact(sender)
                          auth = "\n╠☛ Author : {}".format(str(contact.displayName))
                      else:
                          auth = "\n╠☛ Author : {}".format(str(msg.contentMetadata["serviceName"]))
                      purl = "\n╠☛ Url : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                      ret_ += auth
                      ret_ += purl
                      if "mediaOid" in msg.contentMetadata:
                          object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                          if msg.contentMetadata["mediaType"] == "V":
                              if msg.contentMetadata["serviceType"] == "GB":
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                  murl = "\n╠☛ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                              else:
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                  murl = "\n╠☛ Url Media : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                              ret_ += murl
                          else:
                              if msg.contentMetadata["serviceType"] == "GB":
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                              else:
                                  ourl = "\n╠☛ Url Object : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                          ret_ += ourl
                      if "stickerId" in msg.contentMetadata:
                          stck = "\n╠☛ Sticker : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                          ret_ += stck
                      if "text" in msg.contentMetadata:
                          text = "\n╠☛ Note : {}".format(str(msg.contentMetadata["text"]))
                          ret_ += text
                      ret_ += "\n╚══[ kingEyes botTeam ]"
                      cl.sendMessage(to, str(ret_))
                  except:
                      cl.sendMessage(msg.to,"Invalid Post")

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if Znfwait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"╔══════════════\n╠☛❲Check Sticker❳\n╠☛ STKID : " + msg.contentMetadata["STKID"] +"\n╠☛ STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n╠☛ STKVER : " + msg.contentMetadata["STKVER"] + "\n╠☛ " + "line://shop/detail/" + msg.contentMetadata["STKPKGID"] +"\n╚══════════════")
               if msg.contentType == 13:
                 if Znfwait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"╔══════════════\n╠☛ Nama : " + msg.contentMetadata["displayName"] + "\n╠☛ Mid : " + msg.contentMetadata["mid"] + "\n╠☛ Status : " + contact.statusMessage + "\n╠☛ Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n╚══════════════")
                        cl.sendImageWithURL(msg.to, image)

               if msg.contentType == 13:
                 if msg._from in Ang:
                  if Znfwait["abots"] == True:
                    if msg.contentMetadata["mid"] in Znfbot["Bots"]:
                        cl.sendMessage(msg.to,"was bot friend")
                    else:
                        Znfbot["Bots"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('Znfbot.json','w','utf-8')
                        json.dump(Znfbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add bots")
                 if Znfwait["dbots"] == True:
                    if msg.contentMetadata["mid"] in Znfbot["Bots"]:
                        del Znfbot["Bots"][msg.contentMetadata["mid"]]
                        f=codecs.open('Znfbot.json','w','utf-8')
                        json.dump(Znfbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove bots")
                    else:
                        cl.sendMessage(msg.to,"Contact not in list bots")

                 if msg._from in Ang:
                  if Znfwait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in Znfbot["admin"]:
                        cl.sendMessage(msg.to,"was admin")
                    else:
                        Znfbot["admin"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('Znfbot.json','w','utf-8')
                        json.dump(Znfbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add admin")
                 if Znfwait["deladmin"] == True:
                    if msg.contentMetadata["mid"] in Znfbot["admin"]:
                        del Znfbot["admin"][msg.contentMetadata["mid"]]
                        f=codecs.open('Znfbot.json','w','utf-8')
                        json.dump(Znfbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove admin")
                    else:
                        cl.sendMessage(msg.to,"Contact not in list admin")

                 if msg._from in Ang:
                  if Znfwait["ablacklist"] == True:
                    if msg.contentMetadata["mid"] in Znfbl["blacklist"]:
                        cl.sendMessage(msg.to,"was blacklist")
                    else:
                        Znfbl["blacklist"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add in blacklist")
                 if Znfwait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in Znfbl["blacklist"]:
                        del Znfbl["blacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove blacklist")
                    else:
                        cl.sendMessage(msg.to,"Contact not in blacklist")

                 if msg._from in Ang:
                  if Znfwait["Tablacklist"] == True:
                    if msg.contentMetadata["mid"] in Znfbl["Talkblacklist"]:
                        cl.sendMessage(msg.to,"was Talkblacklist")
                    else:
                        Znfbl["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"succes add in Talkblacklist")
                 if Znfwait["Tdblacklist"] == True:
                    if msg.contentMetadata["mid"] in Znfbl["Talkblacklist"]:
                        del Znfbl["Talkblacklist"][msg.contentMetadata["mid"]]
                        f=codecs.open('Znfblacklist.json','w','utf-8')
                        json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                        cl.sendMessage(msg.to,"Succes remove Talkblacklist")
                    else:
                        cl.sendMessage(msg.to,"Contact not in Talkblacklist")

               if msg.contentType == 1:
                 if msg._from in Ang:
                    if Znfwait["Aimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = cl.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Znfwait["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            cl.sendMessage(msg.to, "Succses")
                        Znfwait["Img"] = {}
                        Znfwait["Aimage"] = False

               if msg.toType == 2:
                 if msg._from in Ang:
                   if settings["gPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["gPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Succes")

               if msg.contentType == 1:
                   if msg._from in Ang:
                       if mid in Znfwait["foto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Znfwait["foto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Succes")

               if msg.contentType == 1:
                 if msg._from in Ang:
                        if Amid in Znfwait["foto"]:
                            path = ka.downloadObjectMsg(msg_id)
                            del Znfwait["foto"][Amid]
                            ka.updateProfilePicture(path)
                            ka.sendMessage(msg.to,"Succes")
                        elif Bmid in Znfwait["foto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Znfwait["foto"][Bmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Succes")
                        elif Cmid in Znfwait["foto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Znfwait["foto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Succes")

               if msg.contentType == 1:
                 if msg._from in Ang:
                   if settings["cPicture"] == True:
                     path1 = ka.downloadObjectMsg(msg_id)
                     path2 = kb.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     settings["cPicture"] = False
                     ka.updateProfilePicture(path1)
                     ka.sendMessage(msg.to, "Succes change pic")
                     kb.updateProfilePicture(path2)
                     kb.sendMessage(msg.to, "Succes change pic")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Succes change pic")

               if msg.contentType == 0:
                    if Znfwait["autoRead"] == True:
                        cl.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        cmd = command(text)
                        if cmd == "help":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               helpMessage = help()
                               cl.sendMessage(to,helpMessage)

                        if cmd == "menubot":
                            if msg._from in Ang:
                               helpMessage = help()
                               ka.sendMessage(to,helpMessage)

                        if cmd == "help1":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               helpMessage1 = helpset()
                               cl.sendMessage(to,helpMessage1)

                        if cmd == "menubot1":
                            if msg._from in Ang:
                               helpMessage1 = helpset()
                               ka.sendMessage(to,helpMessage1)

                        if cmd == "on":
                            if msg._from in Ang:
                                Znfwait["selfbot"] = True
                                cl.sendMessage(msg.to, "⫍◦•◉✿[ᵏⁱⁿᵍᴇʸᵉˢ✔ Mσɗe Oη")

                        elif cmd == "off":
                            if msg._from in Ang:
                                Znfwait["selfbot"] = False
                                cl.sendMessage(msg.to, "⫍◦•◉✿[ᵏⁱⁿᵍᴇʸᵉˢ✔ Mσɗe off")

                        if cmd == "tbanon":
                            if msg._from in Ang:
                                Znfwait["talkban"] = True
                                cl.sendMessage(msg.to, "kick Talkban on")

                        elif cmd == "tbanoff":
                            if msg._from in Ang:
                                Znfwait["talkban"] = False
                                cl.sendMessage(msg.to, "kick Talkban off")

                        elif cmd == "help2":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               helpMessage2 = helpbot()
                               cl.sendMessage(to,helpMessage2)

                        elif cmd == "menubot2":
                            if msg._from in Ang:
                               helpMessage2 = helpbot()
                               ka.sendMessage(to,helpMessage2)

                        elif cmd == "grupset":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                md = ""
                                if msg.to in Znfbl["proqr"]: md+="􁤁􀇜╠☛ PʀᴏQr : ✓\n"
                                else: md+="✔╠☛ PʀᴏQr: ✘\n"
                                if msg.to in Znfbl["proJoin"]: md+="􁤁􀇜╠☛ PʀᴏJᴏɪɴ : ✓\n"
                                else: md+="✔╠☛ PʀᴏJᴏɪn : ✘\n"
                                if msg.to in Znfbl["proKick"]: md+="􁤁􀇜╠☛ Auto ᴋɪᴄᴋ : ✓\n"
                                else: md+="✔╠☛ Auto ᴋɪᴄᴋ : ✘\n"
                                if msg.to in Znfbl["proCancel"]: md+="􁤁􀇜╠☛ Pʀᴏᴄᴀɴᴄᴇʟ : ✓\n"
                                else: md+="✔╠☛ PʀᴏᴄᴀɴᴄᴇL : ✘\n"
                                if msg.to in Znfbl["eyesPoint"]: md+="􁤁􀇜╠☛ Eyes FR7 : ✓\n"
                                else: md+="✔╠☛ EyesPoint : ✘\n"
                                if msg.to in Znfbl["Talkblacklist"]: md+="􁤁􀇜╠☛ ReadKick : ✓\n"
                                else: md+="✔╠☛ ReadKick : ✘\n"
                                if msg.to in Znfbl["welcome"]: md+="􁤁􀇜╠☛ welcome : ✓\n"
                                else: md+="✔╠☛ Welcome : ✘\n"
                                if msg.to in Znfbl["leaveMsg"]: md+="􁤁􀇜╠☛ Leave Msg : ✓\n"
                                else: md+="✔╠☛ Leave Msg : ✘\n"
                                #cl.sendFooter(to,"╔═══❲ Sett Group ❳════\n"+ md +"╚══════════════", userid, "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName)
                                cl.sendMessage(msg.to, "╔═══❲ Sett Group ❳════\n"+ md +"╚══════════════")

                        elif text.lower() == "status":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                md = ""
                                if Znfwait["autoJoin"] == True: md+="✔╠☛ AᴜᴛᴏJᴏɪɴ : ✓\n"
                                else: md+="✔╠☛ AutoJoin : ✘\n"
                                if Znfwait["sticker"] == True: md+="✔╠☛ Stickeʀ : ✓\n"
                                else: md+="✔╠☛ Stickeʀ ✘\n"
                                if Znfwait["contact"] == True: md+="✔╠☛ Cᴏntacᴛ : ✓\n"
                                else: md+="✔╠☛ Cᴏntacᴛ : ✘ \n"
                                if Znfwait["Mentionkick"] == True: md+="✔╠☛ AutoKick Mention : ✓\n"
                                else: md+="✔╠☛ AutoKick Mention : ✘\n"
                                if Znfwait["detectMention"] == True: md+="✔╠☛ Mention : ✓\n"
                                else: md+="✔╠☛ Mention : ✘\n"
                                if Znfwait["autoAdd"] == True: md+="✔╠☛ Msg ᴀᴅᴅ : ✓\n"
                                else: md+="✔╠☛ Msg ᴀᴅᴅ : ✘\n"
                                if Znfwait["autoLeave"] == True: md+="✔╠☛ Auto Lᴇᴀᴠᴇ : ✓\n"
                                else: md+="✔╠☛ Leave Msg : ✘\n"
                                cl.sendMessage(msg.to, "╔═══❲ ✡Status Group✡ ❳════\n"+ md +"╚══════════════")

                        elif cmd == "me" or text.lower() == 'me':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               cl.sendMentionFooter(to, '「My Name」\n', sender, "https://line.me/ti/p/~fajarsambodja27", "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName);cl.sendMessage(to, cl.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+cl.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~fajarsambodja27', 'type': 'mt', 'subText': "⫍◦•◉✿[ᵏⁱⁿᵍᴇʸᵉˢ]🦋F7✔", 'a-installUrl': 'https://line.me/ti/p/~fajarsambodja27', 'a-installUrl': ' https://line.me/ti/p/~fajarsambodja27', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~fajarsambodja27', 'i-linkUri': 'https://line.me/ti/p/~fajarsambodja27', 'id': 'mt000000000a6b79f9', 'text': '⫍◦•◉✿[ᵏⁱⁿᵍᴇʸᵉˢ]🦋F7✔', 'linkUri': 'https://line.me/ti/p/~fajarsambodja27'}, contentType=19)

                        elif ("Gn " in msg.text):
                          if msg._from in Ang:
                              X = cl.getGroup(msg.to)
                              X.name = msg.text.replace("Gn ","")
                              cl.updateGroup(X)

                        elif 'Like ' in text.lower():
                          if msg._from in Ang:
                              try:
                                  typel = [1001,1002,1003,1004,1005,1006]
                                  key = eval(msg.contentMetadata["MENTION"])
                                  u = key["MENTIONEES"][0]["M"]
                                  a = cl.getContact(u).mid
                                  s = cl.getContact(u).displayName
                                  hasil = cl.getHomeProfile(mid=a)
                                  st = hasil['result']["homeId"]
                                  for i in range(len(st)):
                                      test = st[i]
                                      result = test['posts']['postInfo']['postId']
                                      cl.like(str(sender), str(result), likeType=random.choice(typel))
                                      cl.comment(str(sender), str(result), 'AUTO_Like by: kingEyes bot✡Team')
                                  cl.sendMessage(receiver, 'Done Like+Comment '+str(len(st))+' Post From' + str(s))
                              except Exception as e:
                                  cl.sendMessage(receiver, str(e))

                        elif cmd == " like all" or text.lower() == 'like':
                                hasil = cl.getHome(msg._from)
                                zxc =  hasil['result']['homeInfo']['postCount']
                                for zx in range(0,zxc):
                                  if hasil['result']['feeds'][zx]['post']['postInfo']['liked'] == False:
                                    try:
                                      cl.like(hasil['result']['feeds'][zx]['post']['userInfo']['mid'],hasil['result']['feeds'][zx]['post']['postInfo']['postId'],likeType=1000+Znfwait['like'])
                                      cl.comment(hasil['result']['feeds'][zx]['post']['userInfo']['mid'],hasil['result']['feeds'][zx]['post']['postInfo']['postId'],Znfwait['comment']+"\n\nAutoLike by: LIPRO\nhttp://line.me/ti/p/~ankrust86")
                                    except:
                                       pass
                                  else:
                                     pass
                                cl.sendMessage(msg.to,"Done") 

                        elif ("Mid " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               if 'MENTION' in msg.contentMetadata.keys()!= None:
                                   names = re.findall(r'@(\w+)', text)
                                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                   mentionees = mention['MENTIONEES']
                                   lists = []
                                   for mention in mentionees:
                                       if mention["M"] not in lists:
                                           lists.append(mention["M"])
                                   ret_ = ""
                                   for ls in lists:
                                       ret_ += "{}".format(str(ls))
                                   cl.sendMessage(to, str(ret_),{'AGENT_ICON': 'http://dl.profile.line-cdn.net/'+'M', 'AGENT_NAME': 'Mention', 'AGENT_LINK': 'http://line.me/ti/p/~{}'.format(cl.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + cl.getProfile().picturePath})

                        elif ("Info " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "☛ Nama : "+str(mi.displayName)+"\n☛ Mid : " +key1+"\n☛ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "syg":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               ka.sendContact(msg.to, Amid)
                               time.sleep(0.15)
                               kb.sendContact(msg.to, Bmid)
                               time.sleep(0.15)
                               kc.sendContact(msg.to, Cmid)
                               time.sleep(0.15)
                               kd.sendContact(msg.to, Dmid)
                               time.sleep(0.15)
                               ke.sendContact(msg.to, Emid)

                        elif text.lower() == "myrechat":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               try:
                                   cl.removeAllMessages(op.param2)
                               except:
                                   pass

                        elif text.lower() == "hc":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               try:
                                   ka.removeAllMessages(op.param2)
                                   ka.sendMessage(msg.to,"chat bersih boss😊.. ")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"chat bersih boss☺.. ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"chat bersih boss☺.. ")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to,"chat bersih boss😊.. ")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to,"bersih semua boss😊.. ")
                               except:
                                   ka.removeAllMessages(op.param2)
                                   ka.sendMessage(msg.to,"chat telah dihapus boss😊... ")
                                   kb.removeAllMessages(op.param2)
                                   kb.sendMessage(msg.to,"chat telah dihapus boss😊... ")
                                   kc.removeAllMessages(op.param2)
                                   kc.sendMessage(msg.to,"chat telah dihapus boss😊... ")
                                   kd.removeAllMessages(op.param2)
                                   kd.sendMessage(msg.to,"chat telah dihapus boss😊... ")
                                   ke.removeAllMessages(op.param2)
                                   ke.sendMessage(msg.to,"chat talah dihapus boss😊... ")
                                   k1.removeAllMessages(op.param2)
                                   k1.sendMessage(msg.to,"done boss qu😊😜... ")

                        elif cmd.startswith("bcg: "):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               cl.sendMessage(msg.to, "key Now「 " + str(Znfwait["keyCmd"]) + " 」")

                        elif cmd.startswith("setkey "):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "change key failed")
                               else:
                                   Znfwait["keyCmd"] = str(key).lower()
                                   cl.sendMessage(msg.to, "succes at「{}」".format(str(key).lower()))

                        elif text.lower() == "resetkey":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               Znfwait["keyCmd"]=""
                               cl.sendMessage(msg.to, "succes resset key command")

                        elif cmd == "/reboot":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               cl.sendMessage(msg.to, "waiting a second")
                               Znfwait["rePoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "bot was restarting")

                        elif cmd == "runtime":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               eltime = time.time() - listTimeLiking
                               bot = "was run " +waktu(eltime)
                               userid = "https://line.me/ti/p/~" + cl.profile.userid
                               cl.sendMessage(to, bot, (userid), "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName)

                        elif cmd == "ginfo":
                          if msg._from in Ang:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "  •⌻「Grup Info」⌻•\n\n Nama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup"):
                          if msg._from in Ang:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "No file"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "  •⌻ List Grup Info ⌻•\n"
                                ret_ += "\n⌬ Nama Group : {}".format(G.name)
                                ret_ += "\n⌬ ID Group : {}".format(G.id)
                                ret_ += "\n⌬ Pembuat : {}".format(gCreator)
                                ret_ += "\n⌬ Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n⌬ Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n⌬ Jumlah Pending : {}".format(gPending)
                                ret_ += "\n⌬ Group Qr : {}".format(gQr)
                                ret_ += "\n⌬ Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem"):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "● "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to,"● Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except:
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ka.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    ka.sendMessage(msg.to,"Succes leave in group " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"╔══[ FRIEND LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Friends ]")

                        elif cmd == "gruplist":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z1grup":
                            if msg._from in Ang:
                               ma = ""
                               a = 0
                               gid = ka.getGroupIdsJoined()
                               for i in gid:
                                   G = ka.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ka.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z2grup":
                            if msg._from in Ang:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z3grup":
                            if msg._from in Ang:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z4grup":
                            if msg._from in Ang:
                               ma = ""
                               a = 0
                               gid = kd.getGroupIdsJoined()
                               for i in gid:
                                   G = kd.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               kd.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "z5grup":
                            if msg._from in Ang:
                               ma = ""
                               a = 0
                               gid = ke.getGroupIdsJoined()
                               for i in gid:
                                   G = ke.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               ke.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "kickergrup":
                            if msg._from in Ang:
                               ma = ""
                               a = 0
                               gid = k1.getGroupIdsJoined()
                               for i in gid:
                                   G = k1.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "╠ " + str(a) + ". " +G.name+ "\n"
                               k1.sendMessage(msg.to,"╔══[ GROUP LIST ]\n║\n"+ma+"║\n╚══[ Total「"+str(len(gid))+"」Groups ]")

                        elif cmd == "ourl":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                gurl = cl.reissueGroupTicket(msg.to)
                                cl.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "curl":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "done°")

                        elif cmd == "zourl":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                if msg.toType == 2:
                                   X = ka.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   ka.updateGroup(X)
                                gurl = ka.reissueGroupTicket(msg.to)
                                ka.sendMessage(msg.to,"line://ti/g/" + gurl)

                        elif cmd == "zcurl":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                if msg.toType == 2:
                                   X = ka.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   ka.updateGroup(X)
                                   ka.sendMessage(msg.to, "done°")

                        elif cmd == "all urlgrup":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "●Nama : "+str(x.name)+ "\n● Url grup : http://line.me/R/ti/g/"+gurl)

                        elif cmd == "zall urlgrup":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                if msg.toType == 2:
                                   x = ka.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      ka.updateGroup(x)
                                   gurl = ka.reissueGroupTicket(msg.to)
                                   ka.sendMessage(msg.to, "● Nama : "+str(x.name)+ "\n● Url grup : http://line.me/R/ti/g/"+gurl)

#===========================================#
                        elif cmd == "pictgrup":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                              if msg.toType == 2:
                                settings["gPicture"] = True
                                cl.sendMessage(msg.to,"please send pict")

                        elif cmd == "mepict":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                settings["cPicture"] = True
                                cl.sendMessage(msg.to,"please send pict")

                        elif cmd == "uppict":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["foto"][mid] = True
                                cl.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z1pict":
                            if msg._from in Ang:
                                Znfwait["foto"][Amid] = True
                                ka.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z2pict":
                            if msg._from in Ang:
                                Znfwait["foto"][Bmid] = True
                                kb.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z3pict":
                            if msg._from in Ang:
                                Znfwait["foto"][Cmid] = True
                                kc.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z4pict":
                            if msg._from in Ang:
                                Znfwait["foto"][Dmid] = True
                                kd.sendMessage(msg.to,"please Send pict")

                        elif cmd == "z5pict":
                            if msg._from in Ang:
                                Znfwait["foto"][Emid] = True
                                ke.sendMessage(msg.to,"please Send pict")

                        elif cmd == "kickerpict":
                            if msg._from in Ang:
                                Znfwait["foto"][Smid] = True
                                k1.sendMessage(msg.to,"please Send pict")

                        elif cmd.startswith("zname: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z1cn: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ka.getProfile()
                                profile.displayName = string
                                ka.updateProfile(profile)
                                ka.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z2cn: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z3cn: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z4cn: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("z5cn: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd.startswith("kicker cn: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(msg.to,"Succes " + string + "")

                        elif cmd == "hay" or text.lower() == 'mention':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                group = cl.getGroup(msg.to)
                                nama = [contact.mid for contact in group.members]
                                k = len(nama)//20
                                for a in range(k+1):
                                    txt = u''
                                    s=0
                                    b=[]
                                    for i in group.members[a*20 : (a+1)*20]:
                                        b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                        s += 7
                                        txt += u'@Alin \n'
                                    cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif cmd == ".bot":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"  kingEyes Botz\n\n"+ma+"\nTotal : %sBot" %(str(len(Bots))))

                        elif cmd == "adminlist":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                mb = ""
                                b = 0
                                for m_id in Znfbot["admin"]:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"ADMIN: "+mb+"\nTotal :「%s」\n Admin Bot" %(str(len(admin))))

                        elif cmd == "absen":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                ka.sendMessage(msg.to,"hadir bos😊...")
                                kb.sendMessage(msg.to,"saya juga bos😜😜...")
                                kc.sendMessage(msg.to,"aku juga hadir boss😅😅...")
                                kd.sendMessage(msg.to,"bawah aku habis nikung boss👇😅😅...")
                                ke.sendMessage(msg.to,"apaan gak bos dia bohong😑😑😑😣😣...")

                        elif text.lower() == "respon2":
                            if msg._from in Ang:
                                if msg.to in Znfbl["proCancel"] or msg.to in Znfbl["proInvite"]:
                                    cl.sendMessage(msg.to, "siap siaga bos qu")
                                else:
                                    Znfbl["pCancel"][msg.to] = True
                                    Znfbl["pInvite"][msg.to] = True
                                    Znfbl["pQr"][msg.to] = True
                                    f=codecs.open('Znfblacklist.json','w','utf-8')
                                    json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ka.sendMessage(msg.to, "hadir F1..✔")
                                    kb.sendMessage(msg.to, "hadir F2..✔")
                                    kc.sendMessage(msg.to, "hadir F3..✔")
                                    kd.sendMessage(msg.to, "hadir F4..✔")
                                    ke.sendMessage(msg.to, "hadir F5..✔")

                        elif cmd == ".join":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                try:
                                    ang = [Amid,Bmid,Cmid,Dmid,Emid]
                                    cl.inviteIntoGroup(msg.to, ang)
                                    ka.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                except:
                                    pass

                        elif cmd == "stay":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                try:
                                    ang = [Smid]
                                    cl.inviteIntoGroup(msg.to, ang)
                                except:
                                    ka.inviteIntoGroup(msg.to, ang)

                        elif cmd == "eyes bye":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = k1.getGroup(msg.to)
                                k1.sendMessage(msg.to, "see u member "+str(G.name))
                                k1.leaveGroup(msg.to)

                        elif cmd == "z1bye":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = ka.getGroup(msg.to)
                                ka.sendMessage(msg.to, "see u member "+str(G.name))
                                ka.leaveGroup(msg.to)

                        elif cmd == "z2bye":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = kb.getGroup(msg.to)
                                kb.sendMessage(msg.to, "see u member "+str(G.name))
                                kb.leaveGroup(msg.to)

                        elif cmd == "z3bye":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = kc.getGroup(msg.to)
                                kc.sendMessage(msg.to, "see u member "+str(G.name))
                                kc.leaveGroup(msg.to)

                        elif cmd == "z4bye":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = kd.getGroup(msg.to)
                                kd.sendMessage(msg.to, "see u member "+str(G.name))
                                kd.leaveGroup(msg.to)

                        elif cmd == "z5bye":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = ke.getGroup(msg.to)
                                ke.sendMessage(msg.to, "see u member "+str(G.name))
                                ke.leaveGroup(msg.to)

                        elif cmd == "come":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif cmd == "out":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                ka.sendMessage(msg.to, "see you 😎 "+str(G.name))
                                kb.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                ka.leaveGroup(msg.to)

                        elif cmd == "/bye":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "see u member "+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in Ang:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ka.sendMessage(i, "")
                                        kb.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        ka.sendMessage(to,"Leave succes from " +h)

                        elif cmd == "z1join":
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ka.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ka.updateGroup(G)

                        elif cmd == "z2join":
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)

                        elif cmd == "z3join":
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)

                        elif cmd == "z4join":
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kd.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kd.updateGroup(G)

                        elif cmd == "z5join":
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "eyes join":
                            if msg._from in Ang:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = k1.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                k1.updateGroup(G)

                        elif cmd == ".speed respon":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "🚩response 🚩\n\n - 🌏 Speed Profile\n   %.10f\n - ➡ Speed Contact\n   %.10f\n - ➡ Speed Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "speed" or cmd == "sp":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               start = time.time()
                               cl.sendMessage(to, "sabar bos.......")
                               elapsed_time = time.time() - start
                               cl.sendMessage(to,format(str(elapsed_time)))

                        elif cmd == ".speed" or cmd == ".sp":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               start = time.time()
                               ka.sendMessage("uf0716516721c4897fd2b536284a206a6", '.')
                               elapsed_time = time.time() - start
                               ka.sendMessage(msg.to, "%s s" % (elapsed_time))

                               start2 = time.time()
                               kb.sendMessage("uf0716516721c4897fd2b536284a206a6", '.')
                               elapsed_time = time.time() - start2
                               kb.sendMessage(msg.to, "%s s" % (elapsed_time))

                               start3 = time.time()
                               kc.sendMessage("uf0716516721c4897fd2b536284a206a6", '.')
                               elapsed_time = time.time() - start3
                               kc.sendMessage(msg.to, "%s s" % (elapsed_time))

                               start4 = time.time()
                               kd.sendMessage("uf0716516721c4897fd2b536284a206a6", '.')
                               elapsed_time = time.time() - start4
                               kd.sendMessage(msg.to, "%s " % (elapsed_time))

                               start5 = time.time()
                               ke.sendMessage("uf0716516721c4897fd2b536284a206a6", '.')
                               elapsed_time = time.time() - start5
                               ke.sendMessage(msg.to, "%s s" % (elapsed_time))

                        elif cmd == "lurk on":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Znfwait['readPoint'][msg.to] = msg_id
                                 Znfwait['readMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking berhasil diaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurk off":
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Znfwait['readPoint'][msg.to]
                                 del Znfwait['readMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")

                        elif cmd == "lurkers":
                          if msg._from in Ang:
                            if msg.to in Znfwait['readPoint']:
                                if Znfwait['readMember'][msg.to] != {}:
                                    aa = []
                                    for x in Znfwait['readMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\n⌬ Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n⌚ Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Znfwait['readPoint'][msg.to]
                                        del Znfwait['readMember'][msg.to]
                                    except:
                                        pass
                                    Znfwait['readPoint'][msg.to] = msg.id
                                    Znfwait['readMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on ")

                        elif cmd == "intip on":
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "╔══════════════\n╠☛ starting cek sider\n╚══════════════\n╔══════════════\n╠☛ date : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n╠☛ hour "+ datetime.strftime(timeNow,'%H:%M:%S')+"\n╚══════════════")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "intip off":
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "╔══════════════\n╠☛ sider off mode\n╚══════════════")
                              else:
                                  cl.sendMessage(msg.to, "sider in off mode")

                        elif cmd.startswith("sholat: "):
                          if msg._from in Ang:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n Lokasi : " + data[0]
                                         ret_ += "\n⌬ " + data[1]
                                         ret_ += "\n⌬ " + data[2]
                                         ret_ += "\n⌬ " + data[3]
                                         ret_ += "\n⌬ " + data[4]
                                         ret_ += "\n⌬ " + data[5]
                                         ret_ += "\n\n Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\n Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in Ang:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\n Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in Ang:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n Location : " + data[0]
                                    ret_ += "\n Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("lirik: "):
                           if msg._from in Ang:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "╔══[ Lyric ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendMessage(msg.to, str(ret_))
                                   except:
                                       cl.sendMessage(to, "Lirik tidak ditemukan")

                        elif cmd.startswith("music: "):
                           if msg._from in Ang:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "╔══[ Music ]"
                                          ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                          ret_ += "\n╠ Link : {}".format(str(song[3]))
                                          ret_ += "\n╚══[ Waiting Audio ]"
                                      cl.sendMessage(msg.to, str(ret_))
                                      cl.sendMessage(msg.to, "Loading....")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendMessage(to, "Musik tidak ditemukan")

                        elif cmd.startswith("zimage: "):
                          if msg._from in Ang:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("yt4: "):
                          if msg._from in Ang:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendText(msg.to,str(e))

                        elif cmd.startswith("yt3: "):
                          if msg._from in Ang:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                bestaudio = vid.getbestaudio()
                                bestaudio.bitrate
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    shi = bestaudio.url
                                    me = best.url
                                    vin = s.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                cl.sendImageWithURL(msg.to, me)
                                cl.sendAudioWithURL(msg.to, shi)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("profileig: "):
                          if msg._from in Ang:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = " Link : " + "https://www.instagram.com/" + instagram
                                text = " Name : "+namaIG+"\n Username : "+usernameIG+"\n Biography : "+bioIG+"\n Follower : "+followerIG+"\n Following : "+followIG+"\n Post : "+mediaIG+"\n Verified : "+verifIG+"\n Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in Ang:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"⇸「 I N F O 」⇷\n\n"+" Date Of Birth : "+lahir+"\n Age : "+usia+"\n Ultah : "+ultah+"\n Zodiak : "+zodiak)

                        elif cmd.startswith("max: "):
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Znfwait["Maxlimit"] = num
                                cl.sendMessage(msg.to,"Max spam Tag " +strnum)

                        elif cmd.startswith("scall: "):
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Znfwait["limit"] = num
                                cl.sendMessage(msg.to,"Max spam call " +strnum)

                        elif cmd.startswith("stag "):
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Znfwait["Maxlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendMessage(msg.to,"Jumlah melebihi 1000")

                        elif cmd == "scall":
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(Znfwait["limit"])
                                cl.sendMessage(to, "Succes {} Spam Call".format(str(Znfwait["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                         cl.acquireGroupCallRoute(to)
                                         cl.inviteIntoGroupCall(to, contactIds=members)
                                     except:
                                         pass
                                else:
                                    cl.sendMessage(to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Znfwait["spamMsg"]))
                                      ka.sendMessage(midd, str(Znfwait["spamMsg"]))
                                      kb.sendMessage(midd, str(Znfwait["spamMsg"]))
                                      kc.sendMessage(midd, str(Znfwait["spamMsg"]))
                                      kd.sendMessage(midd, str(Znfwait["spamMsg"]))
                                      ke.sendMessage(midd, str(Znfwait["spamMsg"]))

                        elif 'ID line: ' in msg.text:
                          if Znfwait["selfbot"] == True:
                           if msg._from in Ang:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

                        elif 'Welcome ' in msg.text:
                           if msg._from in Ang:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in Znfbl["welcome"]:
                                       msgs = "Msg Welcome was on"
                                  else:
                                       Znfbl["welcome"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group: " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Znfbl["welcome"]:
                                         del Znfbl["welcome"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Msg welcome mode on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Left ' in msg.text:
                           if msg._from in Ang:
                              spl = msg.text.replace('Left ','')
                              if spl == 'on':
                                  if msg.to in Znfbl["leaveMsg"]:
                                       msgs = "Msg Left was on"
                                  else:
                                       Znfbl["leaveMsg"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group: " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Znfbl["leaveMsg"]:
                                         del Znfbl["leaveMsg"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Msg Leave mode on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Proqr ' in msg.text:
                           if msg._from in Ang:
                              spl = msg.text.replace('Proqr ','')
                              if spl == 'on':
                                  if msg.to in Znfbl["proqr"]:
                                       msgs = "Succes"
                                  else:
                                       Znfbl["proqr"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Znfbl["proqr"]:
                                         del Znfbl["proqr"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url on"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Autokick ' in msg.text:
                           if msg._from in Ang:
                              spl = msg.text.replace('Autokick ','')
                              if spl == 'on':
                                  if msg.to in Znfbl["proKick"]:
                                       msgs = "Autokick on"
                                  else:
                                       Znfbl["proKick"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Znfbl["proKick"]:
                                         del Znfbl["proKick"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Autokick off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Projoin ' in msg.text:
                           if msg._from in Ang:
                              spl = msg.text.replace('Projoin ','')
                              if spl == 'on':
                                  if msg.to in Znfbl["proJoin"]:
                                       msgs = "Projoin on"
                                  else:
                                       Znfbl["proJoin"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Znfbl["proJoin"]:
                                         del Znfbl["proJoin"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Projoin off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in Ang:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in Znfbl["proCancel"]:
                                       msgs = "Procancel on"
                                  else:
                                       Znfbl["proCancel"] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "In Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Znfbl["proCancel"]:
                                         Znfbl["proCancel"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "In Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Procancel off"
                                    cl.sendMessage(msg.to, "「off mode」\n" + msgs)

                        elif 'Protect ' in msg.text:
                           if msg._from in Ang:
                              spl = msg.text.replace('Protect ','')
                              if spl == 'on':
                                  if msg.to in Znfbl["proqr"]:
                                       msgs = ""
                                  else:
                                       Znfbl["proqr"][msg.to] = True
                                  if msg.to in Znfbl["proKick"]:
                                      msgs = ""
                                  else:
                                       Znfbl["proKick"][msg.to] = True
                                  if msg.to in Znfbl["proInvite"]:
                                      msgs = ""
                                  else:
                                       Znfbl["proInvite"][msg.to] = True
                                  if msg.to in Znfbl["proJoin"]:
                                      msgs = ""
                                  else:
                                       Znfbl["proJoin"][msg.to] = True
                                  if msg.to in Znfbl["proCancel"]:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "High Allprotection mode on at : " +str(ginfo.name)
                                  else:
                                       Znfbl["proCancel"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "High Allprotection mode on at : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「on mode」\n\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Znfbl["proqr"]:
                                         del Znfbl["proqr"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    else:
                                         msgs = ""
                                    if msg.to in Znfbl["proKick"]:
                                         del Znfbl["proKick"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    else:
                                         msgs = ""
                                    if msg.to in Znfbl["proInvite"]:
                                         del Znfbl["proInvite"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    else:
                                         msgs = ""
                                    if msg.to in Znfbl["proJoin"]:
                                         del Znfbl["proJoin"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    else:
                                         msgs = ""
                                    if msg.to in Znfbl["proCancel"]:
                                         del Znfbl["proCancel"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protection mode off at : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protection mode off at : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "「off mode」\n\n" + msgs)

                        elif 'Eyes ' in msg.text:
                           if msg._from in Ang:
                              spl = msg.text.replace('Eyes ','')
                              if spl == 'on':
                                  if msg.to in Znfbl["intaPoint"]:
                                       msgs = "Eyes on"
                                  else:
                                       Znfbl["intaPoint"][msg.to] = True
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Eyes on at Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "「Eyes VR7 on」\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in Znfbl["intaPoint"]:
                                         del Znfbl["intaPoint"][msg.to]
                                         f=codecs.open('Znfblacklist.json','w','utf-8')
                                         json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Eyes off at Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Eyes off"
                                    cl.sendMessage(msg.to, "「Eyes VR7 off」\n" + msgs)

                        elif ("Eyes kick " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           cl.sendMessage(msg.to, "sorry bro😜.")
                                           random.choice(Amin).kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("F1 kick " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           Znfbl["pCancel"][msg.to] = True
                                           Znfbl["pInvite"][msg.to] = True
                                           Znfbl["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           ka.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("F2 kick " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           Znfbl["pCancel"][msg.to] = True
                                           Znfbl["pInvite"][msg.to] = True
                                           Znfbl["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           kb.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("F3 kick " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           Znfbl["pCancel"][msg.to] = True
                                           Znfbl["pInvite"][msg.to] = True
                                           Znfbl["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           kc.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("F4 kick " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           Znfbl["pCancel"][msg.to] = True
                                           Znfbl["pInvite"][msg.to] = True
                                           Znfbl["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           kd.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("F5 kick " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           Znfbl["pCancel"][msg.to] = True
                                           Znfbl["pInvite"][msg.to] = True
                                           Znfbl["pQr"][msg.to] = True
                                           f=codecs.open('Znfblacklist.json','w','utf-8')
                                           json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           ke.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Cium " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Kicker kick " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ti = cl.reissueGroupTicket(msg.to)
                                           k1.acceptGroupInvitationByTicket(msg.to,Ti)
                                           k1.kickoutFromGroup(msg.to, [target])
                                           X = k1.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           k1.updateGroup(X)
                                           k1.leaveGroup(msg.to)
                                       except:
                                           pass

                        elif ("Cancel" in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "empty ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Angrust and x not in Znfbot["Bots"] and x not in Znfbot ["admin"]:
                                       cl.cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "done.")

                        elif ("Bot cancel" in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               group = cl.getGroup(msg.to)
                               if group.invitee is None:
                                   cl.sendMessage(op.message.to, "empty ")
                               else:
                                   nama = [contact.mid for contact in group.invitee]
                                   for x in nama:
                                     if x not in Angrust and x not in Znfbot["Bots"] and x not in Znfbot ["admin"]:
                                       random.choice(Amin).cancelGroupInvitation(msg.to, [x])
                                       time.sleep(0.3)
                                   cl.sendMessage(to, "done.")

                        elif ("Addadmin " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Znfbot["admin"][target] = True
                                           f=codecs.open('Znfbot.json','w','utf-8')
                                           json.dump(Znfbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           cl.sendMessage(msg.to,"Succes add admin")
                                       except:
                                           pass

                        elif ("Addbot " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Znfbot["Bots"][target] = True
                                           f=codecs.open('Znfbot.json','w','utf-8')
                                           json.dump(Znfbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                                           cl.sendMessage(msg.to,"Succes add bot")
                                       except:
                                           pass

                        elif ("Deladmin " in msg.text):
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                        try:
                                            del Znfbot["admin"][target]
                                            f=codecs.open('Znfbot.json','w','utf-8')
                                            json.dump(Znfbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            cl.sendMessage(msg.to,"Succes delete admin")
                                        except:
                                            pass

                        elif ("Delbot " in msg.text):
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Angrust:
                                        try:
                                            del Znfbot["Bots"][target]
                                            f=codecs.open('Znfbot.json','w','utf-8')
                                            json.dump(Znfbot, f, sort_keys=True, indent=4,ensure_ascii=False)
                                            cl.sendMessage(msg.to,"Succes delete bots")
                                        except:
                                            pass

                        elif cmd == "botlist" or text.lower() == 'bot list':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                              if Znfbot["Bots"] == {}:
                                cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                              else:
                                  mc = "╔══════════════\n╠☛ ❲ Bot List ❳☚\n╠══════════════"
                                  for mi_d in Znfbot["Bots"]:
                                      mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n╚══════════════")

                        elif cmd == "adminlist" or text.lower() == 'admin list':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                              if Znfbot["admin"] == {}:
                                cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                              else:
                                  mc = "╔══════════════\n╠☛ ❲ Admin List ❳☚\n╠══════════════"
                                  for mi_d in Znfbot["admin"]:
                                      mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n╚══════════════")

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in Ang:
                                Znfwait["addadmin"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "admin:del" or text.lower() == 'admin:del':
                            if msg._from in Ang:
                                Znfwait["deladmin"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "admin:off" or text.lower() == 'admin off':
                            if msg._from in Ang:
                                Znfwait["addadmin"] = False
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "deladmin:off" or text.lower() == 'deladmin off':
                            if msg._from in Ang:
                                Znfwait["deladmin"] = False
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "bot:on" or text.lower() == 'bot on':
                            if msg._from in Ang:
                                Znfwait["abots"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "bot:off" or text.lower() == 'bot off':
                            if msg._from in Ang:
                                Znfwait["abots"] = False
                                cl.sendMessage(msg.to,"done boss")

                        elif cmd == "bot:del" or text.lower() == 'bot del':
                            if msg._from in Ang:
                                Znfwait["dbots"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "allrefresh" or text.lower() == 'refresh':
                            if msg._from in Ang:
                                Znfwait["addadmin"] = False
                                Znfwait["deladmin"] = False
                                Znfwait["abots"] = False
                                Znfwait["dbots"] = False
                                Znfwait["ablacklist"] = False
                                Znfwait["dblacklist"] = False
                                Znfwait["Tablacklist"] = False
                                Znfwait["Tdblacklist"] = False
                                cl.sendMessage(msg.to,"done bosquh")

                        elif cmd == "ctadmin" or text.lower() == 'ctadmin':
                            if msg._from in Ang:
                                ma = ""
                                for i in Znfbot["admin"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "ctbot" or text.lower() == 'ctbot':
                            if msg._from in Ang:
                                ma = ""
                                for i in Znfbot["Bots"]:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "notag:on" or text.lower() == 'notag on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag allready on")

                        elif cmd == "notag:off" or text.lower() == 'notag off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["Mentionkick"] = False
                                cl.sendMessage(msg.to,"Notag allready off")

                        elif cmd == "contact:on" or text.lower() == 'contact on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["contact"] = True
                                cl.sendMessage(msg.to,"Contact allready on")

                        elif cmd == "contact:off" or text.lower() == 'contact off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["contact"] = False
                                cl.sendMessage(msg.to,"Contact allready off")

                        elif cmd == "respon:on" or text.lower() == 'respon on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto allready on")

                        elif cmd == "respon:off" or text.lower() == 'respon off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon allready off")

                        elif cmd == "autojoin:on" or text.lower() == 'autojoin on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin allredy on")

                        elif cmd == "autojoin:off" or text.lower() == 'autojoin off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin allready off")

                        elif cmd == "scan:on" or text.lower() == 'scan on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["checkmid"] = True
                                cl.sendMessage(msg.to," allredy on")

                        elif cmd == "scan:off" or text.lower() == 'scan off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["checkmid"] = False
                                cl.sendMessage(msg.to," allready off")

                        elif cmd == "post:on" or text.lower() == 'post on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["checkPost"] = True
                                cl.sendMessage(msg.to,"Check Post allredy on")

                        elif cmd == "post:off" or text.lower() == 'post off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["checkPost"] = False
                                cl.sendMessage(msg.to,"Check Post allready off")

                        elif cmd == "unsend:on" or text.lower() == 'unsend on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["Unsend"] = True
                                cl.sendMessage(msg.to,"Detect unsend allredy on")

                        elif cmd == "unsend:off" or text.lower() == 'unsend off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["Unsend"] = False
                                cl.sendMessage(msg.to,"Detect unsend allready off")

                        elif cmd == "autoleave:on" or text.lower() == 'autoleave on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave allready on")

                        elif cmd == "autoleave:off" or text.lower() == 'autoleave off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave allready off")

                        elif cmd == "autoadd:on" or text.lower() == 'autoadd on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add allready on")

                        elif cmd == "autoadd:off" or text.lower() == 'autoadd off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add allready off")

                        elif cmd == "sticker:on" or text.lower() == 'sticker on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["sticker"] = True
                                cl.sendMessage(msg.to,"Sticker allready on")

                        elif cmd == "sticker:off" or text.lower() == 'sticker off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["sticker"] = False
                                cl.sendMessage(msg.to,"Sticker alleady off")

                        elif cmd == "jticket:on" or text.lower() == 'jticket on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                settings["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Join ticket allready on")

                        elif cmd == "jticket:off" or text.lower() == 'jticket off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                settings["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Notag allready off")

                        elif ("Tban " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Znfbot["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Succses")
                                       except:
                                           pass

                        elif ("Untban " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Znfbot["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif cmd == "tban:on" or text.lower() == 'tban:on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["Tablacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "untban:on" or text.lower() == 'untban:on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["Tdblacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif ("Ban " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Znfbl["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del Znfbl["blacklist"][target]
                                           cl.sendMessage(msg.to,"Succes")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["ablacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "ban:off" or text.lower() == 'ban off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["ablacklist"] = False
                                cl.sendMessage(msg.to,"done boss")

                        elif cmd == "unban:on" or text.lower() == 'unban on':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Send Contact...")

                        elif cmd == "unban:off" or text.lower() == 'unban off':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                                Znfwait["dblacklist"] = False
                                cl.sendMessage(msg.to,"done boss")

                        elif cmd == "bl" or text.lower() == 'bl':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                              if Znfbl["blacklist"] == {}:
                                cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                              else:
                                  mc = "╔══════════════\n╠☛ ❲ BanList ❳☚\n╠══════════════"
                                  for mi_d in Znfbl["blacklist"]:
                                      mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n╚══════════════")

                        elif cmd == "tbanlist" or text.lower() == 'tbanlist':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                              if Znfbl["Talkblacklist"] == {}:
                                cl.sendMessage(to,"╔══════════════\n╠☛ empty list\n╚══════════════")
                              else:
                                  mc = "╔══════════════\n╠☛ ❲ BanList ❳☚\n╠══════════════"
                                  for mi_d in Znfbl["Talkblacklist"]:
                                      mc += "\n╠☛ "+cl.getContact(mi_d).displayName
                                  cl.sendMessage(msg.to,mc + "\n╚══════════════")

                        elif cmd == "hapus bl" or text.lower() == 'hapus bl':
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                              Znfbl["blacklist"] = {}
                              Znfbl["pCancel"] = {}
                              Znfbl["pInvite"] = {}
                              Znfbl["pQr"] = {}
                              ang = cl.getContacts(Znfbl["blacklist"])
                              mc = "%i Blacklist " % len(ang)
                              cl.sendMessage(msg.to,"done boss " +mc)

                        elif text.lower() == ".respon" or text.lower() == "respon.":
                            if msg._from in Ang:
                                if msg.to not in Znfbl["proCancel"] or msg.to not in Znfbl["proInvite"]:
                                    cl.sendMessage(msg.to, "stay boss")
                                else:
                                    del Znfbl["pCancel"][msg.to]
                                    del Znfbl["pInvite"][msg.to]
                                    del Znfbl["pQr"][msg.to]
                                    f=codecs.open('Znfblacklist.json','w','utf-8')
                                    json.dump(Znfbl, f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ka.send(msg.to, "siap bosqu😘")
                                    kb.send(msg.to, "siap bosqu😘")
                                    kc.send(msg.to, "siap bosqu😘")
                                    kd.send(msg.to, "siap bosqu😘")
                                    ke.send(msg.to, "siap bosqu😘")

                        elif 'Add: ' in msg.text:
                           if msg._from in Ang:
                              ang = msg.text.replace('Add: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Znfwait["message"] = ang
                                  cl.sendMessage(msg.to, "「Msg add」 :\n\n「{}」".format(str(ang)))

                        elif 'Left: ' in msg.text:
                           if msg._from in Ang:
                              ang = msg.text.replace('Left: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Znfwait["leftmsg"] = ang
                                  cl.sendMessage(msg.to, "「Msg leave」 :\n\n「{}」".format(str(ang)))

                        elif 'Welcome: ' in msg.text:
                           if msg._from in Ang:
                              ang = msg.text.replace('Welcome: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Znfwait["welcome"] = ang
                                  cl.sendMessage(msg.to, "「Msg wellcome」 :\n\n「{}」".format(str(ang)))

                        elif 'Tag: ' in msg.text:
                           if msg._from in Ang:
                              ang = msg.text.replace('Tag: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Znfwait["msgTag"] = ang
                                  cl.sendMessage(msg.to, "「Msg tag」:\n\n「{}」".format(str(ang)))

                        elif 'Spam: ' in msg.text:
                           if msg._from in Ang:
                              ang = msg.text.replace('Spam: ','')
                              if ang in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Znfwait["spamMsg"] = ang
                                  cl.sendMessage(msg.to, "「Msg spam」 :\n\n「{}」".format(str(ang)))

                        elif 'Sider: ' in msg.text:
                           if msg._from in Ang:
                              znf = msg.text.replace('Sider: ','')
                              if znf in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal boss")
                              else:
                                  Znfwait["siderMsg"] = znf
                                  cl.sendMessage(msg.to, "「Msg cctv」:\n\n「{}」".format(str(znf)))

                        elif text.lower() == "cekmsg":
                            if msg._from in Ang:
                               cl.sendMessage(msg.to, "「Msg add」 :\n「 " + str(Znfwait["message"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg cctv」:\n「 " + str(Znfwait["siderMsg"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg tag」:\n「 " + str(Znfwait["msgTag"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg spam」:\n「 " + str(Znfwait["spamMsg"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg welcome」:\n「 " + str(Znfwait["welcome"]) + " 」")
                               cl.sendMessage(msg.to, "「Msg leave」:\n「 " + str(Znfwait["leftmsg"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "succes join : %s" % str(group.name))

                        elif ("BRATASENA" in msg.text):
                          if Znfwait["selfbot"] == True:
                            if msg._from in Ang:
                               if msg.toType == 2:
                                  group = cl.getGroup(msg.to)
                                  group = ka.getGroup(msg.to)
                                  group = kb.getGroup(msg.to)
                                  group = kc.getGroup(msg.to)
                                  group = kd.getGroup(msg.to)
                                  group = ke.getGroup(msg.to)
                                  nama = [contact.mid for contact in group.members]
                                  for x in nama:
                                      if x not in Angrust:
                                          if x not in Znfbot["Bots"]:
                                              if x not in Znfbot["admin"]:
                                                  try:
                                                      klist=[ka,kb,kc,kd,ke]
                                                      ang=random.choice(klist)
                                                      ang.kickoutFromGroup(msg.to,[x])
                                                  except:
                                                      print ("limit")

    except Exception as error:
        print (error)

while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                oepoll.setRevision(op.revision)
                thread = threading.Thread(target=bot, args=(op,))
                thread.start()
    except Exception as e:
        print(e)
