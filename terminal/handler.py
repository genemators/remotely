# Don't forget about admin configs
import config

# Importing all terminal commands
# Made by myself
from terminal.cd import _cd
from terminal.clear import _clear
from terminal.mkdir import _mkdir
from terminal.rm import _rm
from terminal.cat import _cat
from terminal.echo import _echo
from terminal.exit import _exit
from terminal.dn import _dn

# This is shell connector
from terminal.shell import *


def terminal(commands, message):
    if message.chat.type == "private":
        if message.from_user.id in config.CREATOR or message.from_user.username in config.PRE_ADMINS:
            if "cd" in commands:
                return _cd(commands)
            elif "clear" in commands:
                return _clear(commands)
            elif "mkdir" in commands:
                return _mkdir(commands)
            elif "rm" in commands:
                return _rm(commands)
            elif "cat" in commands:
                return _cat(commands)
            elif "echo" in commands:
                return _echo(commands)
            elif "exit" in commands:
                return _exit(commands)
            elif "dn" in commands:
                return _dn(commands, message)
            else:
                return shell(commands)
            pass
        else:
            reply = "Bruh, you need admin superuser privileges to access terminal commands!"
            return reply
        pass
    elif message.chat.type == "group":
        reply = "Bruh, I won't accept shell commands from groups!"
        return reply
        pass
    elif message.chat.type == "supergroup":
        reply = "Bruh, I won't accept shell commands from supergroup!"
        return reply
        pass
    elif message.chat.type == "channel":
        reply = "Bruh, I won't accept shell commands from channels!"
        return reply
        pass
