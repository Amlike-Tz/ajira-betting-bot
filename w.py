import sys
import os
import telebot
import urllib.request
import bs4 as bs
import time
import requests
import telebot
from telebot import types
from telebot import util
API_KEY = '1961681182:AAEsmCRAlL9hovXxVpuaW63xC98cDOGlfsc'
bot = telebot.TeleBot(API_KEY)


os.system("rm  rea.txt")
os.system("rm  aji.txt")
os.system("rm  time.txt")
os.system("rm  saba.txt")
os.system("rm  shinda.txt")
lenk = urllib.request.urlopen('https://tbet.co.tz/mchezo/mpira-wa-miguu/matokeo')

#salting
soup = bs.BeautifulSoup(lenk, 'lxml')

you9 = soup.find_all('li', class_='team-winner')
#you3 = soup.find_all('div', class_='TipReason__body')
for am in  you9:
    you9 = am.find(class_='team-winner')
    you9 = am.text
    leo = '\n\n Ameshinda: ' + you9.strip()
    file = open("shinda.txt", "a")
    file.write(leo)
    file.close()


shinda = open("shinda.txt", "rb").read()

splitted_text = util.split_string(shinda, 3000)

for shi in splitted_text:
     @bot.message_handler(commands=['matokeo', 'result', 'Matokeo',])
     def hi_sender(message):
          bot.send_message(message.chat.id, shi)


lin2 = urllib.request.urlopen('https://www.freesupertips.com/accumulator-tips/')
#salting
soup = bs.BeautifulSoup(lin2, 'lxml')
you2 = soup.find_all('div', class_='Exp Exp--arrow Leg__inner')
you3 = soup.find_all('div', class_='TipReason__body')

for am in  you2:
    you2 = am.find(class_='Leg__win"')
    you3 = am.find(class_='TipReason__body')
    you3 = am.text
    you2 = am.text
    you2 = you2.format()
    line = '\n mkeka: ' + you2 + '\n'
    file = open("rea.txt", "a")
    file.write(line.replace("Win", " Win  "))
    file.close()
   # print (lines)

lin2 = urllib.request.urlopen('https://www.freesupertips.com/accumulator-tips/')
#salting
soup = bs.BeautifulSoup(lin2, 'lxml')
you2 = soup.find_all('div', class_='Exp Exp--arrow Leg__inner')
you3 = soup.find_all('div', class_='TipReason__body')




for am in  you3:
    you2 = am.find(class_='Leg__win')
    you3 = am.find(class_='TipReason__body')
    you3 = am.text
    you2 = am.text
    you2 = you2.format()
    lines = '\n Kwasababu: ' + you3
    file = open("saba.txt", "a")
    file.write(lines)
    file.close()

last = open("rea.txt", "rb").read()

splitted_text = util.split_string(last, 3000)

for txt in splitted_text:
     @bot.message_handler(commands=['mkeka', 'mikeka', 'match',])
     def hi_sender(message):
          bot.send_message(message.chat.id, txt)

babu = open("saba.txt", "rb").read()

splitted_text = util.split_string(babu, 3000)

for text in splitted_text:
     @bot.message_handler(commands=['reason', 'sababu', 'Sababu',])
     def hi_sender(message):
          bot.send_message(message.chat.id, text)

