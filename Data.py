from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hello {} IAM A BOT USED FOR GENERATING YOUR TELETHON AND PYROGRAM STRING SESSION MAINTAINED BY [DEVOURDEVILS](t.me/devourdevils) """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton(text="Home", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("Start Generating Session", callback_data="generate")],
        [InlineKeyboardButton("Maintaned By", url="https://t.me/devourdevils")],
        [
            InlineKeyboardButton("How to use me", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
      ],
        [InlineKeyboardButton("Other bot info", url="https://t.me/devourdevils")],
    ]


    # Help Message
    HELP = """
✨ **Available Commands** ✨
/about - About this bot
/help - How to use this bot
/start - Start Bot
/generate - Start Generating Session
/cancel - Cancel process
/restart - Restart process
"""

    # About Message
    ABOUT = """
**About This Bot** 
A telegram bot to retrieve pyrograms and telethon string sessions by @devourdevils
Group Support : [Gabung](https://t.me/septemberfilms)
Framework : [Pyrogram](docs.pyrogram.org)
Language : [Python](www.python.org)
Developer : @devourdevils
    """
