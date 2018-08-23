import time
from sys import argv as arguments
from telepot import glance, Bot as Telepot
from rivescript import RiveScript
from dotenv import load_dotenv
from os import getenv


def handle(msg):
    """
    TODO
    """
    content_type, _chat_type, chat_id = glance(msg)

    new_member = (True if content_type == 'new_chat_member' else False)
    msg_text = ('new member' if 'text' not in msg else msg['text'])

    if content_type in ['text', 'new_chat_member']:
        check_msg(chat_id, msg_text, msg['message_id'], new_member)


def check_msg(chat_id, msg, user_id, new_member=False):
    """
    TODO
    """
    message = msg.lower().split()

    if new_member or (WHEN_MENTIONED and BOTNAME in message):
        res = BOT.reply("localuser", msg)
        if(res != "[ERR: No Reply Matched]"):
            TELEGRAM.sendMessage(chat_id,
                                 res,
                                 parse_mode='Markdown',
                                 reply_to_message_id=user_id)


load_dotenv(verbose=True)
TOKEN = arguments[1]
TELEGRAM = Telepot(TOKEN)

BOTNAME = getenv("BOTNAME")
WHEN_MENTIONED = getenv("MENTION")

TELEGRAM.message_loop(handle)
print('Listening ...')

BOT = RiveScript()
BOT.load_directory("./brain")
BOT.sort_replies()

# Keep the program running.
while 1:
    time.sleep(2)
