import os
import asyncio
from pyrogram import filters
from pyrogram.types import Message
import yt_dlp
from yt_dlp.utils import DownloadError
import httpx  # HTTP istəkləri üçün

from AloneMusic import app  # @app dekoratorları üçün

# ----------------- AYARLAR -----------------

COOKIE_URL = "https://github.com/derdomehmet141-sketch/AloneMusic"  # GitHub repo URL-si
COOKIE_FILE = "./cookies/cookies.txt"  # Cookie faylının saxlanılacağı yol
DOWNLOAD_PATH = "./downloads"  # Yükləmə ediləcək yol
os.makedirs(DOWNLOAD_PATH, exist_ok=True)  # Yüklənən faylların saxlanılacağı qovluq

# ----------------- COOKIE FAYLINI YÜKLƏMƏ FUNKSİYASI -----------------

async def download_cookie():
    """Cookie faylını GitHub repo URL-sindən yüklə"""
    async with httpx.AsyncClient() as client:
        response = await client.get(COOKIE_URL)
        if response.status_code == 200:
            # Cookie faylını yadda saxla
            with open(COOKIE_FILE, 'wb') as f:
                f.write(response.content)
        else:
            raise Exception(f"Cookie faylı yüklənə bilmədi. HTTP Statusu: {response.status_code}")

# ----------------- AXTARIŞ VƏ GÖNDƏRMƏ FUNKSİYASI -----------------

async def search_and_send(message: Message, search_type: str = "music"):
    """Axtarış və göndərmə prosesi"""
    # Cookie faylının olub-olmadığını yoxla
    if not os.path.exists(COOKIE_FILE):
        await message.reply_text("❌ Cookie faylı tapılmadı. Hal-hazırda axtarış etmək mümkün deyil.")
        return

    # Əmr yoxlanışı
    if len(message.command) < 2:
        await message.reply_text(
            "❌ ʟüᴛꜰəɴ ᴀxᴛᴀʀış ꜱöᴢü ʏᴀᴢıɴ.\n"
            f"Öʀɴəᴋ: /{'bul' if search_type == 'music' else 'vbul'} Taladro"
        )
        return

    query = " ".join(message.command[1:])  # Axtarış sözü
    status_msg = await message.reply_text(
        f"🔎 `{query}` ɪçɪɴ ᴀxᴛᴀʀış ᴇᴅɪʟɪʀ və ʏüᴋʟəɴɪʀ, ʟüᴛꜰəɴ ʙəᴋʟəʏɪɴ..."
    )

    # ----------------- AXTARIŞ -----------------
    ydl_opts_search = {
        "quiet": True,
        "format": "bestaudio/best" if search_type == "music" else "best",
        "noplaylist": True,
        "cookiefile": COOKIE_FILE,  # Cookie faylını yüklə
        "skip_download": True,
        "extract_flat": True,  # Playlist və ya video ekstraktı edilmir
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts_search) as ydl:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)
            entries = info.get("entries", [])

            if not entries:  # Əgər nəticə tapılmazsa
                await status_msg.edit_text("❌ ɴəᴛɪᴄə ᴛᴀᴘıʟᴍᴀᴅı.")
                return

            first_result = entries[0]  # İlk nəticəni götür
            url = first_result.get("url")
            title = first_result.get("title") or "Adsız"

        # ----------------- YÜKLƏMƏ -----------------
        safe_title = "".join([c if c.isalnum() or c in " _-" else "_" for c in title])
        ext = "mp3" if search_type == "music" else "mp4"
        file_name = os.path.join(DOWNLOAD_PATH, f"{safe_title}.{ext}")

        ydl_opts_download = {
            "format": "bestaudio/best" if search_type == "music" else "best",
            "outtmpl": file_name,
            "cookiefile": COOKIE_FILE,  # Cookie faylını istifadə et
            "quiet": True,
        }

        await status_msg.edit_text(f"⬇️  `{title}` ʏüᴋʟəɴɪʀ...")
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, lambda: yt_dlp.YoutubeDL(ydl_opts_download).download([url]))

        # ----------------- ÇATA GÖNDƏR -----------------
        await status_msg.edit_text(f"✅  `{title}` ʏüᴋʟəɴᴅɪ, ɢöɴᴅəʀɪʟɪʀ...")
        if search_type == "music":
            await message.reply_audio(file_name, caption=title)
        else:
            await message.reply_video(file_name, caption=title)

        # Fayl təmizliyi
        try:
            os.remove(file_name)
        except Exception:
            pass

        await status_msg.delete()

    except DownloadError as e:
        await status_msg.edit_text(f"❌ ʏᴏᴜᴛᴜʙᴇ xəᴛᴀꜱı: {e}")
    except Exception as e:
        await status_msg.edit_text(f"❌ xəᴛᴀ ʙᴀş ᴠᴇʀᴅɪ: {e}")

# ----------------- ƏMR BAĞLANTILARI -----------------

@app.on_message(filters.command("bul") & filters.private)
async def music_search(client, message: Message):
    await search_and_send(message, search_type="music")  # Musiqi axtarışı

@app.on_message(filters.command("vbul") & filters.private)
async def video_search(client, message: Message):
    await search_and_send(message, search_type="video")  # Video axtarışı
