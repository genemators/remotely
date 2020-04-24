import requests
import urllib.request
import itertools
import json

from config import *
from netifaces import interfaces, ifaddresses, AF_INET
from core import bot


def internalIP():
    links = filter(None, (ifaddresses(x).get(AF_INET) for x in interfaces()))
    links = itertools.chain(*links)
    ip_addresses = [x['addr'] for x in links]
    source_ip = ip_addresses
    result = str("\n".join(source_ip))
    return result
    pass


def externalIP():
    source_ip = []
    url = "http://localhost:4040/api/tunnels"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        for address in data['tunnels']:
            source_ip.append(address['public_url'][6:])
    except Exception as err:
        if LOGGING is True:
            print(err)
        else:
            pass
        pass
    source_ip.append(requests.get('https://api.ipify.org').text)
    result = str("\n".join(source_ip))
    return result
    pass


def cmd_ip():
    @bot.message_handler(commands=['ip'])
    def command_ip(message):
        if message.from_user.id in CREATOR or message.from_user.username in PRE_ADMINS:
            internal = str(internalIP())
            external = str(externalIP())

            reply = f"<b>IP Addresses:</b> \n\n" \
                    f"<code>Internal:</code> \n" \
                    f"{internal} \n\n" \
                    f"<code>External:</code> \n" \
                    f"{external} \n\n"
            bot.reply_to(message, reply, parse_mode='HTML')
            pass
        else:
            reply = "<b>Admin permissions required to execute this code!</b>"
            bot.reply_to(message, reply, parse_mode='HTML')

    pass
