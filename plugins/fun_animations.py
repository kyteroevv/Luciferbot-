# =============================================================================
#  CipherElite Userbot Plugin - Mega Ultimate Master File (All-in-One)
# =============================================================================

import asyncio
import random
import os
from collections import deque
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from utils.utils import CipherElite
from utils.decorators import rishabh
from plugins.bot import add_handler

DEFAULTUSER = "Elite User"

# Simple memory storage for copyright strikes tracking (user_id: count)
cpright_strikes = {}

def init(client):
    """Initialize the mega all-in-one plugin with utilities and moderation"""
    commands = [
        # --- Desi & Swag ---
        ".gym       - Gym motivation & biceps flex",
        ".hustle    - Late night hustle & money mindset",
        ".bike      - Rider attitude & speed vibe",
        ".bhai      - Jigri dost ke liye dialogue",
        ".dekh      - Savage reply to haters",
        ".roast     - Dost ki taang khinchne ke liye",
        ".paise     - Jeb khali hone ka dukh",
        ".patli     - Mauka dekh kar 9 do 11 hona",
        ".bhoot     - Bhoot / Ex prank animation",
        ".slap      - Solid thappad action",
        # --- Flirt & Shayari ---
        ".flirt     - Smooth & funny flirt lines",
        ".shayari   - Unique romantic shayari lines",
        ".nazar     - Filmy nazar & aankhon ke dialogues",
        ".chand     - Modern twist on classic chand lines",
        ".bc        - Savage & funny desi reply command",
        # --- Rare & Epic Pranks ---
        ".fakechat  - Fake chat prank generator",
        ".matrix    - Matrix hacker style animation",
        ".ego       - Pure ego & attitude drop",
        ".radar     - Funny scanning radar animation",
        ".system    - High-tech system overload prank",
        ".aajkal    - Savage reality check shayari",
        # --- Advanced Animations ---
        ".scanner   - Biometric high-tech scanner animation",
        ".quantum   - Sci-fi quantum wormhole animation",
        ".meteor    - Meteor impact & earth quake animation",
        ".nuclear   - Nuclear missile launch sequence animation",
        ".casino    - Casino slot machine jackpot animation",
        # --- Gang Roasts & Vibe Commands ---
        ".jk        - Sad / deep shayaris",
        ".bila      - Romantic shayari vibe for Bila",
        ".satya     - Berozgari & reality comedy",
        ".fly       - Funny roast for friend girl",
        ".aaro      - Safe & funny roast for Aaro",
        ".aryan     - Aryan bhai dialogue & funny lines",
        ".dala      - Funny roast line for Dala",
        ".kunal     - Pure funny roast for Kunal",
        # --- Utility & Moderation Commands ---
        "/whois     - Get detailed user profile information",
        "/common    - Find mutual/common info with a user",
        "/ocr       - Extract text from an uploaded image",
        "/cpright   - Copyright detection & auto-strike moderation"
    ]
    description = "Mega collection of desi swag, flirt lines, massive animations, gang roasts, utilities and copyright moderation"
    add_handler("mega_ultimate_master", commands, description)

async def edit_or_reply(event, text):
    try:
        return await event.edit(text)
    except Exception:
        return await event.reply(text)


# ==================== UTILITY & MODERATION COMMANDS ====================

@CipherElite.on(events.NewMessage(pattern=r"^/whois$", outgoing=True))
@rishabh()
async def whois_command(event):
    if event.fwd_from: return
    if not event.is_reply:
        await edit_or_reply(event, "⚠️ Kisi user ke message par reply karke `/whois` type karein!")
        return
    
    reply_msg = await event.get_reply_message()
    try:
        user_full = await event.client(GetFullUserRequest(reply_msg.sender_id))
        user = user_full.user
        bio = user_full.about or "Not Available"
        
        info = (
            f"👤 **User Information Overview**\n\n"
            f"• **Name:** {user.first_name or 'None'}\n"
            f"• **Username:** @{user.username if user.username else 'None'}\n"
            f"• **User ID:** `{user.id}`\n"
            f"• **Bio:** {bio}\n"
            f"• **Bot:** {'Yes' if user.bot else 'No'}"
        )
        await edit_or_reply(event, info)
    except Exception as e:
        await edit_or_reply(event, f"❌ Error fetching user info: `{str(e)}`")

