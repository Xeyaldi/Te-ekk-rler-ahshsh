# ===========================================
# 💙 Kumsal Bots - Eşq Quşları Modulu
# Özəlliklər: Virtual Hədiyyə Sistemi + Sevgi Hekayəsi Yaradıcı (MongoDB)
# Tərcümə və Redaktə: Kumsal Music 💫
# Orijinal: Nand Yaduwanshi (NoxxOP)
# ===========================================

import random
from pyrogram import filters
from AloneMusic import app
from AloneMusic.core.mongo import mongodb
from config import MONGO_DB_URI

# MongoDB kolleksiyaları
lovebirds_db = mongodb.lovebirds
users_collection = lovebirds_db.users
gifts_collection = lovebirds_db.gifts

# 🎁 Hədiyyə Siyahısı
GIFTS = {
    "🌹": {"name": "Qızılgül", "cost": 10, "emoji": "🌹"},
    "🍫": {"name": "Şokolad", "cost": 20, "emoji": "🍫"},
    "🧸": {"name": "Oyuncaq Ayı", "cost": 30, "emoji": "🧸"},
    "💍": {"name": "Üzük", "cost": 50, "emoji": "💍"},
    "❤️": {"name": "Ürək", "cost": 5, "emoji": "❤️"},
    "🌺": {"name": "Gül Buketi", "cost": 25, "emoji": "🌺"},
    "💎": {"name": "Almaz", "cost": 100, "emoji": "💎"},
    "🎀": {"name": "Hədiyyə Qutusu", "cost": 40, "emoji": "🎀"},
    "🌙": {"name": "Ay", "cost": 35, "emoji": "🌙"},
    "⭐": {"name": "Ulduz", "cost": 15, "emoji": "⭐"},
    "🦋": {"name": "Kəpənək", "cost": 18, "emoji": "🦋"},
    "🕊️": {"name": "Göyərçin", "cost": 22, "emoji": "🕊️"},
    "🏰": {"name": "Qəsr", "cost": 80, "emoji": "🏰"},
    "🎂": {"name": "Tort", "cost": 28, "emoji": "🎂"},
    "🍓": {"name": "Çiyələk", "cost": 12, "emoji": "🍓"}
}


# ───────────────────────────────
# 🔹 İstifadəçi məlumatlarını çəkmə və ya yaratma
# ───────────────────────────────
async def get_user_data(user_id):
    if not user_id:
        return None

    user_data = await users_collection.find_one({"user_id": user_id})

    if not user_data:
        new_user = {
            "user_id": user_id,
            "coins": 50,  # Başlanğıc bonusu
            "total_gifts_received": 0,
            "total_gifts_sent": 0,
            "created_at": "2026"
        }
        await users_collection.insert_one(new_user)
        return new_user

    return user_data


# 🔹 Coin (Sikkə) yeniləmə
async def update_user_coins(user_id, amount):
    if not user_id:
        return

    await users_collection.update_one(
        {"user_id": user_id},
        {"$inc": {"coins": amount}},
        upsert=True
    )


# 🔹 İstifadəçi məlumatlarını al (TƏHLÜKƏSİZ)
def get_user_info(message):

    if not message or not message.from_user:
        return None, "Naməlum"

    user_id = message.from_user.id

    username = (
        message.from_user.username
        or message.from_user.first_name
        or "İstifadəçi"
    )

    return user_id, username

# ───────────────────────────────
# 💰 Balans Əmri
# ───────────────────────────────
@app.on_message(filters.command(["balans", "bal", "pul"], prefixes=["/", "!", "."]))
async def balance(_, message):
    uid, username = get_user_info(message)
    user_data = await get_user_data(uid)

    coins = user_data["coins"]
    gifts_received = await gifts_collection.count_documents({"receiver_id": uid})
    gifts_sent = await gifts_collection.count_documents({"sender_id": uid})

    balance_text = f"""
💰 <b>{username} Hesabı</b>
💸 <b>Balans:</b> {coins} coin
🎁 <b>Alınan Hədiyyələr:</b> {gifts_received}
📤 <b>Göndərilən Hədiyyələr:</b> {gifts_sent}

💡 <b>Məsləhət:</b> Qruplarda aktiv olduqca coin qazanarsan!
    """
    await message.reply_text(balance_text)


