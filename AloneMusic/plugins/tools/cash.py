import asyncio
import random
from datetime import datetime, timedelta
from pyrogram import filters
from pyrogram.types import Message
from AloneMusic import app  # Botun app instansiyası
from AloneMusic.core.mongo import mongodb   # ✅ MongoDB bağlantısı

db = mongodb.games  # MongoDB-də 'games' kolleksiyasına giriş
initial_balance = 25000  # İstifadəçilər üçün ilkin balans

# 🔹 İstifadəçi balansını əldə et
async def get_balance(user_id: int) -> int:
    user = await db.find_one({"_id": user_id})
    if user:
        return user.get("balance", initial_balance)
    return initial_balance

# 🔹 İstifadəçi balansını yenilə
async def update_balance(user_id: int, amount: int):
    current_balance = await get_balance(user_id)
    new_balance = max(current_balance + amount, 0)  # Balansın mənfi olmasının qarşısını al
    await db.update_one(
        {"_id": user_id},
        {"$set": {"balance": new_balance}},
        upsert=True,
    )
    return new_balance

# 🎰 Slot oyunu
@app.on_message(filters.command("cash") & filters.group)
async def play_slot(_, message: Message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply("İstifadə qaydası: /cash [məbləğ] [istəyə bağlı vuran] 🎰")

    try:
        amount = int(message.command[1])
        multiplier = 1
        if len(message.command) > 2 and message.command[2].endswith("x"):
            multiplier = int(message.command[2][:-1])
            if multiplier < 1 or multiplier > 6:
                return await message.reply("Vuran (multiplier) 1x ilə 6x arası olmalıdır.")
    except:
        return await message.reply("Düzgün bir məbləğ daxil edin. Nümunə: /cash 50 2x")

    balance = await get_balance(user_id)
    if amount > balance:
        return await message.reply("Balansınız kifayət deyil. 😢")

    # Uduş şansı 50/50
    win_amount = amount * multiplier if random.random() < 0.5 else -amount * multiplier
    new_balance = await update_balance(user_id, win_amount)
    
    # Azərbaycan adları ilə nəticə mesajı
    result = "qazandınız 🎉" if win_amount > 0 else "itirdiniz 🥹"
    
    await message.reply(
        f"{win_amount} AZN {result}!\n💰 Cari balansınız: {new_balance} AZN"
    )

# 🏀 Basketbol oyunu
@app.on_message(filters.command("bcash") & filters.group)
async def play_basket(_, message: Message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply("İstifadə qaydası: /bcash [məbləğ] [istəyə bağlı vuran] 🏀")

    try:
        amount = int(message.command[1])
        multiplier = 1
        if len(message.command) > 2 and message.command[2].endswith("x"):
            multiplier = int(message.command[2][:-1])
            if multiplier < 1 or multiplier > 6:
                return await message.reply("Vuran 1x ilə 6x arası olmalıdır.")
    except:
        return await message.reply("Düzgün bir məbləğ daxil edin.")

    balance = await get_balance(user_id)
    if amount > balance:
        return await message.reply("Balansınız kifayət deyil.")

    dice = await app.send_dice(message.chat.id, emoji="🏀")
    await asyncio.sleep(3)

    if dice.dice.value >= 4:
        win_amount = amount * multiplier
        text = f"🏀 Təbriklər! Səbətə girdi. +{win_amount} AZN"
    else:
        win_amount = -amount * multiplier
        text = f"🏀 Təəssüf, qaçırtdınız. {amount * multiplier} AZN itirdiniz."

    new_balance = await update_balance(user_id, win_amount)
    await message.reply(f"{text}\n💰 Cari balansınız: {new_balance} AZN")

# ⚽ Futbol oyunu
@app.on_message(filters.command("fcash") & filters.group)
async def play_football(_, message: Message):
    user_id = message.from_user.id
    if len(message.command) < 2:
        return await message.reply("İstifadə qaydası: /fcash [məbləğ] [istəyə bağlı vuran] ⚽")

    try:
        amount = int(message.command[1])
        multiplier = 1
        if len(message.command) > 2 and message.command[2].endswith("x"):
            multiplier = int(message.command[2][:-1])
            if multiplier < 1 or multiplier > 6:
                return await message.reply("Vuran 1x ilə 6x arası olmalıdır.")
    except:
        return await message.reply("Düzgün bir məbləğ daxil edin.")

    balance = await get_balance(user_id)
    if amount > balance:
        return await message.reply("Balansınız kifayət deyil.")

    dice = await app.send_dice(message.chat.id, emoji="⚽")
    await asyncio.sleep(3)

    if dice.dice.value >= 3:
        win_amount = amount * multiplier
        text = f"⚽ Qooool! +{win_amount} AZN"
    else:
        win_amount = -amount * multiplier
        text = f"⚽ Qaçırdınız. {amount * multiplier} AZN itirdiniz."

    new_balance = await update_balance(user_id, win_amount)
    await message.reply(f"{text}\n💰 Cari balansınız: {new_balance} AZN")

# 💰 Balansı yoxla
@app.on_message(filters.command("bakiye"))
async def check_balance(_, message: Message):
    user_id = message.from_user.id
    balance = await get_balance(user_id)
    await message.reply(f"Cari balansınız: {balance} AZN 💰")

# 🎁 Gündəlik bonus
@app.on_message(filters.command(["gunluk", "günlük"]))
async def daily_bonus(_, message: Message):
    user_id = message.from_user.id
    now = datetime.utcnow()

    user = await db.find_one({"_id": user_id})
    last_bonus = user.get("last_bonus") if user else None

    if last_bonus and now - last_bonus < timedelta(hours=5):
        return await message.reply("Gündəlik bonus üçün bir az daha gözlə ⏳")

    await db.update_one(
        {"_id": user_id},
        {"$inc": {"balance": 50000}, "$set": {"last_bonus": now}},
        upsert=True,
    )

    balance = await get_balance(user_id)
    await message.reply(f"🎁 Gündəlik bonus aldınız: 50.000 AZN\n💰 Cari balansınız: {balance} AZN")

# 🏆 Zənginlər Siyahısı (Azərbaycan adları və Dağları mövzulu sıralama)
@app.on_message(filters.command("zenginler"))
async def rich_list(_, message: Message):
    cursor = db.find().sort("balance", -1).limit(10)
    users = await cursor.to_list(length=10)

    if not users:
        return await message.reply("Hələ heç bir istifadəçi oynamayıb.")

    # Siyahı başlığına Azərbaycan dağ ruhu əlavə etdik
    text = "🏔️ **Azərbaycanın Ən Zənginləri (Şahdağ Zirvəsi):**\n\n"
    for i, user in enumerate(users, start=1):
        try:
            tg_user = await app.get_users(user["_id"])
            # Tural, Aytən, Elvin kimi adlar sistemdən çəkiləcək, lakin tapa bilməsə aşağıdakı default adlar işləyəcək
            name = tg_user.first_name
        except:
            # Əgər istifadəçi tapılmasa default Azərbaycan adları (Nümunə üçün)
            default_names = ["Anar", "Leyla", "Vüsal", "Nigar", "Tural", "Günay", "Elvin", "Fidan", "Murad", "Arzu"]
            name = f"{random.choice(default_names)} (User-{user['_id']})"
            
        text += f"{i}. {name} — {user['balance']} AZN\n"

    await message.reply(text)
