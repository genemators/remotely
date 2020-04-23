import re
import config
from core import bot


def cmd_add():
    # @bot.message_handler(regexp=r"/add (.+)")
    @bot.message_handler(commands=['add'])
    def command_add(message):
        text = message.text
        new_admin = re.findall(r"/add @(.+)", text)[0]
        if message.from_user.id in config.CREATOR:
            config.PRE_ADMINS.append(new_admin)
            bot.send_message(message.from_user.id, f'<b>Added</b> <a href="https://t.me/{new_admin}">{new_admin}</a> <b>to pre-admins!</b>', parse_mode='HTML')
            pass
        else:
            bot.send_message(message.from_user.id, "<b>This commands requires superuser privileges!</b>", parse_mode='HTML')
            pass
        pass
    pass
