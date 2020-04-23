import os
import shutil


def _rm(commands):
    try:
        file = str(" ".join(commands[1:]))
        if os.path.isfile(file) is True:
            os.remove(file)
            reply = f"The file {file} has been deleted"
        elif os.path.isdir(file) is True:
            shutil.rmtree(file)
            reply = f"The folder {file} has been deleted"
        else:
            reply = f"Invalid type of file"
    except FileNotFoundError:
        reply = "The file you're trying to delete not found!"
        pass
    pass

    return reply
