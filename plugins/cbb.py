from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b> My Name :</b> <a href='https://t.me/Files_Store9_Bot'>File Store Bot</a> \n<b>Language :</b> <a href='https://python.org'>Python 3</a> \n<b>Library :</b> <a href='https://pyrogram.org'>Pyrogram {__version__}</a> \n<b>Server :</b> <a href='https://koyeb.com'>koyeb</a> \n<b>Channel :</b> <a https://t.me/Hindi_Dub_Animes_Official'>Hindi Animes</a> \n<b>Developer :</b> <a href='tg://user?id={OWNER_ID}'>Night</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
