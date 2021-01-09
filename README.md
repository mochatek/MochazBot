# MochazBot

Telegram Bot built using the [Telepot API](https://telepot.readthedocs.io/en/latest/) and Django Webhook.

See the bot in action: [MochazBot](https://telegram.me/mochaz_bot)

## Bot Commands
- [start]() - Start the Bot
- [/psc]() - Shows 20 PSC questions and Answers
- [/compile_lang_code]() - Programming language compiler. Languages supported as of now are: 
`[C, Cpp, Python3]`
- [ans_question]() - Answers the _question_
- [/fakenumber]() - Gives a fake mobile number, which you can use for registering in dumb sites.
- [/inbox_number_count]() - Shows the last _count_ messages received in the _number_

## Installation

Download and Install [Python](https://www.python.org/downloads/)

Use the package manager [pip](https://pip.pypa.io/en/stable/reference/pip_download/) to install the dependencies.

```bash
pip install -r requirements.txt
```

Goto [BotFather](https://telegram.me/BotFather) and type the command `/newbot` to create a new bot. Follow the steps until you get a username and token for your bot.

Copy the bot token and add it as an environment variable `TELEGRAM_TOKEN` or paste the token inside the function in `MochazBot/bot/views.py:line 18` (Use this only in development. Use the first method in production)

Add a WebHook to our web-application using: 
```
https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={URL_TO_OUR_WEBAPP}
```

## How to Run

To start our application, run the command:

```
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://github.com/mochatek/MochazBot/blob/master/LICENSE)
