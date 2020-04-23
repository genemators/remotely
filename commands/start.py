from core import bot


def cmd_start():
    @bot.message_handler(commands=['start'])
    def command_start(message):
        reply = "Use /help for instructions!\n" \
                f"Good luck, {message.from_user.first_name}..."
        bot.send_message(message.from_user.id, reply, parse_mode='HTML')
        pass
    pass
