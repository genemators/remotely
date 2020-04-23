import os
import subprocess


def shell(commands):
    directory = os.getcwd()
    cmd_output = subprocess.Popen(commands,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT,
                                  shell=True, cwd=directory)
    stdout, stderr = cmd_output.communicate()
    reply = str(stdout).replace("\\n", "\n")[2:-1]
    return reply
