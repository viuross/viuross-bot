import telebot
token="8364020069:AAGPYjtxco4epR5XxjHbr8ztdifwjXJxwkI"
gery=telebot.TeleBot(token)
@gery.message_handler(commands=["start"])
def start_bot(message):
    
    send_msg = gery.send_message(message.chat.id, "welocme has viuross ✨, ready /V?")
    gery.pin_chat_message(message.chat.id, send_msg.message_id)
@gery.message_handler(commands=["v"])
def num(message):
    print(f"{message.from_user.first_name}هناك مستخدم جديد")
    wlecome_text=" اهلا بيك ف متجر viuross👑"
    num1=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,)
    itm1=telebot.types.KeyboardButton("للتواصل واتساب ")
    itm2=telebot.types.KeyboardButton("للاستفسار عن المقدمات")
    item3=telebot.types.KeyboardButton("للمغادرة ")
    num1.add(itm1,itm2,item3)
    gery.send_message(message.chat.id,"hello✨",reply_markup=num1)
 
 
 
@gery.message_handler(func=lambda message:True)
def message_1(message):
     if message.text=="للتواصل واتساب":
         gery.reply_to(message,"https://wa.me/201019266979")
     elif message.text=="للاستفسار عن المقدمات":
          ahmed="نحن نقدم لك الممزات لمشاريع بايثون😍"
          gery.reply_to(message, ahmed)
          gery.send_photo(message.chat.id, "https://4kwallpapers.com/images/wallpapers/python-programming-2048x2048-16102.jpg", caption="👑 viuross")
     elif message.text=="للمغادرة":
         gery.reply_to(message,"goodpaye..!")
         
         
         
@gery.message_handler(func=lambda message:message.text==True)
def message(massege):
    gery.send_massege(massege.chat.id,"يمكنك فقط الاختيار من الزراير👑")
    
    
print("don...!") 
gery.infinity_polling()