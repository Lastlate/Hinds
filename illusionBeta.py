# -*- coding: utf-8 -*-

from linepy import *
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,subprocess,GACSender,datetime
import request,urllib.error,pickle,base64,subprocess,unicodedata
from gtts import gTTS
from googletrans import Translator
import traceback
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
botStart = time.time()

cl = LINE()
cl.log("Auth Token : " + str(cl.authToken))
channelToken = cl.getChannelResult()
#cl.log("Channel Token : " + str(channelToken))

ki = LINE()
ki.log("Auth Token : " + str(ki.authToken))
channelToken = ki.getChannelResult()
#ki.log("Channel Token : " + str(channelToken))

kk = LINE()
kk.log("Auth Token : " + str(ki.authToken))

KAC = [cl,ki,kk]

clMID = cl.profile.mid
kiMID = ki.profile.mid
kkMID = kk.profile.mid

Bots = [clMID,kiMID,kkMID]
creator = ["u3d96efa0d532029e9037c6b50dbccfe1"]
Owner = ["u3d96efa0d532029e9037c6b50dbccfe1"]
admin = ["u3d96efa0d532029e9037c6b50dbccfe1"]

clProfile = cl.getProfile()
kiProfile = ki.getProfile()
kkProfile = kk.getProfile()
#ki3Profile = ki3.getProfile()
#ki4Profile = ki4.getProfile()

lineSettings = cl.getSettings()
kiSettings = ki.getSettings()
kkSettings = kk.getSettings()
#ki3Settings = ki3.getSettings()
#ki4Settings = ki4.getSettings()

oepoll = OEPoll(cl)
oepoll1 = OEPoll(ki)
oepoll2 = OEPoll(kk)
#oepoll3 = OEPoll(ki3)
#oepoll4 = OEPoll(ki4)

responsename = cl.getProfile().displayName
responsename2 = ki.getProfile().displayName
#responsename3 = ki2.getProfile().displayName
#responsename4 = ki3.getProfile().displayName
#responsename5 = ki4.getProfile().displayName
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")

read = json.load(readOpen)
settings = json.load(settingsOpen)


with open('tval.pkl', 'rb') as f:
    seeall,tadmin,banned,kickLockList,autoLikeSetting,save1,wait,botProtect,save2,dublist,blockinvite,jfkeyword,join_delay,join_time,joinDetail,preventBlockURL,tyfeFollow,autoDeny,mentmedat = pickle.load(f,encoding='latin1')
with open('Owner.json', 'r') as fp:
    Owner = json.load(fp)
with open('admin.json', 'r') as fp:
    admin = json.load(fp)
    


myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}

myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
#    time.sleep(3)
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
    
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
    
def logError(text):
    cl.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        traceback.print_exc()
        
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
        traceback.print_exc()

def Rapid1Say(mtosay):
    line.sendMessage(Rapid1To,mtosay)
        
def helpmessage():
    helpMessage = "﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏" + "\n" + \
                  "[ERROR] SCRIPT BREAKDOWNED" + "\n" + \
                  "ー═✠〆ⁱˡˡᵘˢᵗᵉᵈ✠͜͡ই❥─" + "\n" + \
                  "[ERROR] SCRIPT BREAKDOWNED" + "\n" + \
                  "" + "\n" + \
                  "" + "\n" + \
                  "!คำสั่ง" + "\n" + \
                  "" + "\n" + \
                  "!รีบอท" + "\n" + \
                  "!เวลาออน" + "\n" + \
                  "!สปีด" + "\n" + \
                  "!ตั้งค่า" + "\n" + \
                  "!บอท" + "\n" + \
                  "" + "\n" + \
                  "Defensive" + "\n" + \
                  " เพิ่มเพื่อน [on/off]" + "\n" + \
                  " เข้ากลุ่มออโต้ [on/off]" + "\n" + \
                  " ออกกลุ่ม [on/off]" + "\n" + \
                  " อ่านออโต้ [on/off]" + "\n" + \
                  " เชคติ้ก [on/off]" + "\n" + \
                  " ตอบกลับ [on/off]" + "\n" + \
                  " .kicktag [on/off]" + "\n" + \
                  " autoblock [on/off]" + "\n" + \
                  " g [on/off]" + "\n" +\
                  " bye [on/off]" + "\n" + \
                  " pro [on/off]" + "\n" + \
                  "ทั่วไป" + "\n" + \
                  " !me" + "\n" + \
                  " !ไอดี" + "\n" + \
                  " !ชื่อ" + "\n" + \
                  " !ตัส" + "\n" + \
                  " !รูป" + "\n" + \
                  " !วิดีโอ" + "\n" + \
                  " !ปก" + "\n" + \
                  "วิธีใช้ (!ขโมย__ @)" + "\n" + \
                  " !ขโมยคท." + "\n" + \
                  " !ขโมยไอดี" + "\n" + \
                  " !ขโมยชื่อ" + "\n" + \
                  " !ขโมยตัส" + "\n" + \
                  " !ขโมยรูป" + "\n" + \
                  " !ขโมยวิดีโอ" + "\n" + \
                  " !ขโมยปก" + "\n" + \
                  " !ลอกคท." + "\n" + \
                  " !คืนร่าง" + "\n" + \
                  "↓ใช้ในกลุ่ม↓" + "\n" + \
                  " !คนสร้างกลุ่ม" + "\n" + \
                  " !ไอดีกลุ่ม" + "\n" + \
                  " !ชื่อกลุ่ม" + "\n" + \
                  " !รูปกลุ่ม" + "\n" + \
                  " !ตั๋ว" + "\n" + \
                  " !เปิด/ปิดลิงค์" + "\n" + \
                  " !รายชื่อกลุ่ม" + "\n" + \
                  " !สมาชิกกลุ่ม" + "\n" + \
                  " !เกี่ยวกับกลุ่ม" + "\n" + \
                  " อื่นๆ⇩" + "\n" +\
                  " !เตะ" + "\n" + \
                  " !แทค" + "\n" +\
                  " !ลบรัน (ข้อความ)" + "\n" + \
                  " !ยกเลิกเชิญ " + "\n" +\
                  " !ส่อง (แท๊ก) " + "\n" +\
                  " !เด้ง" + "\n" +\
                  " .name " + "\n" + \
                  " sms: (เบอร์โทรศัพท์)" + "\n" + \
                  " .speed+" + "\n" + \
                  " .หา " + "\n" + \
                  " -sh " + "\n" + \
                  " ———————————— " + "\n" + \
                  " illusion:google" + "\n" + \
                  " illusion:who (MID)" + "\n" + \
                  "[ERROR] SCRIPT BREAKDOWNED" + "\n" + \
                  "line.me/ti/p/~illustedtearsz"
    return helpMessage
    
def helptexttospeech():
    helpTextToSpeech =   "คำสั่งคิกเกอร์ :" + "\n" + \
                         "Illusion:join" + "\n" +\
                         "Illusion:remove " + "\n" +\
                         "Illusion kicker Beta Test"
    return helpTextToSpeech
    
