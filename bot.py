import telebot
import os

token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(token);

@bot.message_handler(func=lambda m: True)
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Просто введи свои оценки")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Просто введи свои оценки")
    else :
        marks = list(message.text.replace(" ","").replace(",","").replace(".",""))
        try:
            for i in range(len(marks)):
                marks[i] = int(marks[i])
            a = str(round((sum(marks) / len(marks)),4))
            ans = ('Средний балл равен:')
            bot.send_message(message.from_user.id, ans )
            print ('[done] -',str(ans), 'by', message.from_user.username)


        except:
            bot.send_message(message.from_user.id, 'Попробуйте ещё раз' )
        if True:
            image = Image.open("fol/images.jpg")
            font = ImageFont.truetype("Circe-ExtraLight.ttf", 200)
            drawer = ImageDraw.Draw(image)
            if len(a)==4: #oстаток 2
                drawer.text((480,520), a, font=font, fill='black')
            elif len(a) == 5: #oстаток 3 
                drawer.text((425,520), a, font=font, fill='black')
            elif len(a) == 6: #oстаток 4
                drawer.text((370,520), a, font=font, fill='black')
            elif len(a)==3: #oстаток 1
                drawer.text((520,520), a, font=font, fill='black')
            else: #oстаток 0
                drawer.text((590,520), a, font=font, fill='black')
            photo ='fol/new_img-'+'valde'+'_'+str(random.randint(0,6000))+'.jpg'
            image.save(photo)
            bot.send_photo(message.from_user.id, open(photo,'rb'))
bot.polling()
