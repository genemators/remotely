import re
import config
from core import bot


def cmd_add():
    # @bot.message_handler(regexp=r"/add (.+)")
    @bot.message_handler(commands=['add'])
    def command_add(message):
        text = message.text
        new_admin = re.findall(r"/add @(.+)", text)[0]
        config.PRE_ADMINS.append(new_admin)
        print(config.PRE_ADMINS)
        bot.send_message(message.from_user.id, 'Check', parse_mode='HTML')
        pass
    pass