@CipherElite.on(events.NewMessage(pattern=r"^/common$", outgoing=True))
@rishabh()
async def common_command(event):
    if event.fwd_from: return
    if not event.is_reply:
        await edit_or_reply(event, "⚠️ Kisi user ke message par reply karke `/common` type karein!")
        return
    
    reply_msg = await event.get_reply_message()
    try:
        user_full = await event.client(GetFullUserRequest(reply_msg.sender_id))
        common_chats = user_full.common_chats_count
        await edit_or_reply(event, f"🔗 **Common Chats Count:** Is user ke sath aapke **{common_chats}** mutual/common groups hain.")
    except Exception as e:
        await edit_or_reply(event, f"❌ Error: `{str(e)}`")

@CipherElite.on(events.NewMessage(pattern=r"^/ocr$", outgoing=True))
@rishabh()
async def ocr_command(event):
    if event.fwd_from: return
    if not event.is_reply:
        await edit_or_reply(event, "⚠️ Kisi image par reply karke `/ocr` type karein!")
        return
    
    reply_msg = await event.get_reply_message()
    if not reply_msg.media:
        await edit_or_reply(event, "⚠️ Ye message image nahi hai!")
        return

    await edit_or_reply(event, "🔍 Processing OCR...")
    img_path = await event.client.download_media(reply_msg)
    
    try:
        import pytesseract
        from PIL import Image
        text = pytesseract.image_to_string(Image.open(img_path))
        if not text.strip():
            await edit_or_reply(event, "❌ Image mein koi readable text nahi mila!")
        else:
            await edit_or_reply(event, f"✅ **Extracted Text:**\n\n`{text.strip()}`")
    except Exception as e:
        await edit_or_reply(event, f"❌ OCR Error: `{str(e)}`")
    finally:
        if os.path.exists(img_path):
            os.remove(img_path)

@CipherElite.on(events.NewMessage(incoming=True))
async def copyright_detector(event):
    if not event.chat_id: return
    
    flagged_keywords = ["dmca copy", "pirated link", "copyrighted content"]
    text_content = event.raw_text.lower()
    
    is_flagged = any(word in text_content for word in flagged_keywords)
    
    if is_flagged:
        sender_id = event.sender_id
        if not sender_id: return
        
        cpright_strikes[sender_id] = cpright_strikes.get(sender_id, 0) + 1
        strikes = cpright_strikes[sender_id]
        
        try:
            await event.delete()
            
            if strikes >= 3:
                banned_rights = ChatBannedRights(until_date=None, send_messages=True)
                await event.client(EditBannedRequest(event.chat_id, sender_id, banned_rights))
                await event.client.send_message(
                    event.chat_id, 
                    f"🚨 **Copyright Strike 3 Reached!** User ko baar-baar copyright violation karne par mute kar diya gaya hai. ❌"
                )
            else:
                await event.client.send_message(
                    event.chat_id, 
                    f"⚠️ **Copyright Warning ({strikes}/3):** Yeh content copyright-protected hai! Message delete kar diya gaya hai."
                )
        except Exception as e:
            print(f"Copyright moderation error: {e}")


# ==================== DESI & SWAG COMMANDS ====================

@CipherElite.on(events.NewMessage(pattern=r"^\.gym$", outgoing=True))
@rishabh()
async def gym_command(event):
    if event.fwd_from: return
    steps = [
        "💪 Pre-workout chalu...",
        "🏋️‍♂️ Heavy weight deadlifts utha rahe hain...",
        "🔥 Biceps vein pop ho gayi!",
        "🦍 No Pain, No Gain! Asli mard lohe se khelte hain! 💪⚡"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.5)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.hustle$", outgoing=True))
