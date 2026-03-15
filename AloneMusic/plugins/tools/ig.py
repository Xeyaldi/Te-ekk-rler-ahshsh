import requests
from pyrogram import filters

from AloneMusic import app


@app.on_message(filters.command(["ig", "instagram", "reel"]))
async def download_instagram_video(client, message):
    if len(message.command) < 2:
        await message.reply_text(
            "⚠️ <b>ʟᴜ̈ᴛғəɴ ᴋᴏᴍᴀɴᴅᴀᴅᴀɴ sᴏɴʀᴀ ʙɪʀ ɪɴsᴛᴀɢʀᴀᴍ ʟɪɴᴋɪ ᴅᴀxɪʟ ᴇᴅɪɴ.</b>"
        )
        return
    
    # Detektiv emojisi ilə yükləmə effekti
    a = await message.reply_text("🕵️‍♂️ <b>ᴍəʟᴜᴍᴀᴛʟᴀʀ ᴀxᴛᴀʀɪʟɪʀ...</b>")
    
    url = message.text.split()[1]
    api_url = (
        f"https://nodejs-1xn1lcfy3-jobians.vercel.app/v2/downloader/instagram?url={url}"
    )

    try:
        response = requests.get(api_url)
        data = response.json()

        if data["status"]:
            video_url = data["data"][0]["url"]
            await a.edit("🚀 <b>ᴠɪᴅᴇᴏ ʏᴜ̈ᴋʟəɴɪʀ...</b>")
            await client.send_video(message.chat.id, video_url)
            await a.delete()
        else:
            await a.edit("❌ <b>ᴠɪᴅᴇᴏ ʏᴜ̈ᴋʟəɴə ʙɪʟᴍəᴅɪ. ʟɪɴᴋɪ ʏᴏxʟᴀʏɪɴ.</b>")
    except Exception as e:
        await a.edit(f"⚠️ <b>xəᴛᴀ ʏᴀʀᴀɴᴅɪ:</b> <code>{e}</code>")


__MODULE__ = "ɪɴsᴛᴀɢʀᴀᴍ"
__HELP__ = """
/reel [ʟɪɴᴋ] - ɪɴsᴛᴀɢʀᴀᴍ ʀᴇᴇʟs ʏᴜ̈ᴋʟəʏəʀ.
/ig [ʟɪɴᴋ] - ɪɴsᴛᴀɢʀᴀᴍ ᴠɪᴅᴇᴏ ʏᴜ̈ᴋʟəʏəʀ.
/instagram [ʟɪɴᴋ] - ɪɴsᴛᴀɢʀᴀᴍ ᴍᴇᴅɪᴀ ʏᴜ̈ᴋʟəʏəʀ.
"""
