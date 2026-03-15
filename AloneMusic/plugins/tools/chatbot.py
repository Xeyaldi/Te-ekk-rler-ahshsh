import asyncio
import random
from typing import Union
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
)
from AloneMusic import app
from config import LOGGER_ID
from AloneMusic.plugins.tools.kumsal import *

# Sohbet rejimi açıq olan qrupları saxlayır
chatMode = []

# Sohbet rejimini açıb bağlayan istifadəçiləri izləmək üçün
chat_mode_users = {}

@app.on_message(filters.command("chatmode") & filters.group)
async def chat_mode_controller(bot, msg: Message):
    chat_id = msg.chat.id
    chat = msg.chat
    commands = msg.command
    chat_mode_users[chat_id] = msg.from_user.id  # Komandanı göndərən istifadəçini qeyd et

    # LOG GROUP-a mesaj göndər
    await bot.send_message(
        LOGGER_ID,
        f"""
#CHATMODE İSTİFADƏ EDİLDİ 👤 İstifadə edən : {msg.from_user.first_name} 💥 İstifadəçi Id : {msg.from_user.id} 🪐 İstifadə edilən Qrup : {chat.title} 💡 Qrup ID : {chat.id} ◀️ Qrup Linki : @{chat.username}"""
    )

    if len(commands) == 1:
        status = "✅ Açıq" if chat_id in chatMode else "❌ Bağlı"
        await msg.reply(
            f"Status : {status}\n\nSohbet rejimi istifadəçilərin mesajlarına cavab verir.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Aç", callback_data="on"),
                        InlineKeyboardButton("Bağla", callback_data="off"),
                    ]
                ]
            ),
        )

@app.on_callback_query(filters.regex("^(on|off)$"))
async def chat_mode_callback(bot, cb: CallbackQuery):
    chat_id = cb.message.chat.id
    cmd = cb.data

    # Artıq yetki yoxlanışı yoxdur, hər kəs dəyişə bilər
    if cmd == "on":
        if chat_id in chatMode:
            await cb.edit_message_text("Sohbet rejimi onsuz da açıqdır.")
        else:
            chatMode.append(chat_id)
            await cb.edit_message_text("Sohbet rejimi açıldı.")
    elif cmd == "off":
        if chat_id not in chatMode:
            await cb.edit_message_text("Sohbet rejimi onsuz da bağlıdır.")
        else:
            chatMode.remove(chat_id)
            await cb.edit_message_text("Sohbet rejimi bağlandı.")

    await cb.answer()

