import os
import sys
import logging

from config import *
from core import bot


def cmd_re():
    @bot.message_handler(commands=['re'])
    def command_re(message):
        if message.from_user.id in CREATOR or message.from_user.username in PRE_ADMINS:
            try:
                bot.send_message(message.from_user.id, "Restarting")
                os.execl(sys.executable, sys.executable, * sys.argv)
                pass
            except Exception as e:
                logging.error(e)
                pass
            pass
        else:
            bot.send_message(message.from_user.id, "You are not admin of the bot to restart it!")

        python = sys.executable
        os.execl(python, python, *sys.argv)
    pass