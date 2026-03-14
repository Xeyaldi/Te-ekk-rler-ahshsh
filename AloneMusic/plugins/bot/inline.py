#
# Yenidən dizayn edilmiş İinline Search modulu.
#

from py_yt import VideosSearch
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultPhoto)

from AloneMusic import app
from AloneMusic.utils.inlinequery import answer
from config import BANNED_USERS


@app.on_inline_query(~BANNED_USERS)
async def inline_query_handler(client, query):
    text = query.query.strip().lower()
    answers = []
    if text.strip() == "":
        try:
            await client.answer_inline_query(query.id, results=answer, cache_time=10)
        except:
            return
    else:
        a = VideosSearch(text, limit=20)
        result = (await a.next()).get("result")
        for x in range(15):
            title = (result[x]["title"]).title()
            duration = result[x]["duration"]
            views = result[x]["viewCount"]["short"]
            thumbnail = result[x]["thumbnails"][0]["url"].split("?")[0]
            channellink = result[x]["channel"]["link"]
            channel = result[x]["channel"]["name"]
            link = result[x]["link"]
            published = result[x]["publishedTime"]
            
            # Təsvir hissəsini daha səliqəli etdim
            description = f"👁️ {views} | ⏱️ {duration} dəq | 📺 {channel}"
            
            buttons = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🌐 ʏᴏᴜᴛᴜʙᴇ-ᴅᴀ ɪ̇ᴢʟə",
                            url=link,
                        )
                    ],
                ]
            )
            
            # Mətni tamamilə fərqli bir dizayna saldım
            searched_text = f"""
🎬 <b>ʙᴀşʟɪǫ:</b> <a href={link}>{title}</a>

⏳ <b>ᴍᴜ̈ᴅᴅəᴛ:</b> {duration} ᴅəǫɪǫə
📊 <b>ʙᴀxɪş:</b> <code>{views}</code>
📡 <b>ᴋᴀɴᴀʟ:</b> <a href={channellink}>{channel}</a>
📅 <b>ʏᴀʏɪᴍ:</b> {published}

✨ <b>{app.name} ɪ̇ɴʟɪɴᴇ ᴀxᴛᴀʀɪş sɪsᴛᴇᴍɪ</b>"""

            answers.append(
                InlineQueryResultPhoto(
                    photo_url=thumbnail,
                    title=title,
                    thumb_url=thumbnail,
                    description=description,
                    caption=searched_text,
                    reply_markup=buttons,
                )
            )
        try:
            return await client.answer_inline_query(query.id, results=answers)
        except:
            return
