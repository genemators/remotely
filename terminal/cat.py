import os


def _cat(commands):
    try:
        filename = str(" ".join(commands[1:]))
        file = open(filename, 'r').read()
        reply = f"The file {filename}: \n\n" \
            f"{file}"
        pass
    except FileNotFoundError:
        reply = 'The file you tried to cat not found!'
        pass
    pass

    return reply