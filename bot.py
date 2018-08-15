from sys import argv as arguments
import time
import telepot
from rivescript import RiveScript


def handle(msg):
    """
    TODO
    """
    content_type, _chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        check_msg(chat_id, msg['text'], msg['message_id'])


def check_msg(chat_id, msg, user_id):
    """
    TODO
    """
    message = msg.lower().split()
    res = BOT.reply("localuser", msg)

    if(res != "[ERR: No Reply Matched]"):
        TELEGRAM.sendMessage(
            chat_id, res, parse_mode='Markdown', reply_to_message_id=user_id)


TOKEN = arguments[1]

TELEGRAM = telepot.Bot(TOKEN)
TELEGRAM.message_loop(handle)
print('Listening ...')

BOT = RiveScript()
BOT.load_directory("./brain")
BOT.sort_replies()

# Keep the program running.
while 1:
    time.sleep(2)
