#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
# This file is part of < https://github.com/TheAloneTeam/AloneMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/AloneMusic/blob/master/LICENSE >
#
# All rights reserved.

import os
import sys
import traceback
from datetime import datetime
from functools import wraps

import aiofiles
from pyrogram.errors.exceptions.forbidden_403 import ChatWriteForbidden

from AloneMusic import app
from AloneMusic.utils.exceptions import is_ignored_error
from AloneMusic.utils.pastebin import AloneBin
from config import DEBUG_IGNORE_LOG, LOGGER_ID

DEBUG_LOG_FILE = "ignored_errors.log"


# ========== Paste Fallback ==========


async def send_large_error(text: str, caption: str, filename: str):
    try:
        paste_url = await AloneBin(text)
        if paste_url:
            await app.send_message(LOGGER_ID, f"{caption}\n\n🔗 Paste Linki: {paste_url}")
            return
    except Exception:
        pass

    path = f"{filename}.txt"
    async with aiofiles.open(path, "w") as f:
        await f.write(text)
    await app.send_document(LOGGER_ID, path, caption="❌ Xəta Logu (Fayl olaraq)")
    os.remove(path)


# ========== Formatting & Routing ==========


def format_traceback(err, tb, label: str, extras: dict = None) -> str:
    exc_type = type(err).__name__
    parts = [
        f"🚨 <b>{label} Tutuldu</b>",
        f"📍 <b>Xəta Növü:</b> <code>{exc_type}</code>",
    ]
    if extras:
        parts.extend([f"📌 <b>{k}:</b> <code>{v}</code>" for k, v in extras.items()])
    parts.append(f"\n<b>Xəta İzləmə (Traceback):</b>\n<pre>{tb}</pre>")
    return "\n".join(parts)


async def handle_trace(err, tb, label, filename, extras=None):
    if is_ignored_error(err):
        await log_ignored_error(err, tb, label, extras)
        return

    caption = format_traceback(err, tb, label, extras)
    if len(caption) > 4096:
        await send_large_error(tb, caption.split("\n\n")[0], filename)
    else:
        await app.send_message(LOGGER_ID, caption)


async def log_ignored_error(err, tb, label, extras=None):
    if not DEBUG_IGNORE_LOG:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines = [
        f"\n--- İqnor Edilən Xəta | {label} @ {timestamp} ---",
        f"Növ: {type(err).__name__}",
        *(f"{key}: {val}" for key, val in (extras or {}).items()),
        "Traceback:",
        tb.strip(),
        "------------------------------------------\n",
    ]
    async with aiofiles.open(DEBUG_LOG_FILE, "a") as log:
        await log.write("\n".join(lines))


# ========== Decorators ==========


def capture_err(func):
    """
    Əmr emal edicilərindəki xətaları idarə edir.
    Yalnız vacib xətaları loglayır.
    """

    @wraps(func)
    async def wrapper(client, message, *args, **kwargs):
        try:
            return await func(client, message, *args, **kwargs)
        except ChatWriteForbidden:
            await app.leave_chat(message.chat.id)
        except Exception as err:
            tb = "".join(traceback.format_exception(*sys.exc_info()))
            extras = {
                "İstifadəçi": message.from_user.mention if message.from_user else "Bilinmir",
                "Əmr": message.text or message.caption,
                "Qrup ID": message.chat.id,
            }
            filename = f"error_log_{message.chat.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            await handle_trace(err, tb, "Xəta", filename, extras)
            raise err

    return wrapper


def capture_callback_err(func):
    """
    Düymə (callback) əməliyyatlarında yaranan xətaları idarə edir.
    """

    @wraps(func)
    async def wrapper(client, callback_query, *args, **kwargs):
        try:
            return await func(client, callback_query, *args, **kwargs)
        except Exception as err:
            tb = "".join(traceback.format_exception(*sys.exc_info()))
            extras = {
                "İstifadəçi": (
                    callback_query.from_user.mention
                    if callback_query.from_user
                    else "Bilinmir"
                ),
                "Qrup ID": callback_query.message.chat.id,
            }
            filename = f"cb_error_log_{callback_query.message.chat.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            await handle_trace(err, tb, "Düymə Xətası", filename, extras)
            raise err

    return wrapper


def capture_internal_err(func):
    """
    Botun daxili/arxa plan funksiyalarındakı xətaları idarə edir.
    """

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as err:
            tb = "".join(traceback.format_exception(*sys.exc_info()))
            extras = {"Funksiya": func.__name__}
            filename = f"internal_error_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            await handle_trace(err, tb, "Daxili Xəta", filename, extras)
            raise err

    return wrapper
