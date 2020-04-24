import re
import config
from core import bot


def cmd_la():
    @bot.message_handler(commands=['la'])
    def command_la(message):
        if message.from_user.id in config.CREATOR:
            re_admins = str("\n".join(config.PRE_ADMINS))
            bot.send_message(message.from_user.id, '<b>PRE ADMINS:</b> \n' + re_admins, parse_mode='HTML')
            pass
        else:
            bot.send_message(message.from_user.id, "<b>This commands requires superuser privileges!</b>", parse_mode='HTML')
            pass
        pass
    pass
