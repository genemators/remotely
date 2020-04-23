import os


def _mkdir(commands):
    try:
        os.mkdir(str(commands[1:]))
        reply = f"The folder {commands[1:]} has been created"
        pass
    except FileExistsError:
        reply = "The folder already exists"
        pass
    pass

    return reply