# ───────────────────────────────
# 🎁 Hədiyyə Siyahısı
# ───────────────────────────────
@app.on_message(filters.command("hediyyeler", prefixes=["/", "!", "."]))
async def gift_list(_, message):
    text = "🎁 <b>Mövcud Hədiyyələr:</b>\n\n"
    sorted_gifts = sorted(GIFTS.items(), key=lambda x: x[1]["cost"])

    for emoji, gift_info in sorted_gifts:
        text += f"{emoji} <b>{gift_info['name']}</b> - {gift_info['cost']} coin\n"

    text += "\n📝 <b>İstifadə:</b> /hediyyegonder @istifadechi 🌹"
    text += "\n💡 <b>Nümunə:</b> /hediyyegonder @ayxan 🍫"

    await message.reply_text(text)


# ───────────────────────────────
# 💌 Hədiyyə Göndərmə
# ───────────────────────────────
@app.on_message(filters.command("hediyyegonder", prefixes=["/", "!", "."]))
async def send_gift(_, message):
    try:
        parts = message.text.split(" ")
        if len(parts) < 3:
            return await message.reply_text("❌ <b>İstifadə:</b> /hediyyegonder @istifadechi 🌹")

        hedef = parts[1].replace("@", "")
        gift_emoji = parts[2]

        sender_id, sender_name = get_user_info(message)
        sender_data = await get_user_data(sender_id)

        if gift_emoji not in GIFTS:
            return await message.reply_text("❌ <b>Yanlış hədiyyə!</b> Bütün hədiyyələri görmək üçün /hediyyeler yaz.")

        gift_info = GIFTS[gift_emoji]
        cost = gift_info["cost"]

        if sender_data["coins"] < cost:
            return await message.reply_text(f"😢 <b>Kifayət qədər coinin yoxdur!</b>\n💰 Lazım olan: {cost}, Səndə olan: {sender_data['coins']}")

        await users_collection.update_one(
            {"user_id": sender_id},
            {"$inc": {"coins": -cost, "total_gifts_sent": 1}}
        )

        gift_record = {
            "sender_id": sender_id,
            "sender_name": sender_name,
            "receiver_name": hedef,
            "receiver_id": None,
            "gift_name": gift_info["name"],
            "gift_emoji": gift_emoji,
            "cost": cost,
            "timestamp": "2026",
            "claimed": False
        }

        await gifts_collection.insert_one(gift_record)
        updated_sender = await get_user_data(sender_id)

        success_msg = f"""
🎉 <b>Hədiyyə Göndərildi!</b>

{gift_emoji} <b>{sender_name}</b>, <b>@{hedef}</b> istifadəçisinə <b>{gift_info['name']}</b> göndərdi!

💝 <b>Detallar:</b>
• Hədiyyə: {gift_emoji} {gift_info['name']}
• Qiymət: {cost} coin
• Göndərən: {sender_name}
• Alıcı: @{hedef}

💰 <b>Qalan Balans:</b> {updated_sender['coins']} coin
💕 <i>Eşq havası hər yerdədir!</i>
        """

        await message.reply_text(success_msg)

    except Exception as e:
        await message.reply_text(f"⚠️ <b>Xəta:</b> {str(e)}")


