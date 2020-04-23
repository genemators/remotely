from core import bot

text = "<b>Available bot commands to use:</b> \n\n" \
    "/start - start command to start new session \n" \
    "/help - to show this message and get command list \n\n" \
    "<i>Write any shell command, it will be executed on " \
    "this machine's shell!</i>"


def cmd_help():
    @bot.message_handler(commands=['help'])
    def command_help(message):
        bot.send_message(message.from_user.id, text, parse_mode='HTML')
        pass
    pass