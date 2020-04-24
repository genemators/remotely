from core import bot


def cmd_start():
    @bot.message_handler(commands=['start'])
    def command_start(message):
        reply = f"<b>Hello, {message.from_user.first_name}!</b> \n" \
                "<code>This bot helps you to set up remote environment \n" \
                "This might be risky, so please consider any damage \n" \
                "For further detail or help, type </code>/help<code>. Good Luck!</code>"
        bot.send_message(message.from_user.id, reply, parse_mode='HTML')
        pass
    pass
