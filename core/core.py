import telebot
import config
import logging

logger = telebot.logger
bot = telebot.TeleBot(config.TOKEN)


def launch():
    telebot.logger.setLevel(logging.DEBUG)
    bot.polling(none_stop=True)
    pass