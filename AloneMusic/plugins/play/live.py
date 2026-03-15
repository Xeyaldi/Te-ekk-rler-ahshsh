#
# Yenidən dizayn edilmiş Canlı Yayım (Live Stream) Modulu.
#

from pyrogram import filters

from AloneMusic import YouTube, app
from AloneMusic.utils.channelplay import get_channeplayCB
from AloneMusic.utils.decorators.language import languageCB
from AloneMusic.utils.stream.stream import stream
from config import BANNED_USERS


@app.on_callback_query(filters.regex("LiveStream") & ~BANNED_USERS)
@languageCB
async def play_live_stream(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    vidid, user_id, mode, cplay, fplay = callback_request.split("|")
    
    # İstifadəçi yoxlanışı
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(_["playcb_1"], show_alert=True)
        except:
            return
            
    try:
        chat_id, channel = await get_channeplayCB(_, cplay, CallbackQuery)
    except:
        return
        
    video = True if mode == "v" else None
    user_name = CallbackQuery.from_user.first_name
    
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        pass

    # Detektiv emojisi ilə axtarış mesajı
    mystic = await CallbackQuery.message.reply_text(
        f"🕵️‍♂️ <b>ᴄᴀɴʟɪ ʏᴀʏɪᴍ ᴀxᴛᴀʀɪʟɪʀ...</b>\n" + 
        (_["play_2"].format(channel) if channel else _["play_1"])
    )
    
    try:
        details, track_id = await YouTube.track(vidid, True)
    except:
        return await mystic.edit_text("❌ <b>ᴍəʟᴜᴍᴀᴛ ᴀʟɪɴᴀʀᴋəɴ xəᴛᴀ ʏᴀʀᴀɴᴅɪ.</b>")
        
    ffplay = True if fplay == "f" else None
    
    if not details["duration_min"]:
        try:
            await stream(
                _,
                mystic,
                user_id,
                details,
                chat_id,
                user_name,
                CallbackQuery.message.chat.id,
                video,
                streamtype="live",
                forceplay=ffplay,
            )
        except Exception as e:
            ex_type = type(e).__name__
            err = e if ex_type == "AssistantErr" else _["general_2"].format(ex_type)
            return await mystic.edit_text(err)
    else:
        # Canlı yayım deyilsə verilən xəta
        return await mystic.edit_text("⚠️ <b>ʙᴜ ᴄᴀɴʟɪ ʏᴀʏɪᴍ ᴅᴇʏɪʟ. ʟᴜ̈ᴛғəɴ ɴᴏʀᴍᴀʟ ᴏʏɴᴀᴛᴍᴀ ᴍᴏᴅᴜɴᴅᴀɴ ɪsᴛɪғᴀᴅə ᴇᴅɪɴ.</b>")
    
    await mystic.delete()
