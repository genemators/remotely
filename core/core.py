import telebot
import config
import logging

logger = telebot.logger
bot = telebot.TeleBot(config.TOKEN)


def launch():
    if config.LOGGING is True:
        telebot.logger.setLevel(logging.DEBUG)
    else:
        pass
    bot.polling(none_stop=True)
    pass