@app.on_message(filters.group & filters.text & ~filters.command("chatmode"), group=10)
async def chatModeHandler(bot, msg: Message):
    def lower(text):
        return str(text.translate({ord("I"): ord("ı"), ord("İ"): ord("i")})).lower()

    def kontrol(query: Union[str, list], text: str) -> bool:
        if isinstance(query, str):
            return query in text.split()
        elif isinstance(query, list):
            for q in query:
                if q in text.split():
                    return True
            return False
        else:
            return False

    if msg.chat.id not in chatMode or msg.from_user.is_self:
        return

    reply = None
    text = lower(msg.text)

    if text.startswith("ceyda"): 
        reply = random.choice(ceyda)
        await asyncio.sleep(0.06)

    elif kontrol(["selam", "slm", "sa", "selamlar", "selamm"], text): 
        reply = random.choice(slm)
        await asyncio.sleep(0.06)   
        
    elif kontrol(["sahip"], text): 
        reply = random.choice(sahip)
        await asyncio.sleep(0.06)   

    elif kontrol(["naber"], text): 
        reply = random.choice(naber)
        await asyncio.sleep(0.06)  

    elif kontrol(["beri"], text): 
        reply = random.choice(beri)
        await asyncio.sleep(0.06)        

    elif kontrol(["nasılsın"], text): 
        reply = random.choice(nasılsın)
        await asyncio.sleep(0.06)         

    elif kontrol(["tm","tamam","tmm"], text): 
        reply = random.choice(tm)
        await asyncio.sleep(0.06)          

    elif kontrol(["sus","suuss","suss"], text): 
        reply = random.choice(sus)
        await asyncio.sleep(0.06)  

    elif kontrol(["merhaba","mrb","meraba"], text): 
        reply = random.choice(merhaba)
        await asyncio.sleep(0.06)   

    elif kontrol(["yok"], text): 
        reply = random.choice(yok)
        await asyncio.sleep(0.06)   

    elif kontrol(["dur"], text): 
        reply = random.choice(dur)
        await asyncio.sleep(0.06)        

    elif kontrol(["bot", "botu"], text): 
        reply = random.choice(bott)
        await asyncio.sleep(0.06)         

    elif kontrol(["napıyorsun"], text): 
        reply = random.choice(napıyorsun)
        await asyncio.sleep(0.06)          

    elif kontrol(["takılıyorum","takılıyom"], text): 
        reply = random.choice(takılıyorum)
        await asyncio.sleep(0.06)  

    elif kontrol(["he"], text): 
        reply = random.choice(he)
        await asyncio.sleep(0.06)   

    elif kontrol(["hayır"], text): 
        reply = random.choice(hayır)
        await asyncio.sleep(0.06)   

    elif kontrol(["tm"], text): 
        reply = random.choice(tm)
        await asyncio.sleep(0.06)        

    elif kontrol(["nerdesin"], text): 
        reply = random.choice(nerdesin)
        await asyncio.sleep(0.06)         

    elif kontrol(["özledim"], text): 
        reply = random.choice(özledim)
        await asyncio.sleep(0.06)          

    elif kontrol(["bekle"], text): 
        reply = random.choice(bekle)
        await asyncio.sleep(0.06)  

    elif kontrol(["mustafa"], text): 
        reply = random.choice(mustafa)
        await asyncio.sleep(0.06)   

    elif kontrol(["günaydın"], text): 
        reply = random.choice(günaydın)
        await asyncio.sleep(0.06)   

    elif kontrol(["ragnar"], text): 
        reply = random.choice(ragnar)
        await asyncio.sleep(0.06)        

    elif kontrol(["konuşalım","konusalım"], text): 
        reply = random.choice(konuşalım)
        await asyncio.sleep(0.06)         

    elif kontrol(["saat"], text): 
        reply = random.choice(saat)
        await asyncio.sleep(0.06)          

    elif kontrol(["geceler"], text): 
        reply = random.choice(geceler)
        await asyncio.sleep(0.06)  

    elif kontrol(["şaka"], text): 
        reply = random.choice(şaka)
        await asyncio.sleep(0.06)   

    elif kontrol(["kimsin"], text): 
        reply = random.choice(kimsin)
        await asyncio.sleep(0.06)   

    elif kontrol(["günler"], text): 
        reply = random.choice(günler)
        await asyncio.sleep(0.06)        

    elif kontrol(["tanımıyorum"], text): 
        reply = random.choice(tanımıyorum)
        await asyncio.sleep(0.06)         

    elif kontrol(["konuşma"], text): 
        reply = random.choice(konuşma)
        await asyncio.sleep(0.06)          

    elif kontrol(["teşekkürler","tesekkürler","tşkr"], text): 
        reply = random.choice(teşekkürler)
        await asyncio.sleep(0.06)  

    elif kontrol(["eyvallah","eywl"], text): 
        reply = random.choice(eyvallah)
        await asyncio.sleep(0.06)   

    elif kontrol(["sağol"], text): 
        reply = random.choice(sağol)
        await asyncio.sleep(0.06)   

    elif kontrol(["amk","aq","mg","mk"], text): 
        reply = random.choice(amk)
        await asyncio.sleep(0.06)
        elif kontrol(["yoruldum"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yoruldum)
        await asyncio.sleep(0.06)         

    elif kontrol(["yaş"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yaş)
        await asyncio.sleep(0.06)          

    elif kontrol(["eşşək","eşek"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(eşek)
        await asyncio.sleep(0.06)  

    elif kontrol(["canım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(canım)
        await asyncio.sleep(0.06)   

    elif kontrol(["aşkım","askım","eşqim","esqim"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aşkım)
        await asyncio.sleep(0.06)   

    elif kontrol(["yat","uyu"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(uyu)
        await asyncio.sleep(0.06)        

    elif kontrol(["hara","haraya","nereye"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nereye)
        await asyncio.sleep(0.06)         

    elif kontrol(["necəsən","necesen","naber"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(naber)
        await asyncio.sleep(0.06)          

    elif kontrol(["küsdüm","küsüm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(küstüm)
        await asyncio.sleep(0.06)  

    elif kontrol(["yaxşı","yaxsi","peki"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(peki)
        await asyncio.sleep(0.06)   

    elif kontrol(["nə","ne","nee","ney"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ne)
        await asyncio.sleep(0.06)   

    elif kontrol(["komanda","takım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(takım)
        await asyncio.sleep(0.06)        

    elif kontrol(["mənimlə","benimle","bnmle"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(benimle)
        await asyncio.sleep(0.06)         

    elif kontrol(["sevirsen","sevirsenmi","seviyormusun"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(seviyormusun)
        await asyncio.sleep(0.06)          

    elif kontrol(["nədeyirsən","nediyon"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nediyon)
        await asyncio.sleep(0.06)  

    elif kontrol(["üzr","özür"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(özür)
        await asyncio.sleep(0.06)   

    elif kontrol(["niyə","niye"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(niye)
        await asyncio.sleep(0.06)   

    elif kontrol(["bilmirəm","bilmiram","bilmiyorum"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(bilmiyorum)
        await asyncio.sleep(0.06)        

    elif kontrol(["küsmə","kusme"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(küsme)
        await asyncio.sleep(0.06)         

    elif kontrol(["Cihan"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(cihan)
        await asyncio.sleep(0.06)          

    elif kontrol(["haralısan","nerelisin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nerelisin)
        await asyncio.sleep(0.06)  

    elif kontrol(["sevgilin"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sevgilin)
        await asyncio.sleep(0.06)   

    elif kontrol(["olar","olur"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(olur)
        await asyncio.sleep(0.06)   

    elif kontrol(["olmaz","olmas"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(olmaz)
        await asyncio.sleep(0.06)        

    elif kontrol(["necə","nece","nasıl"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(nasıl)
        await asyncio.sleep(0.06)         

    elif kontrol(["həyatım","hayatım"], text): # # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hayatım)
        await asyncio.sleep(0.06)          

    elif kontrol(["çüş","cus"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(cus)
        await asyncio.sleep(0.06)  

    elif kontrol(["vallah","vallaha","valla"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(vallaha)
        await asyncio.sleep(0.06)   

    elif kontrol(["yo"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yo)
        await asyncio.sleep(0.06)   

    elif kontrol(["xeyirdir","hayırdır"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hayırdır)
        await asyncio.sleep(0.06)        

    elif kontrol(["of"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(of)
        await asyncio.sleep(0.06)         

    elif kontrol(["eynən","aynen"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aynen)
        await asyncio.sleep(0.06)          

    elif kontrol(["ağla"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ağla)
        await asyncio.sleep(0.06)  

    elif kontrol(["ağlama"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ağlama)
        await asyncio.sleep(0.06)   

    elif kontrol(["Mehmet","yaren","cihan","alya"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(yaren)
        await asyncio.sleep(0.06)   

    elif kontrol(["bəli","hə","evet"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(evet)
        await asyncio.sleep(0.06)        

    elif kontrol(["hmm","hm","hımm","hmmm"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hmm)
        await asyncio.sleep(0.06)         

    elif kontrol(["hıhım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hıhım)
        await asyncio.sleep(0.06)          

    elif kontrol(["get","git"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(git)
        await asyncio.sleep(0.06)  

    elif kontrol(["komedi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(komedi)
        await asyncio.sleep(0.06)   

    elif kontrol(["kanka","knka"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(knka)
        await asyncio.sleep(0.06)   

    elif kontrol(["ban"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(ban)
        await asyncio.sleep(0.06)        

    elif kontrol(["sən","sen"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sen)
        await asyncio.sleep(0.06)         

    elif kontrol(["heç","hic"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(hiç)
        await asyncio.sleep(0.06)          

    elif kontrol(["aç","ac","açç"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(aç)
        await asyncio.sleep(0.06)  

    elif kontrol(["barışaq","barışalım"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(barışalım)
        await asyncio.sleep(0.06)   

    elif kontrol(["indi","şimdi"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(şimdi)
        await asyncio.sleep(0.06)   

    elif kontrol(["varoş"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(varoş)
        await asyncio.sleep(0.06)        

    elif kontrol(["dost","arkadaş","arkadas"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(arkadaş)
        await asyncio.sleep(0.06)         

    elif kontrol(["sus","suss","suus"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(sus)
        await asyncio.sleep(0.06)          

    elif kontrol(["üzüldüm","pis oldum"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(üzüldüm)
        await asyncio.sleep(0.06)  

    elif kontrol(["pis","kötü"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(kötü)
        await asyncio.sleep(0.06)   

    elif kontrol(["axşamlar","akşamlar"], text): # * Selam yazısı metnin içinde varsa cevap veriyoruz
        reply = random.choice(akşamlar)
        await asyncio.sleep(0.06)   

    try:
        await msg.reply(reply)
    except Exception as e:
        print(e)

    msg.continue_propagation()  #! BURAYA DOKUNMA
