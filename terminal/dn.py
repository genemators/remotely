import os
import zipfile
import requests
from core import bot


def _dn(commands, message):
    global reply
    try:
        file = " ".join(commands[1:])
        if os.path.isfile(file) is True:
            caption = f"The file {file} you requested to send you..."
            document = open(file, "rb")
            bot.send_document(message.from_user.id, document, caption=caption)
            reply = None
        elif os.path.isdir(file):
            archive = f"{file}.zip"
            caption = f"The archived directory {archive}!"
            bot.send_message(message.from_user.id, "<b>Please, wait a minute. I'm archiving directory...</b>",
                             parse_mode='HTML')
            zf = zipfile.ZipFile(archive, "w")
            for dirname, subdirs, files in os.walk(file):
                zf.write(dirname)
                for filename in files:
                    zf.write(os.path.join(dirname, filename))
            document = open(archive, "rb")
            bot.send_document(message.from_user.id, document, caption=caption)
            os.remove(archive)
            reply = None
            pass
        else:
            reply = "Invalid file type!"
            pass
    except FileNotFoundError:
        reply = "The you want to get doesn't exists here!"
        pass
    pass

    return reply