#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# Bu fayl < https://github.com/TheAloneTeam/AloneMusic > layihəsinin bir hissəsidir,
# və "GNU v3.0 License Agreement" altında buraxılmışdır.
# Zəhmət olmasa baxın: < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# Bütün hüquqlar qorunur.

from pyrogram import filters
from pyrogram.types import Message
from unidecode import unidecode

from AloneMusic import app
from AloneMusic.misc import SUDOERS
from AloneMusic.utils.database import (get_active_chats,
                                       get_active_video_chats,
                                       remove_active_chat,
                                       remove_active_video_chat)


@app.on_message(filters.command(["ac"]) & SUDOERS)
async def active_vc(_, message: Message):
    achats = len(await get_active_chats())
    vchats = len(await get_active_video_chats())
    await message.reply_text(
        f"<b>» ᴀᴋᴛɪᴠ ᴢəɴɢʟəʀ:</b>\n\nꜱəꜱʟɪ: {achats}\nᴠɪᴅᴇᴏ: {vchats}"
    )


@app.on_message(filters.command(["activevc", "activevoice"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("» ᴀᴋᴛɪᴠ ꜱəꜱʟɪ ᴢəɴɢʟəʀɪɴ ꜱɪʏᴀʜıꜱı ᴀʟıɴıʀ...")
    served_chats = await get_active_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» {app.mention} ᴅaxɪʟɪɴᴅə ᴀᴋᴛɪᴠ ꜱəꜱʟɪ ᴢəɴɢ ʏᴏxᴅᴜʀ.")
    else:
        await mystic.edit_text(
            f"<b>» ʜᴀʟ-ʜᴀᴢıʀᴅᴀ ᴀᴋᴛɪᴠ ᴏʟᴀɴ ꜱəꜱʟɪ ᴢəɴɢʟəʀ :</b>\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["activev", "activevideo"]) & SUDOERS)
async def activevi_(_, message: Message):
    mystic = await message.reply_text("» ᴀᴋᴛɪᴠ ᴠɪᴅᴇᴏ ᴢəɴɢʟəʀɪɴ ꜱɪʏᴀʜıꜱı ᴀʟıɴıʀ...")
    served_chats = await get_active_video_chats()
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except:
            await remove_active_video_chat(x)
            continue
        try:
            if (await app.get_chat(x)).username:
                user = (await app.get_chat(x)).username
                text += f"<b>{j + 1}.</b> <a href=https://t.me/{user}>{unidecode(title).upper()}</a> [<code>{x}</code>]\n"
            else:
                text += (
                    f"<b>{j + 1}.</b> {unidecode(title).upper()} [<code>{x}</code>]\n"
                )
            j += 1
        except:
            continue
    if not text:
        await mystic.edit_text(f"» {app.mention} ᴅaxɪʟɪɴᴅə ᴀᴋᴛɪᴠ ᴠɪᴅᴇᴏ ᴢəɴɢ ʏᴏxᴅᴜʀ.")
    else:
        await mystic.edit_text(
            f"<b>» ʜᴀʟ-ʜᴀᴢıʀᴅᴀ ᴀᴋᴛɪᴠ ᴏʟᴀɴ ᴠɪᴅᴇᴏ ᴢəɴɢʟəʀ :</b>\n\n{text}",
            disable_web_page_preview=True,
        )
