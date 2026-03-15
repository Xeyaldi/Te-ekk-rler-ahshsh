#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
#
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Dᴀʏᴀɴᴅıʀ",
            description="ᴠɪᴅᴇᴏ çᴀᴛᴅᴀ ʜᴀᴢıʀᴅᴀ ɪғᴀ ᴏʟᴜɴᴀɴ ʏᴀʏıᴍı ᴅᴀʏᴀɴᴅıʀıɴ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="ᴅᴀᴠᴀᴍ ᴇᴛ",
            description="ᴠɪᴅᴇᴏ çᴀᴛᴅᴀ ᴅᴀʏᴀɴᴅıʀıʟᴍış ʏᴀʏıᴍı ᴅᴀᴠᴀᴍ ᴇᴛᴅɪʀɪɴ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="ᴋᴇç",
            description="ʜᴀᴢıʀᴅᴀᴋı ʏᴀʏıᴍı ᴋᴇçɪɴ ᴠə ɴöᴠʙəᴛɪ ᴍᴀʜɴıʏᴀ ᴋᴇçɪᴅ ᴇᴅɪɴ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="sᴏɴʟᴀɴᴅıʀ",
            description="ᴠɪᴅᴇᴏ çᴀᴛᴅᴀ ʜᴀᴢıʀᴅᴀ ɪғᴀ ᴏʟᴜɴᴀɴ ʏᴀʏıᴍı ᴅᴀʏᴀɴᴅıʀıɴ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/end"),
        ),
        InlineQueryResultArticle(
            title="ǫᴀʀışᴅıʀ",
            description="ᴘʟᴇʏʟɪsᴛᴅəᴋɪ ɴöᴠʙəᴅə ᴏʟᴀɴ ᴍᴀʜɴıʟᴀʀı ǫᴀʀışᴅıʀıɴ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="ᴅöᴠʀɪʏʏə",
            description="ʜᴀᴢıʀᴅᴀ ɪғᴀ ᴏʟᴜɴᴀɴ ᴍᴀʜɴıɴı ᴛəᴋʀᴀʀᴀ sᴀʟıɴ.",
            thumb_url="https://telegra.ph/file/c5952790fa8235f499749.jpg",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