def helptranslate():
    helpTranslate =    "╔══[ T R A N S L A T E ]" + "\n" + \
                       "╠ af : afrikaans" + "\n" + \
                       "╠ sq : albanian" + "\n" + \
                       "╠ am : amharic" + "\n" + \
                       "╠ ar : arabic" + "\n" + \
                       "╠ hy : armenian" + "\n" + \
                       "╠ az : azerbaijani" + "\n" + \
                       "╠ eu : basque" + "\n" + \
                       "╠ be : belarusian" + "\n" + \
                       "╠ bn : bengali" + "\n" + \
                       "╠ bs : bosnian" + "\n" + \
                       "╠ bg : bulgarian" + "\n" + \
                       "╠ ca : catalan" + "\n" + \
                       "╠ ceb : cebuano" + "\n" + \
                       "╠ ny : chichewa" + "\n" + \
                       "╠ zh-cn : chinese (simplified)" + "\n" + \
                       "╠ zh-tw : chinese (traditional)" + "\n" + \
                       "╠ co : corsican" + "\n" + \
                       "╠ hr : croatian" + "\n" + \
                       "╠ cs : czech" + "\n" + \
                       "╠ da : danish" + "\n" + \
                       "╠ nl : dutch" + "\n" + \
                       "╠ en : english" + "\n" + \
                       "╠ eo : esperanto" + "\n" + \
                       "╠ et : estonian" + "\n" + \
                       "╠ tl : filipino" + "\n" + \
                       "╠ fi : finnish" + "\n" + \
                       "╠ fr : french" + "\n" + \
                       "╠ fy : frisian" + "\n" + \
                       "╠ gl : galician" + "\n" + \
                       "╠ ka : georgian" + "\n" + \
                       "╠ de : german" + "\n" + \
                       "╠ el : greek" + "\n" + \
                       "╠ gu : gujarati" + "\n" + \
                       "╠ ht : haitian creole" + "\n" + \
                       "╠ ha : hausa" + "\n" + \
                       "╠ haw : hawaiian" + "\n" + \
                       "╠ iw : hebrew" + "\n" + \
                       "╠ hi : hindi" + "\n" + \
                       "╠ hmn : hmong" + "\n" + \
                       "╠ hu : hungarian" + "\n" + \
                       "╠ is : icelandic" + "\n" + \
                       "╠ ig : igbo" + "\n" + \
                       "╠ id : indonesian" + "\n" + \
                       "╠ ga : irish" + "\n" + \
                       "╠ it : italian" + "\n" + \
                       "╠ ja : japanese" + "\n" + \
                       "╠ jw : javanese" + "\n" + \
                       "╠ kn : kannada" + "\n" + \
                       "╠ ki : kazakh" + "\n" + \
                       "╠ km : khmer" + "\n" + \
                       "╠ ko : korean" + "\n" + \
                       "╠ ku : kurdish (kurmanji)" + "\n" + \
                       "╠ ky : kyrgyz" + "\n" + \
                       "╠ lo : lao" + "\n" + \
                       "╠ la : latin" + "\n" + \
                       "╠ lv : latvian" + "\n" + \
                       "╠ lt : lithuanian" + "\n" + \
                       "╠ lb : luxembourgish" + "\n" + \
                       "╠ mk : macedonian" + "\n" + \
                       "╠ mg : malagasy" + "\n" + \
                       "╠ ms : malay" + "\n" + \
                       "╠ ml : malayalam" + "\n" + \
                       "╠ mt : maltese" + "\n" + \
                       "╠ mi : maori" + "\n" + \
                       "╠ mr : marathi" + "\n" + \
                       "╠ mn : mongolian" + "\n" + \
                       "╠ my : myanmar (burmese)" + "\n" + \
                       "╠ ne : nepali" + "\n" + \
                       "╠ no : norwegian" + "\n" + \
                       "╠ ps : pashto" + "\n" + \
                       "╠ fa : persian" + "\n" + \
                       "╠ pl : polish" + "\n" + \
                       "╠ pt : portuguese" + "\n" + \
                       "╠ pa : punjabi" + "\n" + \
                       "╠ ro : romanian" + "\n" + \
                       "╠ ru : russian" + "\n" + \
                       "╠ sm : samoan" + "\n" + \
                       "╠ gd : scots gaelic" + "\n" + \
                       "╠ sr : serbian" + "\n" + \
                       "╠ st : sesotho" + "\n" + \
                       "╠ sn : shona" + "\n" + \
                       "╠ sd : sindhi" + "\n" + \
                       "╠ si : sinhala" + "\n" + \
                       "╠ sk : slovak" + "\n" + \
                       "╠ sl : slovenian" + "\n" + \
                       "╠ so : somali" + "\n" + \
                       "╠ es : spanish" + "\n" + \
                       "╠ su : sundanese" + "\n" + \
                       "╠ sw : swahili" + "\n" + \
                       "╠ sv : swedish" + "\n" + \
                       "╠ tg : tajik" + "\n" + \
                       "╠ ta : tamil" + "\n" + \
                       "╠ te : telugu" + "\n" + \
                       "╠ th : thai" + "\n" + \
                       "╠ tr : turkish" + "\n" + \
                       "╠ uk : ukrainian" + "\n" + \
                       "╠ ur : urdu" + "\n" + \
                       "╠ uz : uzbek" + "\n" + \
                       "╠ vi : vietnamese" + "\n" + \
                       "╠ cy : welsh" + "\n" + \
                       "╠ xh : xhosa" + "\n" + \
                       "╠ yi : yiddish" + "\n" + \
                       "╠ yo : yoruba" + "\n" + \
                       "╠ zu : zulu" + "\n" + \
                       "╠ fil : Filipino" + "\n" + \
                       "╠ he : Hebrew" + "\n" + \
                       "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                         "Contoh : tr-id cl Cantik"
    return helpTranslate
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
def lineBot(op):
    try:
        if op.type == 0:
            print ("[ 0 ] รอคำสั่งー═✠〆ⁱˡˡᵘˢᵗᵉᵈ✠͜͡ই❥─")
            return
        if op.type == 5:
            print ("[ 5 ] มีคนแอดมาー═✠〆ⁱˡˡᵘˢᵗᵉᵈ✠͜͡ই❥─")
            if settings["autoblock"] == True:
                cl.sendMessage(op.param1, "ไง {} ตอนนี้กำลังเปิดระบบบล็อคน่ะ..แจ้งในกลุ่มนะ?".format(str(cl.getContact(op.param1).displayName)))
                cl.blockContact(op.param1)
        if op.type == 13:
            print ("[ 13 ] มีคนเชิญเข้ากลุ่มー═✠〆ⁱˡˡᵘˢᵗᵉᵈ✠͜͡ই❥─")
            cl.sendMessage(op.param1, "ขณะนี้มีการเชิญสมาชิกเข้าร่วมกลุ่ม")
            group = cl.getGroup(op.param1)
            if settings["autoJoin"] == True:
                cl.acceptGroupInvitation(op.param1)
                ki.acceptGroupInvitation(op.param1)
                kk.acceptGroupInvitation(op.param1)
        if op.type == 17:
           print ("Member Joined")
           if settings["greetings"] == True:
              zerot = cl.getGroup(op.param1)
              dan = cl.getContact(op.param2)
              cl.sendContact(op.param1, op.param2)
              cl.sendMessage(op.param1, "สวัสดี {}, Welcome to Group {}\nเข้ามาแล้วทำตัวดีๆละ\nอย่าไปเป็นบ้าลบเพื่อนๆออกกลุ่มนะ (｀・ω・´)".format(str(dan.displayName),str(zerot.name)))
              cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 15:
            print ("[15]Member Leaved")
            if settings["bye"] == True:
               dan = cl.getContact(op.param2)
               tgb = cl.getGroup(op.param1)
               cl.sendMessage(op.param1, "เอ้า {}, ได้ออกจากกลุ่ม {} \nยืนไว้อาลัยแด่เขาเป็นเวลา3วินาที  (｀・ω・´)".format(str(dan.displayName),str(tgb.name)))
               cl.sendContact(op.param1, op.param2)
               cl.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net{}".format(dan.picturePath))
        if op.type == 11:
            kk.sendMessage(op.param1, "ขณะนี้มีการเปลี่ยนแปลงการตั้งค่ากลุ่ม(｀・ω・´)")
            if settings["linkProtect"] == True:
               ki.sendMessage(op.param1, "โหมดห้ามเปลี่ยนแปลงการตั้งค่าเปิดอยู่")
               ki.kickoutFromGroup(op.param1,[op.param2])
               G = ki.getGroup(op.param1)
               G.preventedJoinByTicket = True
               ki.updateGroup(G)
               ki.sendMessage(op.param1, "ปิดลิงค์เรียบร้อยแล้ว(｀・ω・´)")
        if op.type == 26:
            print ("[ 26 ] ได้รับข้อความละ")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                if sender in settings["mimic"]["target"] and settings["mimic"]["status"] == True and settings["mimic"]["target"][sender] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendMessage(msg.to,text)
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
               	 if 'MENTION' in list(msg.contentMetadata.keys()) != None:
                    if settings["kickMention"] == True:
                        contact = cl.getContact(msg._from)
                        cName = contact.displayName
                        balas = ["OmaeWaMoeShinDeiru" + cName + " แท๊กฉันหาพ่อเธอหรือ~ ตายซะ"]
                        ret_ = random.choice(balas)
                        name = re.findall(r'@(\w+)', msg.text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                              if clMID in mention["M"]:
                                     cl.sendMessage(msg.to,ret_)
                                     ki.kickoutFromGroup(msg.to,[msg._from])
                    if "MENTION" in list(msg.contentMetadata.keys()) != None:
                         if settings['detectMention'] == True:
                             contact = cl.getContact(msg._from)
                             cName = contact.displayName
                             balas = ["『 Auto Respon』\n " + cName + "\nแทคทำไมหืม?"]
                             ret_ = "" + random.choice(balas)
                             name = re.findall(r'@(\w+)', msg.text)
                             mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                             mentionees = mention['MENTIONEES']
                             for mention in mentionees:
                                   if mention['M'] in clMID:
                                          cl.sendMessage(to,ret_)
                                          cl.sendMessageWithMention(to, contact.mid)
                                          break										  
                if msg.text in ["Me","me",".me",".Me","คท","/me","!me"]:
                    cl.sendMessage(msg.to,"มีเธอมีฉันมีกันตลอดไป😂")
                if msg.text in ["sp","speed",".speed","/speed","Sp",".Speed"]:
                    cl.sendMessage(msg.to,"ไม่ต้องเช็คก็รู้ว่าแรงอยู่แล้ว5555")
                if msg.text in ["runtime","Runtime","/uptime","ออน",".uptime"]:
                    cl.sendMessage(msg.to,"ล็อคเชลเก็บเวลาหราจร้ะ5555")
                if msg.text in ["555","555+","55","5555","55555"]:
                    cl.sendMessage(msg.to,"ขำให้ตายเลยมุง")				
                if msg.text in ["ถถถ"]:
                    cl.sendMessage(msg.to,"บ้านผลิตถุงยางขายหราจ้ะ?")	
        if op.type == 25:
            print ("[ 25 ] ส่งข้อความแล้วー═✠〆ⁱˡˡᵘˢᵗᵉᵈ✠͜͡ই❥─")
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if msg.contentType == 0:
                if text is None:
                    return
        if op.type == 55:
            print ("[ 55 ] มีคนอ่านข้อความ")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                   pass
            except:
                pass
    except Exception as error:
        logError(error)
        if op.type == 19:
            try:
                if op.param3 in lineMID:
                    if op.param2 in kiMID:
                        G = ki.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                #        kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                 #       time.sleep(0.0001)
               #         ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                 #       time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                    else:
                        G = ki.getGroup(op.param1)                                                
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        ki.updateGroup(G)
                        ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
             #           kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
             #           time.sleep(0.0001)
             #           ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
              #          time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
                    #    settings["blacklist"][op.param2] = True                       

                elif op.param3 in kiMID:
                    if op.param2 in lineMID:
                        G = kk.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        #kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                    #    time.sleep(0.0001)
                  #      ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                    #    time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        kk.updateGroup(G)
                    else:
                        G = kk.getGroup(op.param1)
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        G.preventedJoinByTicket = False
                        kk.updateGroup(G)
                        ticket = kk.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        ki.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
                        kk.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                        time.sleep(0.0001)
              #          kc.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
              #          time.sleep(0.0001)
             #           ke.acceptGroupInvitationByTicket(op.param1,format(str(ticket)))
                #        time.sleep(0.0001)						
                        G.preventedJoinByTicket = True
                        ki.updateGroup(G)
              #          settings["blacklist"][op.param2] = True
    #    if op.type == 32:
    #    cl.sendMessage(op.param1, "ขณะนี้มีการยกเลิกเชิญสมาชิกเกิดขึ้น")
        
 #------------------------------------------------------------------------------#
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
                elif text.lower() == '!คำสั่ง':
                     helpMessage = helpmessage()
                     cl.sendMessage(to, str(helpMessage))
                     cl.sendContact(to, "u3d96efa0d532029e9037c6b50dbccfe1")
                elif text.lower() == 'kickcmd':
                     helpTextToSpeech = helptexttospeech()
                     cl.sendMessage(to, str(helpTextToSpeech))
                elif text.lower() == 'translate':
                     helpTranslate = helptranslate()
                     cl.sendMessage(to, str(helpTranslate))
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
#                elif text.lower() == 'say ':
 #               txts = msg.text.split(" ")
  #              jmlh = int(txts[2])
   #             teks = msg.text.replace("say "+str(txts[1])+" "+str(jmlh)+" ","")
    #            tulisan = jmlh * (teks+"\n")
     #           if txts[1] == "on":
      #              if jmlh <= 100000:
       #                for x in range(jmlh):
        #                   cl.sendMessage(msg.to, teks)
         #           else:
          #             cl.send tli(msg.to, "Out of Range!")
           #     elif txts[1] == "off":
            #        if jmlh <= 100000:
             #           cl.sendMessage(msg.to, tulisan)
              #      else:
                #        cl.sendMessage(msg.to, "Out Of Range!")
                
                elif text.lower() == '.speed+':
                    start = time.time()
                    cl.sendMessage(to, "กำลังทดสอบ")
                    elapsed_time = time.time() - start
                    cl.sendMessage(msg.to, "[ %s วินาที ] [ " % (elapsed_time) + str(int(round((time.time() - start) * 1000)))+" ปิง ]")
                    now2 = datetime.datetime.now()
                    nowT = datetime.datetime.strftime(now2,"%H")
                    nowM = datetime.datetime.strftime(now2,"%M")
                    nowS = datetime.datetime.strftime(now2,"%S")
                    tm = "\n\n"+nowT+":"+nowM+":"+nowS
                    cl.sendMessage(to, "เร็วมั้ยล่ะ😂😂\n"+tm)
                elif msg.text.lower() == "!เด้ง":
                     cl.sendContact(to, "u1f41296217e740650e0448b96851a3e2',")
                elif 'illusion:remove' in text.lower():
                       targets = []
                       key = eval(msg.contentMetadata["MENTION"])
                       key["MENTIONEES"] [0] ["M"]
                       for x in key["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               ki.kickoutFromGroup(msg.to,[target])           
                               print ("K1 Kick User")
                           except:
                               ki.sendMessage(msg.to,"Failed")                             
                elif "รัว " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("รัว "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "1":
                         if jmlh <= 100000:
                          for x in range(jmlh):
                            cl.sendMessage(msg.to, teks) 
                elif msg.text.lower() == "kickprev on":
                        if msg.to not in kickLockList:
                            kickLockList.append(msg.to)
                            cl.sendMessage(msg.to,"เปิดโหมดห้ามลบแล้ว (^・ω・^ )")
                elif msg.text.lower().startswith("deco "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    cl.sendMentionFooter(to, say, sender, "https://line.me/ti/p/~illusionai2", "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName);cl.sendMessage()
                elif ".name " in msg.text.lower():
                    spl = re.split(".name ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prof = cl.getProfile()
                        prof.displayName = spl[1]
                        cl.updateProfile(prof)
                        now2 = datetime.datetime.now()
                        nowT = datetime.datetime.strftime(now2,"%H")
                        nowM = datetime.datetime.strftime(now2,"%M")
                        nowS = datetime.datetime.strftime(now2,"%S")
                        tm = "\n\n"+nowT+":"+nowM+":"+nowS
                        cl.sendMessage(msg.to,"Renamed Success\n"+tm)
                elif ".เตะ " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            cl.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        cl.findAndAddContactsByMid(allmid)
                        cl.inviteIntoGroup(msg.to,allmid)
                        cl.cancelGroupInvitation(msg.to,allmid)
                elif msg.text.lower().startswith("sms: "):
                    pnum = re.split("sms: ",msg.text,flags=re.IGNORECASE)[1]
                    pnum = "66"+pnum[1:]
                    GACReq = GACSender.send(pnum)
                    if GACReq.responseNum == 0:
                        if msg.toType != 0:
                                cl.sendMessage(msg.to,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                        else:
                                cl.sendMessage(msg.from_,"ส่ง SMS สำเร็จแล้ว (｀・ω・´)")
                    elif GACReq.responseNum == 1:
                        if msg.toType != 0:
                                cl.sendMessage(msg.to,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                        else:
                                cl.sendMessage(msg.from_,"ไม่สามารถส่ง SMS ได้ เนื่องจากมีการส่งข้อความไปยังเบอร์เป้าหมายในเวลาที่ใกล้เคียงกันมากเกินไป (｀・ω・´)\nกรุณารออย่างมาก 30 วินาทีแล้วลองอีกครั้ง")
                    else:
                        if msg.toType != 0:
                                cl.sendMessage(msg.to,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                        else:
                                cl.sendMessage(msg.from_,"พบข้อผิดพลาดที่ไม่รู้จัก (｀・ω・´)")
                elif msg.text.lower() == "!crash":
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': "cl"}
                    cl.sendMessage(msg)
                elif msg.text.lower() == "ไวรัส01":
                	cl.sendMessage(to, "1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.11.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.")
                elif "รัว " in msg.text:
                    txt = msg.text.split(" ")
                    jmlh = int(txt[2])
                    teks = msg.text.replace("รัว "+str(txt[1])+" "+str(jmlh)+" ","")
                    tulisan = jmlh * (teks+"\n")
                    if txt[1] == "":
                         if jmlh <= 100000:
                          for x in range(jmlh):
                            cl.sendMessage(msg.to, teks) 
                     #  cl.sendMessage(msg.to, "Out of Range!")
                    #   elif txt[1] == "off":
              #           if jmlh <= 100000:
                    #    cl.sendMessage(msg.to, tulisan)
            #    elif "say: " in msg.text:
 #                 bctxt = msg.text.replace("say: ", "")
          #        t = 5
  #                x = 5
   #               while(t):
       #             cl.sendMessage(to, (bctxt))
             #       t-=1
    #              while(x):
            #        cl.sendMessage(to, (bctxt))
   #                 x-=1
    #            elif "3: " in msg.text:
     #             bctxt = msg.text.replace("3: ", "")
   #               t = 3
   #               while(t):
  #                  cl.sendMessage(msg.to, (bctxt))
        #            t-=1
                elif "-sh " in msg.text.lower():
                    spl = re.split("-sh ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        try:
                            cl.sendMessage(msg.to,subprocess.getoutput(spl[1]))
                        except:
                            pass
                
                elif "illusion:google " in msg.text.lower():
                   spl = re.split("illusion:google ",msg.text,flags=re.IGNORECASE)
                   if spl[0] == "":
                       if spl[1] != "":
                           try:
                               if msg.toType != 0:
                                   cl.sendMessage(msg.to,"กำลังรับข้อมูล กรุณารอสักครู่..")
                               else:
                                   cl.sendMessage(msg.from_,"กำลังรับข้อมูล กรุณารอสักครู่..")
                               resp = BeautifulSoup(requests.get("https://www.google.co.th/search",params={"q":spl[1],"gl":"th"}).content,"html.parser")
                               text = "ผลการค้นหาจาก Google:\n\n"
                               for el in resp.findAll("h3",attrs={"class":"r"}):
                                   try:
                                       tmp = el.a["class"]
                                       continue
                                   except:
                                       pass
                                   try:
                                       if el.a["href"].startswith("/search?q="):
                                           continue
                                   except:
                                       continue
                                   text += el.a.text+"\n"
                                   text += str(el.a["href"][7:]).split("&sa=U")[0]+"\n\n"
                               text = text[:-2]
                               if msg.toType != 0:
                                   cl.sendMessage(msg.to,str(text))
                               else:
                                   cl.sendMessage(msg.from_,str(text))
                           except Exception as e:
                               print(e)
                elif msg.text.lower() == ".speed":
                     start = time.time()
                     cl.sendMessage(msg.to,"Connecting to LINE API ...")
                     cl.sendMessage(msg.to,str(int(round((time.time() - start) * 1000)))+" หน่วย")
                elif msg.text.lower() == "!ยกเลิกเชิญ":
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for i in gMembMids:
                            cl.cancelGroupInvitation(msg.to,[i])
                elif "!ส่อง " in msg.text.lower():
                    spl = re.split("!ส่อง ",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        for i in range(len(prov)):
                            uid = prov[i]["M"]
                            userData = cl.getContact(uid)
                            try:
                                cl.sendImageWithUrl(msg.to,"http://dl.profile.line.naver.jp/"+userData.pictureStatus)
                            except:
                                pass
                            cl.sendMessage(msg.to,"ชื่อที่แสดง: "+userData.displayName)
                            cl.sendMessage(msg.to,"ข้อความสเตตัส:\n"+userData.statusMessage)
                            cl.sendMessage(msg.to,"ไอดีบัญชี: "+userData.mid)
                            msg.contentType = 13
                            msg.text = None
                            msg.contentMetadata = {'mid': userData.mid}
                            cl.sendMessage(msg)                
                elif "!ลบรัน" in msg.text.lower():
                    spl = re.split("!ลบรัน",msg.text,flags=re.IGNORECASE)
                    if spl[0] == "":
                        spl[1] = spl[1].strip()
                        ag = cl.getGroupIdsInvited()
                        txt = "กำลังยกเลิกเชิญเข้ากลุ่มจำนวน "+str(len(ag))+" กลุ่ม"
                        if spl[1] != "":
                            txt = txt + " ด้วยข้อความ \""+spl[1]+"\""
                        txt = txt + "\nกรุณารอสักครู่.."
                        cl.sendMessage(msg.to,txt)
                        procLock = len(ag)
                        for gr in ag:
                            try:
                                cl.acceptGroupInvitation(gr)
                                if spl[1] != "":
                                    cl.sendMessage(gr,spl[1])
                                cl.leaveGroup(gr)
                            except:
                                pass
                        cl.sendMessage(msg.to,"สำเร็จแล้ว")
                elif "!เตะ " in msg.text.lower():
                    if msg.toType == 2:
                        prov = eval(msg.contentMetadata["MENTION"])["MENTIONEES"]
                        allmid = []
                        for i in range(len(prov)):
                            cl.kickoutFromGroup(msg.to,[prov[i]["M"]])
                            allmid.append(prov[i]["M"])
                        cl.findAndAddContactsByMid(allmid)
                        cl.inviteIntoGroup(msg.to,allmid)
                        cl.cancelGroupInvitation(msg.to,allmid)
                elif "!เชิญโทร" == msg.text.lower():
                    cl.inviteIntoGroupCall(msg.to,[uid.mid for uid in cl.getGroup(msg.to).members if uid.mid != cl.getProfile().mid])
                    cl.sendMessage(to, "เชิญโทรสำเร็จแล้ว(′・ω・`)")
                elif text.lower() == '!สปีด':
                    start = time.time()
                    elapsed_time = time.time() - start
                    cl.sendMessage(to,format(str(elapsed_time)))
              #      cl.sendMessage(to, "แปปดิกำลังโหลด--")
         #           cl.sendMessage(to, "เชลบอท ー═✠〆ⁱˡˡᵘˢᵗᵉᵈ✠͜͡ই❥─")
         #           cl.sendMessage(to, "line.me/ti/p/~illustedtearsz")
                elif text.lower() == 'reboot':
                    cl.sendMessage(to, "Rebooting")
                    time.sleep(5)
                    cl.sendMessage(to, "Finished wait 10 secs to use again")
                    restartBot()
                elif text.lower() == '!เวลาออน':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "เปิดมาประมาณ {} ละ".format(str(runtime)))
                elif text.lower() == '!บอท':
                    try:
                        arr = []
                        owner = "u3d96efa0d532029e9037c6b50dbccfe1"
                        creator = cl.getContact(owner)
                        contact = cl.getContact(clMID)
                        grouplist = cl.getGroupIdsJoined()
                        contactlist = cl.getAllContactIds()
                        blockedlist = cl.getBlockedContactIds()
                        ret_ = "ข้อมูลบอท\n"
                        ret_ += "\n ชื่อ : {}".format(contact.displayName)
                        ret_ += "\n กลุ่ม : {}".format(str(len(grouplist)))
                        ret_ += "\n เพื่อน : {}".format(str(len(contactlist)))
                        ret_ += "\n บล็อค : {}".format(str(len(blockedlist)))
                        ret_ += "\n [ เชล]"
                        ret_ += "\n เวอร์ชั่น : [ERROR] SCRIPT BREAKDOWNED"
                        ret_ += "\nCreator : {}".format(creator.displayName)
                        ret_ += "\n[line.me/ti/p/~illustedtearsz]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
                elif text.lower() == '!ตั้งค่า':
                    try:
                        ret_ = "╔══[ Status ]"
                        if settings["autoAdd"] == True: ret_ += "\n╠ Auto Add ✅"
                        else: ret_ += "\n╠ Auto Add ❌"
                        if settings["autoJoin"] == True: ret_ += "\n╠ Auto Join ✅"
                        else: ret_ += "\n╠ Auto Join ❌"
                        if settings["autoLeave"] == True: ret_ += "\n╠ Auto Leave ✅"
                        else: ret_ += "\n╠ Auto Leave ❌"
                        if settings["autoRead"] == True: ret_ += "\n╠ Auto Read ✅"
                        else: ret_ += "\n╠ Auto Read ❌"
                        if settings["checkSticker"] == True: ret_ += "\n╠ Check Sticker ✅"
                        else: ret_ += "\n╠ Check Sticker ❌"
                        if settings["detectMention"] == True: ret_ += "\n╠ Detect Mention ✅"
                        else: ret_ += "\n╠ Detect Mention ❌"
                        if settings["kickMention"] == True: ret_ += "\n╠ kick Mention ✅"
                        else: ret_ += "\n╠ kick Mention ❌"
                        if settings["greetings"] == True: ret_ += "\n╠ Greetings✅"
                        else: ret_ += "\n╠ Greetings❌"
                        if settings["autoblock"] == True: ret_ += "\n╠ ออโต้บล็อค ✅"
                        else: ret_ += "\n╠ ออโต้บล็อค ❌"
                        if settings["bye"] == True: ret_ += "\n╠ อำลา ✅"
                        else: ret_ += "\n╠ อำลา ❌"
                        if settings["protect"] == True: ret_ += "\n╠ Pro✅"
                        else: ret_ += "\n╠ Pro ❌"
                        if settings["linkProtect"] == True: ret_ += "\n╠ Pro2✅"
                        else: ret_ += "\n╠ Pro2 ❌"
                        ret_ += "\n╚══[ Status ]"
                        cl.sendMessage(to, str(ret_))
                    except Exception as e:
                        cl.sendMessage(msg.to, str(e))
                elif text.lower() == 'autoblock on':
                    settings["autoblock"] = True
                    cl.sendMessage(to, "True")
                elif text.lower() == 'autoblock off':
                    settings["autoblock"] = False
                    cl.sendMessage(to, "False")
                elif text.lower() == 'bye on':
                    settings["bye"] = True
                    cl.sendMessage(to, "1")
                elif text.lower() == 'bye off':
                    settings["bye"] = False
                    cl.sendMessage(to, "0")
                elif text.lower() == "pro on":
                   settings["protect"] = True
                   cl.sendMessage(to, "1")
                elif text.lower() == "pro off":
                   settings["protect"] = False
                   cl.sendMessage(to, "0")
                elif text.lower() == 'g on':
                    settings["greetings"] = True
                    cl.sendMessage(to, "True")
                elif text.lower() == 'g off':
                    settings["greetings"] = False
                    cl.sendMessage(to, "False")
                elif text.lower() == 'เพิ่มเพื่อน on':
                    settings["autoAdd"] = True
                    cl.sendMessage(to, "เปิดละ")
                elif text.lower() == '.kicktag on':
                    settings["kickMention"] = True
                    cl.sendMessage(to, "เปิดละ")
                elif text.lower() == '.kicktag off':
                    settings["kickMention"] = False
                    cl.sendMessage(to, "ปิดละ")
                elif text.lower() == 'gpro on':
                     settings["linkProtect"] = True
                elif text.lower() == 'gpro off':
                     settings["linkProtect"] = False
                elif text.lower() == 'เพิ่มเพื่อน off':
                    settings["autoAdd"] = False
                    cl.sendMessage(to, "ปิดละ")
                elif text.lower() == 'เข้ากลุ่มออโต้ on':
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "เปิดละ")
                elif text.lower() == 'เข้ากลุ่มออโต้ off':
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "ปิดละ")
                elif text.lower() == 'ออกกลุ่ม on':
                    settings["autoLeave"] = True
                    cl.sendMessage(to, "เปิดละ")
                elif text.lower() == 'ออกกลุ่ม off':
                    settings["autoLeave"] = False
                    cl.sendMessage(to, "ปิดละ")
                elif text.lower() == 'อ่านออโต้ on':
                    settings["autoRead"] = True
                    cl.sendMessage(to, "เปิดละ")
                elif text.lower() == 'อ่านออโต้ off':
                    settings["autoRead"] = False
                    cl.sendMessage(to, "ปิดละ")
                elif text.lower() == 'เชคติ้ก on':
                    settings["checkSticker"] = True
                    cl.sendMessage(to, "เปิดละ")
                elif text.lower() == 'เชคติ้ก off':
                    settings["checkSticker"] = False
                    cl.sendMessage(to, "ปิดละ")
                elif text.lower() == 'ตอบกลับ on':
                    settings["detectMention"] = True
                    cl.sendMessage(to, "เปิดละ")
                elif text.lower() == 'ตอบกลับ off':
                    settings["detectMention"] = False
                    cl.sendMessage(to, "ปิดละ")
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
                elif text.lower() == "!me":
                    cl.sendMentionFooter(to, 'ー═✠〆ⁱˡˡᵘˢⁱᵒⁿ✠͜͡ই❥─\n', sender, "https://line.me/ti/p/~illusionai2", "http://dl.profile.line-cdn.net/"+cl.getContact(sender).pictureStatus, cl.getContact(sender).displayName);cl.sendMessage(to, cl.getContact(sender).displayName, contentMetadata = {'previewUrl': 'http://dl.profile.line-cdn.net/'+cl.getContact(sender).pictureStatus, 'i-installUrl': 'https://line.me/ti/p/~illusionai2', 'type': 'mt', 'subText': "Illusion Bot", 'a-installUrl': 'https://line.me/ti/p/~illusionai2', 'a-installUrl': ' https://line.me/ti/p/~illusionai2', 'a-packageName': 'com.spotify.music', 'countryCode': 'ID', 'a-linkUri': 'https://line.me/ti/p/~illusionai2', 'i-linkUri': 'https://line.me/ti/p/~illusionai2', 'id': 'mt000000000a6b79f9', 'text': 'Illusion', 'linkUri': 'https://line.me/ti/p/~illusionai2'}, contentType=19)
                elif text.lower() == '!ไอดี':
                    cl.sendMessage(msg.to,"[ไอดี [ERROR] SCRIPT BREAKDOWNED]\n" +  clMID)
                elif text.lower() == '!ชื่อ':
                    me = cl.getContact(clMID)
                    cl.sendMessage(msg.to,"[ชื่อ [ERROR] SCRIPT BREAKDOWNED]\n" + me.displayName)
                elif text.lower() == '!ตัส':
                    me = cl.getContact(clMID)
                    cl.sendMessage(msg.to,"[ตัส [ERROR] SCRIPT BREAKDOWNED]\n" + me.statusMessage)
                elif text.lower() == '!รูป':
                    me = cl.getContact(clMID)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif text.lower() == '!วีดิโอ':
                    me = cl.getContact(clMID)
                    cl.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus + "/vp")
                elif text.lower() == '!ปก':
                    me = cl.getContact(clMID)
                    cover = cl.getProfileCoverURL(clMID)    
                    cl.sendImageWithURL(msg.to, cover)
                elif msg.text.lower().startswith("!ขโมยคท. "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            mi_d = contact.mid
                            cl.sendContact(msg.to, mi_d)
                elif msg.text.lower().startswith("!ขโมยไอดี "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "[ Mid User ]"
                        for ls in lists:
                            ret_ += "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif msg.text.lower().startswith("!ขโมยชื่อ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ [ERROR] SCRIPT BREAKDOWNED ]\n" + contact.displayName)
                elif msg.text.lower().startswith("!ขโมยตัส "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            contact = cl.getContact(ls)
                            cl.sendMessage(msg.to, "[ [ERROR] SCRIPT BREAKDOWNED]\n{}" + contact.statusMessage)
                elif msg.text.lower().startswith("!ขโมยรูป "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("!ขโมยวีดิโอ "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        for ls in lists:
                            path = "http://dl.profile.line.naver.jp/" + cl.getContact(ls).pictureStatus + "/vp"
                            cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("!ขโมยปก "):
                        if 'MENTION' in msg.contentMetadata.keys()!= None:
                            names = re.findall(r'@(\w+)', text)
                            mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                            mentionees = mention['MENTIONEES']
                            lists = []
                            for mention in mentionees:
                                if mention["M"] not in lists:
                                    lists.append(mention["M"])
                            for ls in lists:
                                path = cl.getProfileCoverURL(ls)
                                cl.sendImageWithURL(msg.to, str(path))
                elif msg.text.lower().startswith("!ลอกคท. "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        for mention in mentionees:
                            contact = mention["M"]
                            break
                        try:
                            cl.cloneContactProfile(contact)
                            cl.sendMessage(msg.to, "ลอกสำเร็จ")
                        except:
                            cl.sendMessage(msg.to, "ไม่สำเร็จ")
                            
                elif text.lower() == '!คืนร่าง':
                    try:
                        clProfile.displayName = str(myProfile["displayName"])
                        clProfile.statusMessage = str(myProfile["statusMessage"])
                        clProfile.pictureStatus = str(myProfile["pictureStatus"])
                        cl.updateProfileAttribute(8, clProfile.pictureStatus)
                        cl.updateProfile(clProfile)
                        cl.sendMessage(msg.to, "สำเร็จ")
                    except:
                        cl.sendMessage(msg.to, "ไม่สำเร็จ")
                        
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
                elif msg.text.lower().startswith("mimicadd "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            settings["mimic"]["target"][target] = True
                            cl.sendMessage(msg.to,"Target ditambahkan!")
                            break
                        except:
                            cl.sendMessage(msg.to,"Added Target Fail !")
                            break
                elif msg.text.lower().startswith("mimicdel "):
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del settings["mimic"]["target"][target]
                            cl.sendMessage(msg.to,"Target dihapuskan!")
                            break
                        except:
                            cl.sendMessage(msg.to,"Deleted Target Fail !")
                            break
                elif text.lower() == 'mimiclist':
                    if settings["mimic"]["target"] == {}:
                        cl.sendMessage(msg.to,"Tidak Ada Target")
                    else:
                        mc = "╔══[ Mimic List ]"
                        for mi_d in settings["mimic"]["target"]:
                            mc += "\n╠ "+cl.getContact(mi_d).displayName
                        cl.sendMessage(msg.to,mc + "\n╚══[ Finish ]")
                    
                elif "mimic" in msg.text.lower():
                    sep = text.split(" ")
                    mic = text.replace(sep[0] + " ","")
                    if mic == "on":
                        if settings["mimic"]["status"] == False:
                            settings["mimic"]["status"] = True
                            cl.sendMessage(msg.to,"Reply Message on")
                    elif mic == "off":
                        if settings["mimic"]["status"] == True:
                            settings["mimic"]["status"] = False
                            cl.sendMessage(msg.to,"Reply Message off")
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
                elif text.lower() == '!คนสร้างกลุ่ม':
                    group = cl.getGroup(to)
                    GS = group.creator.mid
                    cl.sendContact(to, GS)
                elif text.lower() == '!ไอดีกลุ่ม':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[ID Group : ]\n" + gid.id)
                elif text.lower() == '!รูปกลุ่ม':
                    group = cl.getGroup(to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(to, path)
                elif text.lower() == '!ชื่อกลุ่ม':
                    gid = cl.getGroup(to)
                    cl.sendMessage(to, "[ชื่อ : ]\n" + gid.name)
                elif text.lower() == '!ตั๋ว':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ลิงค์เชิญ ]\nhttps://cl.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "เปิดลิงค์ {}openqr".format(str(settings["keyCommand"])))
                elif text.lower() == '!เปิดลิงค์':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            cl.sendMessage(to, "เปิดอยู่แล้ว")
                        else:
                            group.preventedJoinByTicket = False
                            cl.updateGroup(group)
                            cl.sendMessage(to, "เปิดเรียบร้อย")
                elif text.lower() == '!ปิดลิงค์':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == True:
                            cl.sendMessage(to, "ปิดอยู่แล้ว")
                        else:
                            group.preventedJoinByTicket = True
                            cl.updateGroup(group)
                            cl.sendMessage(to, "ปิดละ")
                elif text.lower() == '!เกี่ยวกับกลุ่ม':
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "ตายห่าไปละ"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "ปิดอยู่"
                        gTicket = "ปิดอยู่"
                    else:
                        gQr = "Open"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    ret_ = "╔══[[ERROR] SCRIPT BREAKDOWNED ]"
                    ret_ += "\n╠ ชื่อกลุ่ม : {}".format(str(group.name))
                    ret_ += "\n╠ ไอดีกลุ่ม : {}".format(group.id)
                    ret_ += "\n╠ คนสร้าง : {}".format(str(gCreator))
                    ret_ += "\n╠ สมาชิก : {}".format(str(len(group.members)))
                    ret_ += "\n╠ ค้างเชิญ : {}".format(gPending)
                    ret_ += "\n╠ Qr : {}".format(gQr)
                    ret_ += "\n╠ ตั๋ว : {}".format(gTicket)
                    ret_ += "\n╚══[ Finish ]"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                elif text.lower() == '!สมาชิกกลุ่ม':
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        ret_ = "╔══[ [ERROR] SCRIPT BREAKDOWNED ]"
                        no = 0 + 1
                        for mem in group.members:
                            ret_ += "\n╠ {}. {}".format(str(no), str(mem.displayName))
                            no += 1
                        ret_ += "\n╚══[ Total {} ]".format(str(len(group.members)))
                        cl.sendMessage(to, str(ret_))
                elif text.lower() == 'รายชื่อกลุ่ม':
                        groups = cl.groups
                        ret_ = "╔══[ Group List ]"
                        no = 0 + 1
                        for gid in groups:
                            group = cl.getGroup(gid)
                            ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                            no += 1
                        ret_ += "\n╚══[  {} กลุ่ม ]".format(str(len(groups)))
                        cl.sendMessage(to, str(ret_))
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#          
                elif text.lower() == '!แทค':
                    group = cl.getGroup(msg.to)
                    nama = [contact.mid for contact in group.members]
                    k = len(nama)//100
                    for a in range(k+1):
                        txt = u''
                        s=0
                        b=[]
                        for i in group.members[a*100 : (a+1)*100]:
                            b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                            s += 7
                            txt += u'@Alin \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                        cl.sendMessage(to, "Total {} Mention".format(str(len(nama))))          
                elif text.lower() == 'ปักหมุด':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hr + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('read.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            cl.sendMessage(msg.to, "Set reading point:\n" + readTime)
                            
                elif text.lower() == 'ดึงหมุด':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hr + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        cl.sendMessage(msg.to,"Lurking already off")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                              pass
                        cl.sendMessage(msg.to, "Delete reading point:\n" + readTime)
    
                elif text.lower() == 'รีหมุด':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hr + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nเวลา : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            del read["readPoint"][msg.to]
                            del read["readMember"][msg.to]
                            del read["readTime"][msg.to]
                        except:
                            pass
                        cl.sendMessage(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        cl.sendMessage(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif text.lower() == 'อ่าน':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hr + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if receiver in read['readPoint']:
                        if read["ROM"][receiver].items() == []:
                            cl.sendMessage(receiver,"[ Reader ]:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][receiver].items():
                                chiya.append(rom[1])
                            cmem = cl.getContacts(chiya) 
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = '[ Reader ]:\n'
                        for x in range(len(cmem)):
                            xname = str(cmem[x].displayName)
                            pesan = ''
                            pesan2 = pesan+"@c\n"
                            xlen = str(len(zxc)+len(xpesan))
                            xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                            zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                            zx2.append(zx)
                            zxc += pesan2
                        text = xpesan+ zxc + "\n[ Lurking time ]: \n" + readTime
                        try:
                            cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                        except Exception as error:
                            print (error)
                        pass
                    else:
                        cl.sendMessage(receiver,"Lurking has not been set.")
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#
                elif msg.text.lower().startswith("say-af "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'af'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
        
                elif msg.text.lower().startswith("say-sq "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sq'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ar "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ar'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-bn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'bn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ca "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ca'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-cn "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-cn'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-tw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-tw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-zh-yue "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'zh-yue'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cs "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cs'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-da "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'da'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-nl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'nl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-au "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-au'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-en-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'en-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-eo "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'eo'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-fr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'fr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-de "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'de'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-el "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'el'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-hu "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'hu'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-is "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'is'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-id "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'id'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-it "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'it'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ja "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ja'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-km "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'km'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ko "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ko'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-la "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'la'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-lv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'lv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-mk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'mk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-no "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'no'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pl "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pl'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-pt "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'pt'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-do "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ro'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ru "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ru'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-si "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'si'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-es "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-es'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-es-us "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'es-us'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sw "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sw'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-sv "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'sv'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-ta "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'ta'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-th "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'th'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-tr "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'tr'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-uk "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'uk'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-vi "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'vi'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
                    
                elif msg.text.lower().startswith("say-cy "):
                    sep = text.split(" ")
                    say = text.replace(sep[0] + " ","")
                    lang = 'cy'
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to,"hasil.mp3")
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========# 
                elif msg.text.lower().startswith("tr-af "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='af')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sq "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sq')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-am "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='am')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ar "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ar')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hy')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-az "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='az')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-eu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='eu')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-be "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='be')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bn')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bs')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-bg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='bg')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ca "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ca')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ceb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ceb')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ny "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ny')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-cn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-cn')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zh-tw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zh-tw')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-co "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='co')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hr')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cs "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cs')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-da "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='da')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-nl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='nl')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-en "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='en')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-et "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='et')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fi')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fr')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fy')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gl')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ka "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ka')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-de "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='de')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-el "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='el')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gu')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ht "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ht')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ha "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ha')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-haw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='haw')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-iw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='iw')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hi')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hmn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hmn')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-hu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='hu')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-is "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='is')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ig "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ig')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-id "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='id')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ga "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ga')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-it "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='it')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ja "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ja')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-jw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='jw')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-kn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='kn')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ki "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ki')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-km "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='km')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ko "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ko')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ku "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ku')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ky "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ky')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lo')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-la "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='la')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lv')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lt')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-lb "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='lb')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mk')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mg')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ms "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ms')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ml "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ml')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mt')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mi')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mr')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-mn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='mn')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-my "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='my')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ne "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ne')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-no "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='no')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ps "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ps')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fa')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pl')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pt "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pt')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-pa "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='pa')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ro "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ro')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ru "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ru')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sm "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sm')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-gd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='gd')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sr')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-st "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='st')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sn "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sn')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sd "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sd')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-si "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='si')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sk')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sl "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sl')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-so "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='so')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-es "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='es')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-su "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='su')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sw "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sw')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-sv "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='sv')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tg "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tg')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ta "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ta')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-te "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='te')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-th "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='th')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-tr "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='tr')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uk "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uk')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-ur "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='ur')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-uz "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='uz')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-vi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='vi')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-cy "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='cy')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-xh "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='xh')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yi "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yi')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-yo "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='yo')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-zu "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='zu')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-fil "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='fil')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
                elif msg.text.lower().startswith("tr-he "):
                    sep = text.split(" ")
                    isi = text.replace(sep[0] + " ","")
                    translator = Translator()
                    hasil = translator.translate(isi, dest='he')
                    A = hasil.text
                    cl.sendMessage(msg.to, A)
#﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏﹏=========#   
                elif text.lower() == 'kalender':
                    tz = pytz.timezone("Asia/Makassar")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hr + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    cl.sendMessage(msg.to, readTime)                 
                elif "screenshotwebsite" in msg.text.lower():
                    sep = text.split(" ")
                    query = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                        data = r.text
                        data = json.loads(data)
                        cl.sendImageWithURL(to, data["result"])
                elif "checkdate" in msg.text.lower():
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    ret_ = "╔══[ D A T E ]"
                    ret_ += "\n╠ Date Of Birth : {}".format(str(data["data"]["lahir"]))
                    ret_ += "\n╠ Age : {}".format(str(data["data"]["usia"]))
                    ret_ += "\n╠ Birthday : {}".format(str(data["data"]["ultah"]))
                    ret_ += "\n╠ Zodiak : {}".format(str(data["data"]["zodiak"]))
                    ret_ += "\n╚══[ Success ]"
                    cl.sendMessage(to, str(ret_))
                elif "instagraminfo" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            cl.sendImageWithURL(to, str(path))
                            cl.sendMessage(to, str(ret_))
                        except:
                            cl.sendMessage(to, "Pengguna tidak ditemukan")
                elif "instagrampost" in msg.text.lower():
                    separate = msg.text.split(" ")
                    user = msg.text.replace(separate[0] + " ","")
                    profile = "https://www.instagram.com/" + user
                    with requests.session() as x:
                        x.headers['user-agent'] = 'Mozilla/5.0'
                        end_cursor = ''
                        for count in range(1, 999):
                            print('PAGE: ', count)
                            r = x.get(profile, params={'max_id': end_cursor})
                        
                            data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                            j    = json.loads(data)
                        
                            for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                                if node['is_video']:
                                    page = 'https://www.instagram.com/p/' + node['code']
                                    r = x.get(page)
                                    url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                    print(url)
                                    cl.sendVideoWithURL(msg.to,url)
                                else:
                                    print (node['display_src'])
                                    cl.sendImageWithURL(msg.to,node['display_src'])
                            end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                elif ".หา" in msg.text.lower():
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                        data = r.text
                        data = json.loads(data)
                        if data["result"] != []:
                            items = data["result"]
                            path = random.choice(items)
                            a = items.index(path)
                            b = len(items)
                            cl.sendImageWithURL(to, str(path))
                elif ".ยูทูบ" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        cl.sendMessage(to, str(ret_))
                elif "searchmusic" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                ret_ = "╔══[ Music ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ reading Audio ]"
                                cl.sendMessage(to, str(ret_))
                                cl.sendAudioWithURL(to, song[3])
                        except:
                            cl.sendMessage(to, "Musik tidak ditemukan")
                elif "searchlyric" in msg.text.lower():
                    sep = text.split(" ")
                    search = text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.parse.urlencode(params))
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
                                ret_ += "\n╠ Link : {}".format(str(song[4]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                cl.sendMessage(to, str(ret_))
                        except:
                            cl.sendMessage(to, "Lirik tidak ditemukan")
                elif msg.contentType == 7:
                   if settings["checkSticker"] == True:
                      stk_id = msg.contentMetadata['STkiD']
                      stk_ver = msg.contentMetadata['STKVER']
                      pkg_id = msg.contentMetadata['STKPKGID']
                      ret_ = "╔══[ Sticker Info ]"
                      ret_ += "\n╠ STICKER ID : {}".format(stk_id)
                      ret_ += "\n╠ STICKER PACKAGES ID : {}".format(pkg_id)
                      ret_ += "\n╠ STICKER VERSION : {}".format(stk_ver)
                      ret_ += "\n╠ STICKER URL : line://shop/detail/{}".format(pkg_id)
                      ret_ += "\n╚══[ Finish ]"
                      cl.sendMessage(to, str(ret_))

        #    elif msg.contentType == 13:
        #        cl.sendMessage(msg.to, "บัญชีนี้ไม่ได้อยู่ในรายชื่อบัญชีดำ(｀・ω・´)")