import os


def _cat(commands):
    try:
        filename = str(" ".join(commands[1:]))
        if os.path.isfile(filename) is True:
            file = open(filename, 'r').read()
            reply = f"The file {filename}: \n\n" \
                f"{file}"
            pass
        elif os.path.isdir(filename) is True:
            reply = "The command cat can't print directory"
        else:
            reply = "Invalid type of content!"
    except FileNotFoundError:
        reply = 'The file you tried to cat not found!'
        pass
    pass

    return reply