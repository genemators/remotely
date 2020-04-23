# The main core bot variable
from core import bot
from terminal.handler import terminal


# Initialization of terminal
def init():
    @bot.message_handler(func=lambda message: True)
    def command(message):
        output = terminal(message.text.split(), message)
        if output == '':
            reply = f"<pre>Just emptiness</pre>"
            bot.reply_to(message, reply, parse_mode='HTML')
        if output is None:
            pass
        else:
            reply = f"<pre>{output}</pre>"
            bot.reply_to(message, reply, parse_mode='HTML')
        pass
