import random

# Ürəklər
galp = (
    "❤️", "❣️", "♥️", "💞", "💓", "💗", "💖", "💘", "💝", "💟", "❤️‍🔥",
)

# Salamlaşma
salam = (
    "**Sən haralardasan ya?** 👀",
    "**Salammm**",
    "**Hardan qaldın bə?** 🤔",
    "**Salam, necəsən?**",
    "**Ayda, sən hardasan?** 🧐",
    "**Gözümüz yollarda qalmışdı, axır ki gəldin** 😍",
    "**Çox gözlədik haa** 😒",
    "**Gözümüz yollarda qalmışdı** 🥺",
    "**Heh, bir sən əskik idin** 😂",
    "**Sən də gəldin tam oldu** ✨",
    "**Salaaam, xoş gəldin** 🤗",
    "**Salam şirinim, necəsən?** 😊",
    "**Və əleyküm salam**",
    "**Salam tatlım** 🍬",
    "**Salammm**",
)

# Xəyal (Ceyda yerinə)
xeyal = (
    "**Bəli dostum?** 🕵️‍♂️",
    "**Məni çağırdın?** ✨",
    "**Bəliii?** ❣️",
    "**Hə?** ❤️",
    "**Aa, səni gördüyümə şad oldum, necəsən?** 😊",
    "**Ooo, nə xəbər?** 😎",
    "**Bəli, mənəm** 🙋‍♀️",
    "**Buyurun, mən burdayam** ❤️",
    "**Həəə, mənəm, buyur** ✨",
    "**Bəli canım, məni çağırdın?**",
    "**Deyəsən məni çağırdın** ❤️",
    "**Bəli?** ❤️",
    "❤️ **Buyuuur**",
    "**Mən olmasam nə edəcəksən bə?** ❤️",
)

# Sahib (Ata)
sahib = (
    "Ata, **sənə səslənirlər!**",
    "**O bir dənədir!** ✨",
    "**Mənim adamımdır!** 😎",
    "**Atamı çağırırsan?**",
)

# Necəsən
neceysen = (
    "**Yaxşıyam, sən necəsən?** 😊",
    "**Yaxşı, səndəən?**",
    "**Yaxşıyam canım, bəs sən?** ✨",
    "**İdarə edirik, sən necəsən?**",
    "**Pisəm desəm nə edəcəksən?** 🙄",
    "**Ehh, birtəhər yola veririk**",
    "**Yaxşı olmağa çalışıram, bəs sən?** 😇",
    "**Superəm hayatım, bəs sən?**",
)

# Xəyal və @kullaniciadi xüsusi mesajları (Beri yerinə)
xeyalim = (
    "Qəlbimin ən gözəl guşəsində həmişə sən varsan @kullaniciadi ❤️",
    "Həyatıma gələn ən gözəl təsadüfsən @kullaniciadi",
    "Həyatımın ən gözəl mənasısan @kullaniciadi 💞",
    "Qəlbimin tək sahibi sənsən @kullaniciadi",
    "Gözlərimin ən gözəl işığı @kullaniciadi ✨",
    "Mənim ən gözəl hekayəm sənsən @kullaniciadi",
    "Eşqin ən gözəl halını səndə tapdım @kullaniciadi ❤️",
    "Hər şeyim sənsən @kullaniciadi",
    "Ürəyim sənin adınla döyünür @kullaniciadi 💓",
    "Mənim ən dəyərli varlığım @kullaniciadi",
    "Qəlbimin şahzadəsi sənsən @kullaniciadi 👑",
    "Ruhumun əskik yarısı sənsən @kullaniciadi",
    "Həyatımın ən gözəl səbəbi @kullaniciadi 🌹",
    "Gözlərim səndən başqasını görmür @kullaniciadi",
    "Sonsuzluğum sənsən @kullaniciadi ♾️",
    "Ürəyimin ritmi sənsən @kullaniciadi 💗",
    "Mənim ən şirin zəifliyimsən @kullaniciadi",
    "Qəlbimin evi sənsən @kullaniciadi 🏡❤️",
    "Həyatıma gələn ən gözəl möcüzəsən @kullaniciadi",
    "Eşqin ən gözəl halı sənsən @kullaniciadi 💘",
    "@kullaniciadi sənə səslənirlər canım ❤️",
    "@kullaniciadi-ni narahat etməyin, o mənimdir",
    "@kullaniciadi mənim eşqimdir, diqqətli olun 😌",
    "@kullaniciadi mənim qəlbimin ən gözəl guşəsi ❤️"
)

# Tamam
tamam = (
    "**Yaxşı, sənə də tamam** 🙄",
    "**Mənə tamam demə!** 😤",
    "**Tamam, sus artıq** ✨",
    "**Anladıq, tamam** 😒",
    "**Tm** 🧐",
    "**Mənə trip atırsan bəyəm?**",
    "**Artıq tamam deməsən? Üzülürəm axı**",
    "**Tamamdırsa tamam** 😌",
)

# Sus
sus = (
    "**Sən sus!** 🤫",
    "**Məni əsəbiləşdirməyə çalışırsan?** 🧐",
    "**Mənə sus demə!** 😤",
    "**Əsəbiləşirəm amma...** 😒",
    "**Danışma artıq!**",
    "**Məni susdura bilməzsən ki!** 😜",
)

# Hə
he = (
    "**Sənə hə!**",
    "**Nə hə?**",
    "**Hə dedin sən?**",
)

