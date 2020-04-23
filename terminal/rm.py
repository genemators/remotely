import os
import shutil


def _rm(commands):
    try:
        file = commands[1:]
        reply = None
        if os.path.isfile(file) is True:
            os.remove(file)
        else:
            shutil.rmtree(file)
        reply = f"The file {file} has been deleted"
    except FileNotFoundError:
        reply = "The file you're trying to delete not found!"
        pass
    pass

    return reply
