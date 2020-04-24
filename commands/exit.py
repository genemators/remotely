import sys
import logging

from config import *
from core import bot


def cmd_exit():
    @bot.message_handler(commands=['exit'])
    def command_exit(message):
        if message.from_user.id in CREATOR or message.from_user.username in PRE_ADMINS:
            try:
                bot.send_message(message.from_user.id, "Terminating bot's session! Thank you...")
                exit(1)
                pass
            except Exception as e:
                logging.error(e)
                pass
            pass
        else:
            bot.send_message(message.from_user.id, "You're not admin of this bot to turn it off!")
    pass