from core import bot
import os


def cmd_start():
    @bot.message_handler(commands=['start'])
    def command_start(message):
        os.path.join('/home/genemator/')
        bot.send_message(message.from_user.id, '<b>You can start your session</b>', parse_mode='HTML')
        pass
    pass
