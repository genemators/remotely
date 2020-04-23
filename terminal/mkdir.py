import os


def _mkdir(commands):
    try:
        filename = str(" ".join(commands[1:]))
        os.mkdir(filename)
        reply = f"The folder {filename} has been created"
        pass
    except FileExistsError:
        reply = "The folder already exists"
        pass
    pass

    return reply