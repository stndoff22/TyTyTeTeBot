import telebot

bot = telebot.TeleBot("6642385128:AAHVn_3y9HhEOG8kRxw6yzN1ynI1ghGqpZ4")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id,"Привет я TyTy_TeTebot.Хощеш TyTe прикол")
    if message.text == "да":

            bot.send_message(message.from_user.id, "cccр.в зони 3 сталкира     ")
    if message.text == "ещё":
            bot.send_message(message.from_user.id, "абломииииииииииись")
bot.polling(none_stop=True, interval=0)
