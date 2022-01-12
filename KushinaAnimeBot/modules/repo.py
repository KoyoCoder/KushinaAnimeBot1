from KushinaAnimeBot import dispatcher

from telegram import ParseMode, Update
from telegram.ext import CommandHandler, CallbackContext
from telegram.ext.dispatcher import  run_async

GIT_PIC = "https://telegra.ph/file/a631d98805faa407daccb.jpg"

GIT_TEXT = """
KushinaAnimeRobot By @StarkBug

*Contributors/Credits*

> [StarkBug](https://github.com/StarkBug)
> [Nautilus](https://github.com/sudo-nautilus)
> [Kaneki](https://github.com/KanekiKen44)
> [Paul-Larsen](https://github.com/PaulSonofLars)
> [TheHamkerCat](https://github.com/TheHamkerCat)


[Repository](https://github.com/StarkBug/KushinaAnimeBot)
[Support](https://telegram.dog/StarkBugBotsChat)
[Docs](https://telegra.ph/file/a631d98805faa407daccb.jpg)

"""

@run_async
def repo(update: Update, context: CallbackContext):
    update.effective_message.reply_photo(
        GIT_PIC,
        caption = GIT_TEXT,
        parse_mode=ParseMode.MARKDOWN
        )

REPO_HANDLER = CommandHandler("repo", repo)

dispatcher.add_handler(REPO_HANDLER)
