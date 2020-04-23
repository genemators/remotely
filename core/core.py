import telebot
import config

bot = telebot.TeleBot(config.TOKEN)


def launch():
    print("Bot has been started!")
    bot.polling(none_stop=True)
    pass