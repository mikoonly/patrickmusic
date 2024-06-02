import asyncio

from patrick import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME, OWNER_USERNAME, SUPPORT_CHANNEL

@app.on_message(filters.command("alive", ["/", ".", "!"]))
async def kontolmasukmemek(client: Client, message: Message):
    await message.reply_video(
        video=f"https://telegra.ph/file/0711c7c7ecd3aba595219.mp4",
        caption=f"💖 Hei {message.from_user.mention}\n\n I am {MUSIC_BOT_NAME}\n\n✨ I am Fast and Powerful music player bot with some awesome features.\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="ᴏᴡɴᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "ᴄʟᴏsᴇ", callback_data="close"
                    )
                ],
            ]
        )
    )