# ───────────────────────────────
# 💕 Sevgi Hekayəsi Yaradıcı
# ───────────────────────────────
@app.on_message(filters.command(["hikaye", "hekaye"], prefixes=["/", "!", "."]))
async def love_story(_, message):
    try:
        parts = message.text.split(" ", 2)
        if len(parts) < 3:
            return await message.reply_text("❌ <b>İstifadə:</b> /hekaye Ad1 Ad2\n💡 <b>Nümunə:</b> /hekaye Əli Ayşə")

        isim1, isim2 = parts[1], parts[2]

        hikayeler = [
            f"Bir gün <b>{isim1}</b>, <b>{isim2}</b> ilə bir kafedə tanış oldu ☕. Göz-gözə gəldilər və tale onların hekayəsini yazdı ❤️✨",
            f"<b>{isim1}</b> yağış altında gəzərkən 🌧️, <b>{isim2}</b> çətirini ona uzatdı ☂️. O anda sevgi cücərdi 🌸",
            f"<b>{isim1}</b> və <b>{isim2}</b> eyni kitabı almaq üçün əllərini uzatdılar 📚. Barmaqları toxundu, qəlbləri isindi 💫💕",
            f"Bir konsert zamanı 🎵, <b>{isim1}</b> və <b>{isim2}</b> eyni mahnını oxudular. Ürəkləri eyni ritmdə döyündü 🎶❤️",
            f"<b>{isim1}</b> parkda quşlara dən verirdi 🐦, <b>{isim2}</b> də ona qoşuldu. O an səssizlik belə gözəlləşdi 💕"
        ]

        sonlar = [
            "\n\n💕 <i>Və sonsuza qədər xoşbəxt yaşadılar...</i>",
            "\n\n❤️ <i>Həqiqi sevgi hər zaman yolunu tapır...</i>",
            "\n\n🌹 <i>Hər sevgi hekayəsi gözəldir, amma onlarınkı ən özəli idi...</i>",
        ]

        hikaye = random.choice(hikayeler) + random.choice(sonlar)
        baslik = random.choice(["💕 <b>Sevgi Hekayəsi</b> 💕", "🌸 <b>Romantik Hekayə</b> 🌸", "❤️ <b>Eşq Nağılı</b> ❤️"])

        await message.reply_text(f"{baslik}\n\n{hikaye}")

        uid, _ = get_user_info(message)
        await update_user_coins(uid, 5)

    except Exception as e:
        await message.reply_text(f"⚠️ <b>Xəta:</b> {str(e)}")


# ───────────────────────────────
# 🎁 Alınan Hədiyyələr
# ───────────────────────────────
@app.on_message(filters.command(["hediyyem", "aldıqlarım"], prefixes=["/", "!", "."]))
async def my_gifts(_, message):
    uid, username = get_user_info(message)
    await get_user_data(uid)

    gifts_received = await gifts_collection.find({"receiver_id": uid}).to_list(length=10)

    if not gifts_received:
        await message.reply_text(f"📭 <b>{username}</b>, hələ heç bir hədiyyə almamısan!\n💡 Dostlarından /hediyyegonder ilə istəyə bilərsən 🎀")
        return

    text = f"🎁 <b>{username} istifadəçisinin Hədiyyələri:</b>\n\n"
    for i, gift in enumerate(gifts_received, 1):
        text += f"{i}. {gift['gift_emoji']} <b>{gift['gift_name']}</b> - <b>{gift['sender_name']}</b> tərəfindən\n"

    toplam = await gifts_collection.count_documents({"receiver_id": uid})
    text += f"\n💝 <b>Ümumi Hədiyyə Sayı:</b> {toplam}"

    await message.reply_text(text)


# ───────────────────────────────
# 🏆 Liderlik Cədvəli
# ───────────────────────────────
@app.on_message(filters.command(["liderlik", "zirve", "top"], prefixes=["/", "!", "."]))
async def leaderboard(_, message):
    try:
        top_users = await users_collection.find().sort("coins", -1).limit(10).to_list(length=10)
        if not top_users:
            return await message.reply_text("📊 Hələ ki heç bir istifadəçi yoxdur!")

        text = "🏆 <b>Ən Zəngin 10 İstifadəçi</b>\n\n"
        madalyalar = ["🥇", "🥈", "🥉"] + ["🏅"] * 7

        for i, user in enumerate(top_users):
            madalya = madalyalar[i] if i < len(madalyalar) else "🏅"
            text += f"{madalya} <b>İstifadəçi {user['user_id']}</b> — {user['coins']} coin\n"

        await message.reply_text(text)
    except Exception as e:
        await message.reply_text(f"⚠️ <b>Xəta:</b> {str(e)}")


# ───────────────────────────────
# 💬 Mesajla Coin Qazan
# ───────────────────────────────
@app.on_message(filters.text & ~filters.regex(r"^[/!.\-]"))
async def give_coins_and_claim_gifts(_, message):
    uid, username = get_user_info(message)
    await get_user_data(uid)

    # %20 ehtimalla coin qazan
    if random.randint(1, 100) <= 20:
        await update_user_coins(uid, 1)
