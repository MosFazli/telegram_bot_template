# Add libraries to project
from flask import Flask, request
from datetime import datetime, timedelta
import requests

app = Flask(__name__)

# Your Telegram token should replace YOUR_BOT_TOKEN
# for Example token = '5440108238:AAEDYgsTwEnGjii0AkBlaXq57gGiN5QwfFE'
token = 'YOUR_BOT_TOKEN'


def welcome_msg(item):
    global token

    # This line using for convert time of server to your desired location
    # in this case location is Tehran with add 4 hours and 30 miuntes +(04:30)
    # You can also access the day of the week, hour and minute using the following variables
    time_tehran = datetime.now() + timedelta(hours=4, minutes=30)
    day = time_tehran.weekday()
    hour = time_tehran.hour
    minute = time_tehran.minute

    # This flag using for Text expressions that are not defined in bots
    flagElse = True

    # This function using for get text or not text with condition if
    if 'text' in item:

        # The first command we can consider is the bot start command, which is defined as follows
        if item["text"].lower() == "/start":
            flagElse = False
            msg = 'Hello, Welcome to the Bot'
            chat_id = item["chat"]["id"]
            welcome_msg = '''{}'''.format(msg)
            to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token,
                                                                                                            chat_id,
                                                                                                            welcome_msg)
            resp = requests.get(to_url)

        # You can find the command guide in this section
        if item["text"].lower() == "/help" or item["text"].lower() == "help":
            flagElse = False
            msg = 'You can find the command guide in this section'
            chat_id = item["chat"]["id"]
            help_mgs = '''{}'''.format(msg)
            to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token,
                                                                                                            chat_id,
                                                                                                            help_mgs)
            resp = requests.get(to_url)

        # Command example
        # You can put the order you want in this section
        if item["text"].lower() == "Command 1":
            flagElse = False
            msg = 'You Enter Command 1 !'
            chat_id = item["chat"]["id"]
            command = '''{}'''.format(msg)
            to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token,
                                                                                                            chat_id,
                                                                                                            command)
            resp = requests.get(to_url)

        # If imput command not setted, this function is executed
        else:
            if flagElse == True:
                msg = 'Your Text command is not setted by Admin, Please try again !'
                chat_id = item["chat"]["id"]
                welcome_msg = '''{}'''.format(msg)
                to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token,
                                                                                                                chat_id,
                                                                                                                welcome_msg)
                resp = requests.get(to_url)

    # if the input command is not text, this function is executed
    # you can use this function for message client if them send GIF, image, video and etc
    else:
        chat_id = item["chat"]["id"]
        msg = 'The command format is not supported'
        welcome_msg = '''{}'''.format(msg)
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, chat_id,
                                                                                                        welcome_msg)
        resp = requests.get(to_url)

# This is route of bot thah send message
# Don't remove it !!!!
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        data = data["message"]
        welcome_msg(data)
        return {'statusCode': 200, 'body': 'Success', 'data': data}
    else:
        return {'statusCode': 200, 'body': 'Success'}
