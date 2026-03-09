from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AloneMusic import app
import config

def help_pannel(, START: Union[bool, int] = None):
first = [InlineKeyboardButton(text=["CLOSE_BUTTON"], callback_data=f"close")]
second = [
InlineKeyboardButton(
text=["BACK_BUTTON"],
callback_data=f"settingsback_helper",
),
]
mark = second if START else first
upl = InlineKeyboardMarkup(
[
[
InlineKeyboardButton(
text=["S_B_3"],
url=f"https://t.me/{app.username}?startgroup=true",
)
],
[
InlineKeyboardButton(
text=["H_B_1"],
callback_data="help_callback hb1",
),
InlineKeyboardButton(
text=["H_B_2"],
callback_data="help_callback hb2",
),
],
[
InlineKeyboardButton(text=["S_B_2"], url=config.SUPPORT_CHAT),
InlineKeyboardButton(text=["S_B_5"], user_id=config.OWNER_ID),
],
[
InlineKeyboardButton(text="✚  ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ  ", url="https://www.youtube.com/@EpikTv87"),
],
mark,
]
)
return upl

def private_help_panel():
buttons = [
[
InlineKeyboardButton(
text=["S_B_4"],
url=f"https://t.me/{app.username}?start=help",
),
InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
],
[
InlineKeyboardButton(text="✚ ᴋᴀʏɴᴀᴋ ᴋᴏᴅᴜ ✚", url="https://www.youtube.com/@EpikTv87"),
],
]
return buttons
