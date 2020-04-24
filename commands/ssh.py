from config import *
from core import bot
from pyngrok import ngrok


def cmd_ssh():
    @bot.message_handler(commands=['ssh'])
    def command_ssh(message):
        if message.from_user.id in CREATOR or message.from_user.username in PRE_ADMINS:
            ssh_url = ngrok.connect(22, "tcp")
            port = ssh_url[21:]
            reply = f"<b>Use this command to ssh:</b> \n" \
                    f"<code>ssh genemator@0.tcp.ngrok.io -p{port}</code>"

            bot.reply_to(message, reply, parse_mode='HTMl')
            pass
        else:
            reply = "<b>Admin permissions required to execute this code!</b>"
            bot.reply_to(message, reply, parse_mode='HTML')
            pass
        pass
    pass