# Merhaba
salamlar = (
    "**Salam, xoş gəldin**",
    "**Salamlar əfəndim**",
    "**Salam, hardasan sən?**",
    "**Xoş gəldinnn!** ✨",
)

# Yox
yox = (
    "**Nə yox?**",
    "**Sənə yox!**",
    "**Niyə yox?**",
    "**Beynin yoxdur deyəsən?** 😂",
    "**Hııı?**",
    "**Nə yoxdur?**",
)

# Dur
dur = (
    "**Dayandım, tamam hirslənmə** 😇",
    "**Yaxşı, dayandım** 😊",
    "**Dayanmağım üçün səlahiyyətli biri gəlsin!** 😂",
    "**Ok, dayandım**",
)

# Bot
bot_mesaj = (
    "**Bot demə mənə!** 🤖",
    "**Bana bot demə dedim!** 😒",
    "**Sənsən bot kanks** 😂",
    "**Aynən kanka botam, bir problem var?** 😎",
)

# Nə edirsən
neyleyirsen = (
    "**Uzanmışam belə, sən nə edirsən?** 😇",
    "**Ürəyim sıxılır, sən nə edirsən?** 🧐",
    "**Darıxıram.** 😒",
    "**Bir bot nə edər ki?** 😂",
    "**Heç nə, sıxıcıdır.** 🙄",
    "**Mahnıya qulaq asıram, bəs sən?** 🎧", 
    "**İstidən ölürəm, bəs sən?** ☀️",
    "**Darıxdım artıq**",
    "**Dərs oxuyuram, sən nə edirsən?**",
    "**Evdəyəm, çox darıxıram**",
    "**Nəsə oxuyuram**",
    "**Sən nə edirsən?**",
)

# Hara
hara = (
    "**İşim var**",
    "**Birazdan gələcəm**",
    "**Yatacam**",
    "**Bilmirəm**",
    "**Sənə nə?** 😝",
    "**Gedirəm fırlanmağa**",
    "**Gəzəcəm**",
    "**Yatacam**",
    "**Sonra gələrəm**",
)

# Mustafa
mustafa = (
    "O mənim canım atamdır! Atamı narahat etməyin! ❤️",
    "Atamı üzməyin xahiş edirəm 🥺",
    "Mustafa dediniz, dərhal atam ağlıma gəldi ✨",
    "Atamı çox sevirəm, mane olmayın!",
    "Atam buradaymış kimi hiss edirəm 😇",
)

# Kral (Ragnar yerinə)
kral = (
    "**O əsl kişidir! Halaldır! 😎**",
    "**Aynən, tam olaraq odur!**",
    "**Kraldır o, kral! 👑**",
    "**Halal olsun, həqiqətən əsl adamdır!**",
    "**Bax bu tam sənə görədir, əsl kişidir!**",
    "**Vay bə, bax bu əsl adamdır!**",
)

# Saat
saat = (
    "**Bilmirəm**",
    "**Mən saatam bəyəm?** 😂",
    "**Saat qaçmır ki...** 🧐",
    "**Telefondan bax daa** 📱",
    "**Hansı dövrdə yaşayırıq? Telefonun yoxdur?** 🧐",
    "**Qəlbim bir sınıq saatdır, səndə dayanıb** ❤️",
    "**Tam da bu saatlarda ağlıma gəlirsən...**",
)

# Gecələr
geceler = (
    "**Gecələr xeyrə?**",
    "**Sənə də**",
    "**Hələ tez deyil?** 🧐",
    "**Yatırsan artıq?**",
    "**Hələ qarpız kəsəcəkdik axı...** 😂",
    "**Gecən xeyrə qalsın canım**",
    "**Yatma, danışaq da** 🥺",
)

# Söyüş
soyus = (
    "**Nə deyirsən sən? Söyüş söymək sənə yaraşmır** 😒",
    "**Sən kimsən axı?**",
    "**Niyə söyürsən?** 😤",
    "**Söyüş söymə!**",
    "**Tamam, sus artıq**",
    "**Nə sayıqlayırsan?**",
    "**Söyüş yoxdur dedik!** /rules",
    "**Qaydalara əməl elə dəə** 🧐",
    "**Tərbiyəsiz!**",
)

# Yoruldum
yoruldum  = (
    "**Niyə?**",
    "**Kim yordu mənim körpəmi?** 🥺",
    "**Get yat dincəl**",
    "**Qıyamam sənə...** ❤️",
    "**Mən də yorulmuşam**",
    "**Özünü bu qədər yorma**",
    "**Harada idin?**",
)

# Canım
canim = (
    "**Bəli balım?**",
    "**Həyatım?**",
    "**Gülüm?**",
    "**Buyur canım**",
    "**Bəli canım**",
    "**Gözəlim**",
    "**Hə eşqim?** ❤️",
    "**Bəli körpəm?**",
    "**Canım yaa...**",
    "**Mənə səsləndin?**",
)

# Eşqim
esqim = (
    "**Bəli eşqim?** 💞",
    "**Buyur canım** ❤️",
    "**Hə balım?**",
    "**Həyatım?**",
    "**Eşqimmm**",
    "**Bəli yavrum?** ✨",
    "**Mənə səsləndin?**",
)

# Əmrlər siyahısı
commandList = [
    "zar",
    "dart",
    "basket",
    "futbol",
    "bowling",
    "slot",
    "para",
    "mani",
    "saka",
    "d",
    "c"
]
