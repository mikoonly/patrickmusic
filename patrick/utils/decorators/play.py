from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import PLAYLIST_IMG_URL, MUST_JOIN, SUPPORT_GROUP, adminlist
from strings import get_string
from patrick import YouTube, app
from patrick.misc import SUDOERS
from patrick.utils.database import (get_cmode, get_lang,
                                       get_playmode, get_playtype,
                                       is_active_chat,
                                       is_commanddelete_on,
                                       is_served_private_chat)
from patrick.utils.database.memorydatabase import is_maintenance
from patrick.utils.inline.playlist import botplaylist_markup



def PlayWrapper(command):
    async def wrapper(client, message):
        language = await get_lang(message.chat.id)
        _ = get_string(language)
        if message.sender_chat:
            upl = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="ʜᴏᴡ ᴛᴏ ғɪx ?",
                            callback_data="AnonymousAdmin",
                        ),
                    ]
                ]
            )
            return await message.reply_text(
                _["general_3"], reply_markup=upl
            )
        if MUST_JOIN:
            try:
                await app.get_chat_member(MUST_JOIN, message.from_user.id)
            except UserNotParticipant:
                sub = await app.export_chat_invite_link(MUST_JOIN)
                kontol = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("📑 Gabung Dulu", url=sub)]
                    ]
                )
                return await message.reply_text(
                _["general_3"], reply_markup=upl
            )
        if MUST_JOIN:
            try:
                await app.get_chat_member(MUST_JOIN, message.from_user.id)
            except UserNotParticipant:
                sub = await app.export_chat_invite_link(MUST_JOIN)
                kontol = InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("join dulu🗿", url=sub)]
                    ]
                )
                return await message.reply_text(_["force_sub"].format(message.from_user.mention), reply_markup=kontol)
                

        if await is_maintenance() is False:
            if message.from_user.id not in SUDOERS:
                return await message.reply_text(
                    text=f"{app.mention} ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ, ᴠɪsɪᴛ <a href={SUPPORT_GROUP}>Support Group</a> for knowing the reason.",
                    disable_web_page_preview=True,
                )