@rishabh()
async def hustle_command(event):
    if event.fwd_from: return
    lines = [
        "🌙 Raat lambi hai, sapne bade hain aur mehnat 24/7 chalu hai! 💼🔥",
        "Paisa bolta hai aur bhai ka kaam bolta hai! 💸🚀",
        "Competition se hum nahi darte, kyunki hum khud ek standard hain! 🦁👑",
        "Sona band, sirf empire build karna hai! 📈💪"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.bike$", outgoing=True))
@rishabh()
async def bike_command(event):
    if event.fwd_from: return
    steps = [
        "🔑 Key lagayi, ignition on...",
        "🏍️ Exhaust ki aawaz gunji...",
        "💨 Gear dala aur top speed par nikal liye!",
        "🌪️ 'Riders don't fly, they stay low to the ground!' 🛣️🔥"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.5)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.bhai$", outgoing=True))
@rishabh()
async def bhai_command(event):
    if event.fwd_from: return
    lines = [
        "Bhai apna bhai hai, chahe samne poori duniya khadi ho! 🤝🔥",
        "Dosti aisi honi chahiye ki dushman bhi kahe—'Inke beech mat aana, kat loge!' 🗿⚔️",
        "Bhai ke liye jaan bhi hazir hai, bas pehle bill tera hoga! 😂🍻",
        "Sher akela chalta hai, par jab bhai sath ho toh pura jungle apna hota hai! 🦁👑",
        "Apni yaari ki misaal toh aane wali naslein bhi dengi, bas shart yeh hai ki party tu dega! 🍕🎉",
        "Musibat chahe kitni bhi badi ho, bhai ka dialogue ek hi hota hai—'Chinta mat kar, main hoon na!' 💪✨",
        "Sache dost wahi hote hain jo galti par gaali dein aur mushkil waqt mein sabse pehle khade milein! 🍻👊",
        "Bhai aur bhai ka style kabhi out of fashion nahi hota! 😎⚡"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.dekh$", outgoing=True))
@rishabh()
async def dekh_command(event):
    if event.fwd_from: return
    savage_lines = [
        "Abe oye! Jyada smart banne ki koshish mat kar, kat lega! 🐒🖕",
        "Beta tumse na ho payega, jaa pehle dhoodh pi le! 🍼🥱",
        "Tera level wahan hai jahan hum sochna bhi band kar dete hain! 📉🤫",
        "Bade heavy driver ho bhai, seedhe sadak par ditch mein gir gaye! 🛺💥",
        "Humein mat sikhao ki aage kaise chalna hai, hum apne raste khud banate hain aur dusro ke map phaad dete hain! 🦁🔥",
        "Beta jitni teri net worth hai, utna toh hum mahine ka Wi-Fi bill bhar dete hain! 📶💸",
        "Abe chup reh, teri baatein sunkar lagta hai ki mute button duniya ki sabse best invention hai! 🤐🔇",
        "Humse panga lene se pehle apni aukat check kar liya kar, warna GPS bhi tera pata nahi dhoond payega! 🧭💀",
        "Shakal se innocent aur harkato se joker lagta hai tu! 🤡🎪",
        "Jitna dimag tu dusro ki taang khinchne mein lagata hai, utna laga leta toh aaj tu bhi kahi pahunch gaya hota! 🚶‍♂️📉"
    ]
    await edit_or_reply(event, random.choice(savage_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.roast$", outgoing=True))
@rishabh()
async def roast_command(event):
    if event.fwd_from: return
    roasts = [
        "Bhai jab upar wala akal baant raha tha, toh tu line tod kar momos khane chala gaya tha kya? 🥟😂",
        "Teri baatein sunkar lagta hai ki tera dimag aur phone ka 1% battery ek jaisa hi kaam karta hai! 🪫📉",
        "Tujhe dekh kar lagta hai ki Bhagwan ne bhi 'Draft' me save karke galti se publish kar diya hoga! 🗑️💀",
        "Bhai jab bhagwan akal baant raha tha, toh tu umbrella lekar khada tha ki ek boond bhi dimaag ki andar na jaye! ☂️🤣",
        "Teri shakal dekh kar lagta hai ki mirror ko bhi roz subah tujhe dekhne ke baad apology letter likhna padta hoga! 🪞💀",
        "Tujhe dekh kar lagta hai ki human evolution reverse direction mein chal raha hai! 🐒📉",
        "Bhai tu jab serious baat karta hai na, toh aisi comedy hoti hai jo Kapil Sharma bhi nahi la sakta! 🎤😂",
        "Tere paas dimaag hai ya sirf baal sambhalne ke liye khopdi di hai upar wale ne? 🧠🚫",
        "Bhai tujhe dekh kar ek hi line yaad aati hai—'Koshish karne walon ki haar nahi hoti, par teri koshish dekh kar lagta hai umeed hi chhod deni chahiye!' 📉🔥",
        "Tera confidence dekh kar lagta hai ki confidence aur common sense ka kabhi aamna-saamna hi nahi hua! 🤡✋",
        "Bhai jab tu paida hua tha toh doctor ne tere gharwalo se sorry bola tha ya hospital ka bill maaf kar diya tha? 🏥😂",
        "Tujhe dekh kar lagta hai ki Google bhi search history delete karne ki jagah tera contact block kar deta hoga! 🛑💻",
        "Teri general knowledge dekh kar lagta hai ki school ki kitaabein tune sirf wazan badhane ke liye rakhi thi! 🎒🗿",
        "Bhai tu itna slow hai ki agar tujhe snail race mein daal dein, toh snail bhi peechhe mud kar dekhega ki bhai raste mein kahan so gaya! 🐌💤",
        "Tere dimaag ki loading speed itni slow hai ki 2G network bhi tujhse fast chalta hai! 📶🐢",
        "Tujhe dekh kar lagta hai ki WhatsApp ka 'Delete for Everyone' feature sirf tere messages ke liye hi banaya gaya tha! 📱🗑️"
    ]
    await edit_or_reply(event, random.choice(roasts))

@CipherElite.on(events.NewMessage(pattern=r"^\.paise$", outgoing=True))
@rishabh()
async def paise_command(event):
    if event.fwd_from: return
    lines = [
        "Bhai 500 rupaye dena toh... \nMe: Dekh bhai, dosti apni jagah hai par jeb mein sirf makhi udd rahi hai! 🪰💸",
        "Bank balance dekh kar rona aata hai, lagta hai ab bank hi lootna padega! 🏦🏃‍♂️",
        "Udhaar maangne wale dost ki category mein tera naam top par hai bhai! 😂🤝"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.patli$", outgoing=True))
@rishabh()
async def patli_gali(event):
    if event.fwd_from: return
    steps = [
        "⚠️ Scene tight ho raha hai...",
        "👀 Aas-paas dekha koi nahi hai...",
        "🏃‍♂️ Patli gali pakdi aur rocket ki tarah 9 do 11 ho liye! 🚀💨"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.5)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.bhoot$", outgoing=True))
@rishabh()
async def bhoot_prank(event):
    if event.fwd_from: return
    steps = [
        "👻 Room ki batti gul...",
        "🕯️ Andhera ho gaya...",
        "😱 Bhoot aaya ya teri ex ka message aaya?",
        "🏃‍♂️ Jaan bachao bhai, bhoot se zyada toh ex se darr lagta hai! 💀💨"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.5)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.slap$", outgoing=True))
@rishabh()
async def slap_user(event):
    if event.fwd_from: return
    if event.is_reply:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        target = replied_user.user.first_name or "bhai"
        await edit_or_reply(event, f"👊 Ek rasedaar thappad **{target}** ke gaal par jada! 💥")
    else:
        await edit_or_reply(event, "👊 Hava mein ghusa mara, mood theek ho gaya! 💨")


# ==================== FLIRT & SHAYARI COMMANDS ====================

@CipherElite.on(events.NewMessage(pattern=r"^\.flirt$", outgoing=True))
@rishabh()
async def flirt_command(event):
    if event.fwd_from: return
    lines = [
        "Tumhari smile dekh kar toh Google bhi confuse ho gaya hai ki 'Beautiful' ki definition mein aapki photo lagaye ya meri! 😉🔥",
        "Kya aap WiFi ho? Kyunki jabse aapko dekha hai, ek strong connection feel ho raha hai! 📶❤️",
        "Log kehte hain ki duniya mein har cheez ki koi na koi limit hoti hai, par tum par aakar meri yeh limit khatam ho jaati hai! ✨🌹",
        "Agar khoobsurati ek crime hoti, toh aapko umar-kaid ki saza mil chuki hoti! 🚔😍",
        "Aapki aankhon mein kuch aisi baat hai, ki hum bina piye hi behak jaate hain! 🥂💫",
        "Tumhein dekhte hi mere dil ki speed itni badh gayi hai ki lagta hai abhi charger lagana padega! ⚡💘",
        "Aapka naam dictionary mein hona chahiye, kyunki aapke baad kisi aur ki tareef karne ke liye shabd hi nahi bachte! 📖✨",
        "Suna hai chand zameen par nahi utarta, par lagta hai kisi ne rules tod diye hain! 🌙😍",
        "Tumhari aankhein hain ya Google Maps? Jab bhi dekhta hoon, khud ko khoya hua paata hoon! 🗺️👀",
        "Kya aapke paas band-aid hai? Kyunki jab main aapko dekha, toh gir kar ghutna chhil gaya mera! 🩹😂",
        "Agar pyaar ek exam hota, toh main pakka fail ho jata... kyunki main sirf tumhe hi padhta rehta hoon! 📚❤️",
        "Tumhari ek hasi ke liye toh hum apna pura coding syntax badal sakte hain! 💻🔥",
        "Log coffee peene jaate hain date par, main toh tumhe bas dekhne ke liye hi poora din nikal deta hoon! ☕💫",
        "Aapki battery 1% bhi ho na, tab bhi aapki baatein mere dil ko full charge kar deti hain! 🔋⚡",
        "Aap itni cute ho ki tumhe dekh kar mosquito bhi kaatne se pehle selfie mangta hoga! 🦟📸",
        "Pehle mujhe lagta tha ki taare aasmaan mein hote hain, par jabse tumhe dekha, pata chala woh toh chat par online hain! ✨📱",
        "Tumhari baatein sunkar lagta hai ki sugar ki zaroorat hi nahi hai, profile kholte hi diabetes ho jata hai! 🍬😋",
        "Agar tum 10 rupaye ki Pepsi ho, toh main poora ka poora cold drink factory hoon! 🥤😎",
        "Tumhare sath waqt aise nikal jata hai, jaise Jio ka 1.5GB data raat ke 12 baje se pehle! 📉😂",
        "Tumhe dekh kar ek hi baat yaad aati hai—'Mera dil ye pukaare aaja, mere bas mein ab nahi hai re!' 🎶💖"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.shayari$", outgoing=True))
@rishabh()
async def shayari_command(event):
    if event.fwd_from: return
    shayaris = [
        "Teri adaon ka nasha hi kuch alag hai, \nDil toh chahta hai ki bas tumhe dekhte rahein, \nKambhakht ye waqt bhi tumhare aage aakar ruk jata hai! ⏳💖",
        "Aankhon se aankhon ki baat hoti hai, \nJab tum haste ho toh dil ki har fariyad poori hoti hai! ✨🌹",
        "Na jane kyu tumhe dekhne ke baad kisi aur ko dekhne ka dil hi nahi karta, \nLagta hai khuda ne tumhare alawa sabko draft mein daal diya hai! 📱😂"
    ]
    await edit_or_reply(event, random.choice(shayaris))

@CipherElite.on(events.NewMessage(pattern=r"^\.nazar$", outgoing=True))
@rishabh()
async def nazar_command(event):
    if event.fwd_from: return
    lines = [
        "Nazrein milti hain toh dil dhadakta hai, aur jab aap haste ho toh system hil jata hai! 👀💥",
        "Hum toh bas aapse nazrein chura rahe thay, kambhakht dil ne aapki aankhon mein hi ghar bana liya! 🏡❤️"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.chand$", outgoing=True))
@rishabh()
async def chand_command(event):
    if event.fwd_from: return
    lines = [
        "Log kehte hain chand ka tukda ho aap, par sach toh yeh hai ki chand khud aapka daag chhipane ki koshish karta hai! 🌙😂",
        "Aasmaan ka chand toh sabko dikhta hai, par mera chand toh phone ki screen par chat kar raha hai! 📱💫"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.bc$", outgoing=True))
@rishabh()
async def bc_command(event):
    if event.fwd_from: return
    responses = [
        "Abe kisko yaad kar raha hai bhai, seedhe kaam ki baat kar! 😒🔥",
        "Bole toh aag laga rakhi hai market mein! 😎⚡",
        "Abe chup kar, kitna bolega! 🐒🤫"
    ]
    await edit_or_reply(event, random.choice(responses))


# ==================== RARE & EPIC PRANKS ====================

@CipherElite.on(events.NewMessage(pattern=r"^\.fakechat$", outgoing=True))
@rishabh()
async def fake_chat_prank(event):
    if event.fwd_from: return
    steps = [
        "📱 Opening WhatsApp/Telegram API...",
        "💬 Generating fake conversation...",
        "👤 Target: [Secret Celebrity / Crush]",
        "✅ **Prank Chat Created Successfully!**\n\n_Crush: 'Please ek baar mujhse baat kar lo na! 🥺'_"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.matrix$", outgoing=True))
@rishabh()
async def matrix_rain(event):
    if event.fwd_from: return
    frames = [
        "🟩 01010101 🟩",
        "🟩 11001101 🟩",
        "🟢 HACKING THE MAINFRAME... 🟢",
        "💻 ACCESS GRANTED: WELCOME TO THE MATRIX! 🕶️🔥"
    ]
    event = await edit_or_reply(event, frames[0])
    for frame in frames[1:]:
        await asyncio.sleep(0.5)
        await event.edit(frame)

@CipherElite.on(events.NewMessage(pattern=r"^\.ego$", outgoing=True))
@rishabh()
async def ego_command(event):
    if event.fwd_from: return
    lines = [
        "Humara ego utna hi high hai, jitna tumhari aukat se bahar ka sapna hai! 🦁🔥",
        "Humse jalne wale log bhi kya kamaal ke hain... jalte khud hain aur roshni humari dekhte hain! 😎✨"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.radar$", outgoing=True))
@rishabh()
async def radar_scan(event):
    if event.fwd_from: return
    steps = [
        "📡 Scanning surrounding area...",
        "🔍 Target Locked: [Over-smart friend detected]",
        "⚠️ Warning: High level of nonsense found!",
        "🚨 **Scan Complete:** Dimaag ki kachhi aisi ki taisi ho chuki hai! 📉😂"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.5)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.system$", outgoing=True))
@rishabh()
async def system_overload(event):
    if event.fwd_from: return
    steps = [
        "⚠️ **WARNING:** System Overload Detected!",
        "🔴 Core Temperature: 99°C",
        "💣 Self-Destruct Sequence Initiated... 3",
        "💥 2...",
        "🔥 1...",
        "😎 Bas mazaak tha! System rock solid hai bhai ka! 🚀💪"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.aajkal$", outgoing=True))
@rishabh()
async def aajkal_shayari(event):
    if event.fwd_from: return
    shayaris = [
        "Aajkal ke log pyaar mein itne andhe ho gaye hain ki, flashlight on karke bhi wafa dhoondhte hain! 🔦😂",
        "Zindagi mein do hi cheezein tough hain—pehla code ka bug theek karna, aur doosra bewakoof doston ko samjhana! 🗿🥀"
    ]
    await edit_or_reply(event, random.choice(shayaris))


# ==================== ADVANCED ANIMATIONS ====================

@CipherElite.on(events.NewMessage(pattern=r"^\.scanner$", outgoing=True))
@rishabh()
async def scanner_animation(event):
    if event.fwd_from: return
    steps = [
        "🧬 Initializing Biometric Scanner...",
        "🔍 Scanning Fingerprint / Retina...\n`[░░░░░░░░░░] 20%`",
        "🔍 Analyzing DNA structure...\n`[█████░░░░░] 60%`",
        "🔍 Matching with Criminal Database...\n`[██████████] 100%`",
        "🚨 **ALERT:** 100% Certified Legend (aur thoda pagal) found! 😎🔥"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.quantum$", outgoing=True))
@rishabh()
async def quantum_animation(event):
    if event.fwd_from: return
    steps = [
        "🌀 Opening Quantum Portal...",
        "⚡ Bending Space and Time...",
        "🌌 Entering Hyper-Space Vortex...",
        "✨ **Teleportation Successful!** Hum ab doosri dimension mein hain! 🚀👽"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.meteor$", outgoing=True))
@rishabh()
async def meteor_animation(event):
    if event.fwd_from: return
    steps = [
        "☄️ Meteor detected in outer space...",
        "📉 Descending towards Earth atmosphere fast...",
        "🔥 Burning up due to high friction...",
        "💥 **BOOM!** Massive impact! Dharti hila di bhai ne! 🌋💀"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.nuclear$", outgoing=True))
@rishabh()
async def nuclear_animation(event):
    if event.fwd_from: return
    steps = [
        "☢️ Nuclear Silo Open: Preparing Launch...",
        "🚀 Missile Launched into Orbit... 3",
        "🎯 Target Locked on Enemy Base... 2",
        "🔥 Re-entering Atmosphere... 1",
        "💥 **KABOOM!** Nuclear blast complete! Kuch nahi bacha! 🌋💀"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.casino$", outgoing=True))
@rishabh()
async def casino_animation(event):
    if event.fwd_from: return
    steps = [
        "🎰 Spinning the slot machine...\n`[ 🍒 | 🍋 | 🔔 ]`",
        "🎰 Changing symbols...\n`[ 7️⃣ | 7️⃣ | 🍋 ]`",
        "🎰 Almost there...\n`[ 💎 | 💎 | 🍒 ]`",
        "🎉 **JACKPOT! 7 7 7** Saare paise bhai ke! 💰🔥"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)


# ==================== GANG ROASTS & VIBE COMMANDS (EXPANDED) ====================

@CipherElite.on(events.NewMessage(pattern=r"^\.jk$", outgoing=True))
@rishabh()
async def jk_command(event):
    if event.fwd_from: return
    shayaris = [
        "Jise hum apni jaan maante rahe, wahi humari khamoshi ki wajah ban gaye! 🥀💔",
        "Kitna ajeeb dastoor hai is duniya ka, jise sabse zyada chaho, wahi sabse door chala jata hai! 🌧️😔",
        "Rula diya us shakhs ne mujhe, jisse maine kabhi hansna seekha tha... 🖤📉",
        "Waqt badla, log badle, aur phir pata chala ki hum hi bewakoof thay jo sabko apna samajh बैठे! 🥀🔄",
        "Khamoshi se behter koi jawab nahi hota, aur dard se bada koi ustaad nahi hota! 🖤🤫"
    ]
    await edit_or_reply(event, random.choice(shayaris))

@CipherElite.on(events.NewMessage(pattern=r"^\.bila$", outgoing=True))
@rishabh()
async def bila_command(event):
    if event.fwd_from: return
    bila_lines = [
        "Soniyaa meri jaan, tujhpe fida hai yeh dil mera! ❤️✨",
        "Bila bhai ka andaaz aur romantic vibe kabhi fail nahi hoti! 🌹🔥",
        "Bila ki ek smile par toh poora shehar fida hai, baaki sab toh bas timepass hain! 😉💫",
        "Jab Bila entry maarta hai, toh mahol apne aap romantic ho jata hai! 🎶🌹"
    ]
    await edit_or_reply(event, random.choice(bila_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.satya$", outgoing=True))
@rishabh()
async def satya_command(event):
    if event.fwd_from: return
    satya_lines = [
        "Berozgari ka aalam yeh hai ki ab toh sapne bhi unpaid internship wale aate hain! 📉😂",
        "Kadwa sach toh yeh hai ki hum jitna padhte hain, usse zyada toh phone ki battery drain ho jati hai! 📱🔋",
        "Zindagi mein do hi cheezein hard hain—ek engineering ki padhai, aur doosra Satya ko subah time par uthana! ⏰😴",
        "Satya ki pocket money aur mere phone ka net pack ek sath khatam hota hai! 💸📉"
    ]
    await edit_or_reply(event, random.choice(satya_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.fly$", outgoing=True))
@rishabh()
async def fly_command(event):
    if event.fwd_from: return
    funny_lines = [
        "Oye sun pagli! Tujhse baat karke lagta hai ki bhagwan ne tera dimaag banate waqt coding mein koi bada bug chhor diya tha! 🐒😂",
        "Tujhe dekh kar lagta hai ki duniya ki saari bhootniyain ek taraf aur meri ye dost ek taraf! 👻💀",
        "Fly ka attitude dekh kar lagta hai ki ye aasmaan se nahi, seedhe direct 3ri manzil ke ventilation se giri hai! 🏢😂",
        "Tujhse behes karna matlab apne phone ka data aur dimaag dono barbad karna hai! 📶📉"
    ]
    await edit_or_reply(event, random.choice(funny_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.aaro$", outgoing=True))
@rishabh()
async def aaro_command(event):
    if event.fwd_from: return
    safe_funny_lines = [
        "Aaro se dosti karke ek baat samajh aa gayi, ki duniya mein dimaag kharab karne ke liye alag se dushmano ki zaroorat hi nahi padti! 🐒😂",
        "Aaro tu jab seedhi muh baat karti hai na, toh lagta hai zaroor dal mein kuch kala hai! 🧐✨",
        "Bhagwan ne sabko thoda-thoda dimaag diya hai, par lagta hai Aaro ki baari mein line busy thi! 📱😂"
    ]
    await edit_or_reply(event, random.choice(safe_funny_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.aryan$", outgoing=True))
@rishabh()
async def aryan_command(event):
    if event.fwd_from: return
    aryan_lines = [
        "Aryan bhai ke aage koi bol sakta hai kya? Aawaz hi nahi nikalne dete log darr ke maare! 🗣️🔥",
        "Aryan bhai jab raste par chalte hain, toh gadiyan khud side ho jati hain ki bhai ka mood kharab na ho jaye! 🚗💨😎",
        "Aryan bhai ka confidence dekh kar toh Google bhi confuse ho jata hai ki 'Search' kare ya 'Inse permission le'! 🌐🤔😂"
    ]
    await edit_or_reply(event, random.choice(aryan_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.dala$", outgoing=True))
@rishabh()
async def dala_command(event):
    if event.fwd_from: return
    dala_lines = [
        "Dala bhai ki entry aisi hoti hai jaise bina invitation ke shaadi mein photobomber! 📸😂",
        "Dala bhai jab bolte hain toh lagta hai radio ka FM signal crash ho gaya ho! 📻💥",
        "Dala bhai ka swag dekh kar mohalle ke kutte bhi silence mode par chale jaate hain! 🐕🤫",
        "Dala bhai ka dimaag aur calculator dono ek jaise hain—dono mein error ke alawa kuch nahi milta! 🧮💀",
        "Jab Dala serious hota hai, toh sabse pehlehasne ka man karta hai! 😂🎭"
    ]
    await edit_or_reply(event, random.choice(dala_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.kunal$", outgoing=True))
@rishabh()
async def kunal_command(event):
    if event.fwd_from: return
    kunal_lines = [
        "Kunal bhai ka logic sunkar Newton ne apni teesri law wapas lene ka soch liya tha! 🍎😂",
        "Kunal tu chup hi raha kar, tere bolte hi Wi-Fi ke signals drop hone lagte hain! 📶📉",
        "Kunal ki baaton mein utna hi sach hota hai jitna chips ke packet mein hawa nahi hoti! 🥔💀",
        "Kunal jab gyan baantne baithta hai, toh lagta hai free ka internet khatam hone wala hai! 🌐⏳",
        "Kunal bhai ka style dekh kar local tailoring shop wale bhi kapde silna chhod dete hain! 👔🏃‍♂️"
    ]
    await edit_or_reply(event, random.choice(kunal_lines))