for message in lines:
     @bot.message_handler(commands=['Hi', 'hello', 'Hellow', 'mambo', 'start', 'hi', 'Start'])
     def hi_sender(message):
          bot.send_message(message.chat.id, "Hi There🤪!! \nWelcome to AmlikeTz Ajira And Betting Bot✅.Nin niweze kukusaidia?? ama  KUWEZA kuona List of Commands Andika neno\n /help .Thankyou")

     @bot.message_handler(commands=['/help', 'help', 'help', 'HELP',])
     def hi_sender(message):
          bot.send_message(message.chat.id, "Am Ajira and Betting TippsBot. zifuatazo ni List Of commands amaa vitu ambavyo naweza Kukufanyia.\n\n  /help : how to use me\n\n  /mkeka : kuweza kuona mkeka wa bure\n\n  /sababu : Sababu ya kuchagua hizo team \n\n  /matokeo  or  /result  : kuangalia matokeo ya match hi ni kwa tim zilizoshinda tu!!  \n\n   /Online : kuangalia kama niko online\n\n   /ajira : Taarifa za ajira mpya \n\n   /trending : Habari zinazotrend Now.\n\n   /developer : kuongea na owner wa Ajira And Betting Bot\n\n  /next : kuona upcomming features za hii Bot.\n\n   ✅Ajira And Betting-Tips")

     @bot.message_handler(commands=['ajira', 'job', 'kazi', 'Ajira', 'Kazi',])
     def hi_sender(message):
          bot.send_message(message.chat.id, "Hi There🤪!! \nWelcome!! Ili kuweza kuona post za nafasi za kazi Ama kuweza kuona siku ilipostiwa Angalia Command Zifuatazo✅.\n \post :Kuona Nafasi za kazi.\n /show : Kuona Nafasi za kazi pia.\n /time : Kuona siku zilizotangwaza,\n Note; mda wa siku ilotangazwa umepangwa kulingana na mtiririko wa hizo list za kazi. \n  /help .: kuludi kwenye muongozo mkuu")

     @bot.message_handler(commands=['start'])
     def start(message):
          key = types.InlineKeyboardMarkup()
          cal = types.InlineKeyboardButton(text='Chat with Me Now', url='https://bit.ly/3E7QUZx')
          key.add(cal)
          bot.send_message(message.chat.id, text='AmlikeTz', reply_markup=key)
     
     @bot.message_handler(commands=['online', 'Online',])
     def hi_sender(message):
          bot.send_message(message.chat.id, "LMAO!!!🤪!! \n  Am online Dudee.✅.\n  click /help To see how to use me.")
     
     @bot.message_handler(commands=['Trending', 'trending',])
     def hi_sender(message):
          bot.send_message(message.chat.id, "Hmmm!!!  No trending story sir/miss !!!\n or go and search google!!!")
     
     @bot.message_handler(commands=['next', 'upcoming',])
     def hi_sender(message):
          bot.send_message(message.chat.id, "\n\n  Next added features of this bot will be more amazing than anoying please keep in touch so that to be first one to use that pretty cool feature buddy!")










#     @bot.message_handler(commands=['mkeka', 'mikeka', 'match',])
 #    def hi_sender(message):
  #       bot.send_message(message.chat.id, text)

  #        bot.send_message(message.chat.id, lines)
   #       print (you2)
#               "Opps!! Sijakuelewa Invalid command.Pleasee Try Again.🙏🙏"





link2 = urllib.request.urlopen('https://www.ajirayako.co.tz/')
#salting
soup = bs.BeautifulSoup(link2, 'lxml')
you2 = soup.find_all('h2', class_='post-title')
you3 = soup.find_all('span', class_='post-date published')


for am in you2:
    you2 = am.find(class_='post-title')
    you2 = am.a.text
   # print (you2)
    you2 = you2.format()
    line = '\n Nafasi Ya Kazi : ' +you2.strip()
    file = open("aji.txt", "a")
    file.write(line)
    file.close()
ajira = open("aji.txt", "rb").read()

splitt_text = util.split_string(ajira, 4000)

for texti in splitt_text:
     @bot.message_handler(commands=['show', 'onesha', 'post',])
     def hi_amo(message):
          bot.send_message(message.chat.id, texti)




for am in you3:
    you3 = am.find('span', class_='post-date published')
    you3 = am.text
   # print (you3)   
    you3 = you3.format()
    x = 0
    x += 1
    line = '\n Siku Iliotangazwa: ' +you3.strip()
    file = open("time.txt", "a")
    file.write(line)
    file.close()
    



tim = open("time.txt", "rb").read()

splitted_txt = util.split_string(tim, 3000)

for tax in splitted_txt:
     @bot.message_handler(commands=['tareh', 'mda', 'siku', 'time',])
     def hi_sender(message):
          bot.send_message(message.chat.id, tax)




while True:
   try:
     bot.polling()
   except Exception:
     time.sleep (10)
bot.polling(none_stop=False, interval=0, timeout=20)
