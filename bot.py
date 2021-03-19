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
        if ' ' in message.text:
            marks = message.text.split(' ')
        elif '.' in message.text:
            marks = message.text.split('.')
        elif ',' in message.text:
            marks = message.text.split(',')
        else:
            pass
        try:
            for i in range(len(marks)):
                marks[i] = int(marks[i])
            ans = ('Средний балл равен - ' + str(round((sum(marks) / len(marks)),4)))
            bot.send_message(message.from_user.id, ans )
            print ('[done] -',str(ans), message.from_user.first_name)
        except:
            bot.send_message(message.from_user.id, 'Попробуйте ещё раз' )
bot.polling()
