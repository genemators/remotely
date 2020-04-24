import os
import time
import psutil

from config import *
from core import bot


def cmd_stats():
    @bot.message_handler(commands=['stats'])
    def command_stats(message):
        if message.from_user.id in CREATOR or message.from_user.username in PRE_ADMINS:
            # Time
            year, month, day = time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday
            now = f"{day}.{month}.{year}"

            # CPU
            cpu_usage_percent = psutil.cpu_percent()
            cpu_count = psutil.cpu_count()

            # RAM
            # VM
            virtual_rm_usage = psutil.virtual_memory().used >> 30
            total_virtual_rm, vrm_percent = psutil.virtual_memory().total >> 30, psutil.virtual_memory().percent
            # SWAP
            swap_rm_usage = psutil.swap_memory().used >> 30
            total_swap_rm, swrm_percent = psutil.swap_memory().total >> 30, psutil.swap_memory().percent

            # USAGE
            usage = psutil.Process(os.getpid()).memory_info()[0] >> 20

            reply = "<b>PC USAGE:</b> \n" \
                    "\n" \
                    "<u>CPU MANAGEMENT:</u> \n" \
                    f"<b>COUNT:</b> <code>{cpu_count}</code> \n" \
                    f"<b>USAGE:</b> <code>{cpu_usage_percent}%</code> \n" \
                    "\n" \
                    "<u>RAM MANAGEMENT:</u> \n" \
                    f"<b>VM:</b> <code>{virtual_rm_usage}GB | {vrm_percent}%</code> \n" \
                    f"<b>TOTAL:</b> <code>{total_virtual_rm}GB</code> \n" \
                    f"<b>SWAP:</b> <code>{swap_rm_usage}GB | {swrm_percent}%</code> \n" \
                    f"<b>TOTAL:</b> <code>{total_swap_rm}GB</code> \n" \
                    "\n" \
                    "<u>MISC:</u> \n" \
                    f"<b>DATE:</b> <code>{now}</code> \n" \
                    f"<b>USING:</b> <code>{usage}MB</code> \n" \
                    f""
            bot.send_message(message.from_user.id, reply, parse_mode='HTML')
        else:
            reply = "WHO ARE YOU TO GET INFORMATION ABOUT OWNER'S MACHINE?"
            bot.send_message(message.from_user.id, reply, parse_mode='HTMl')
