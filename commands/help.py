from core import bot

reply = "<u>BSBA: MONSTER MACHINE V132.21 BUILD</u> \n" \
        "\n" \
        "<u>Built-in available bot commands:</u> \n" \
        "/start - <code>Start bot's session</code> \n" \
        "/help - <code>Show this message</code> \n" \
        "/ip - <code>Show available ip addresses</code> \n" \
        "/stats - <code>Current statuses of the bot</code> \n" \
        "/ssh - <code>Open a ssh tunnel for remote term</code> \n" \
        "/re - <code>reset all tunnels and restart bot</code> \n" \
        "/exit - <code>stop bot from working and reset everything</code> \n" \
        "\n" \
        "<u>There exists hand made inside shell based commands as:</u> \n" \
        "cd &lt path &gt - <code>Change working directory</code> \n" \
        "cat &lt file &gt - <code>Show file's contents</code> \n" \
        "dn &lt file|folder &gt - <code>Download content</code> \n" \
        "echo &lt string &gt - <code>Just send a string</code> \n" \
        "mkdir &lt string &gt - <code>Create a directory</code> \n" \
        "rm &lt file|folder &gt - <code>Delete content</code> \n" \
        "\n" \
        "<i>Any other exceptional shell command will be executed on this machine's shell!</i>"


def cmd_help():
    @bot.message_handler(commands=['help'])
    def command_help(message):
        bot.send_message(message.from_user.id, reply, parse_mode="HTML")
        pass

    pass
