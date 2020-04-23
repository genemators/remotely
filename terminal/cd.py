import os


def _cd(commands):
    try:
        os.path.join(os.getcwd())
        os.chdir(str(" ".join(commands[1:])))
        reply = str('Changing working directory to ' + os.getcwd())
        pass
    except FileNotFoundError:
        reply = str('The given path not found!')
        pass
    pass

    return reply


pass
