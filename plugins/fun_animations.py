# =============================================================================
#  CipherElite Userbot Plugin
#
#  Plugin Name:    fun_animations
#  Author:         CipherElite Dev (@rishabhops)
#  Repository:     https://github.com/rishabhops/CipherElite
#
#  LICENSE:        MIT
# =============================================================================

import asyncio
import random
from collections import deque
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from utils.utils import CipherElite
from utils.decorators import rishabh
from plugins.bot import add_handler

DEFAULTUSER = "Elite User"

def init(client):
    """Initialize the fun_animations plugin"""
    commands = [
        ".gym      - Gym motivation & biceps flex",
        ".hustle   - Late night hustle & money mindset",
        ".bike     - Rider attitude & speed vibe",
        ".bhai     - Jigri dost ke liye dialogue",
        ".dekh     - Savage reply to haters",
        ".roast    - Dost ki taang khinchne ke liye",
        ".paise    - Jeb khali hone ka dukh",
        ".patli    - Mauka dekh kar 9 do 11 hona",
        ".bhoot    - Bhoot / Ex prank animation",
        ".slap     - Solid thappad action",
        ".mind     - Brain cleanup sequence",
        ".explode  - Explosive animation",
        ".dial     - Simulate a call to a VIP",
        ".zap      - Zap someone with a fun animation",
        ".joke     - Tell a random funny joke"
    ]
    description = "Desi swag and fun animations for chats"
    add_handler("fun_animations", commands, description)

async def edit_or_reply(event, text):
    try:
        return await event.edit(text)
    except Exception:
        return await event.reply(text)

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
        "Sher akela chalta hai, par jab bhai sath ho toh pura jungle apna hota hai! 🦁👑"
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
        "Bade heavy driver ho bhai, seedhe sadak par ditch mein gir gaye! 🛺💥"
    ]
    await edit_or_reply(event, random.choice(savage_lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.roast$", outgoing=True))
@rishabh()
async def roast_command(event):
    if event.fwd_from: return
    roasts = [
        "Bhai jab upar wala akal baant raha tha, toh tu line tod kar momos khane chala gaya tha kya? 🥟😂",
        "Teri baatein sunkar lagta hai ki tera dimag aur phone ka 1% battery ek jaisa hi kaam karta hai! 🪫📉",
        "Tujhe dekh kar lagta hai ki Bhagwan ne bhi 'Draft' me save karke galti se publish kar diya hoga! 🗑️💀"
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

@CipherElite.on(events.NewMessage(pattern=r"^\.mind$", outgoing=True))
@rishabh()
async def mind(event):
    if event.fwd_from: return
    event = await edit_or_reply(event, "🧠 Processing...")
    chars = ["🧠 MIND RESET 🚀", "🧠 <(•_•)> 💨", "🧠 CLEARED! ✨ Ready to rock!"]
    for char in chars:
        await asyncio.sleep(0.8)
        await event.edit(char)

@CipherElite.on(events.NewMessage(pattern=r"^\.explode$", outgoing=True))
@rishabh()
async def explode(event):
    if event.fwd_from: return
    event = await edit_or_reply(event, "💥 Preparing explosion...")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣\n💥💥💥💥")
    await asyncio.sleep(0.5)
    await event.edit("💥 **BOOM!** Everything's gone! 😎")

@CipherElite.on(events.NewMessage(pattern=r"^\.dial$", outgoing=True))
@rishabh()
async def dial(event):
    if event.fwd_from: return
    event = await edit_or_reply(event, "📞 Dialing VIP...")
    await asyncio.sleep(1)
    await event.edit(f"📞 Connected with VIP!\nMe: Yo, it's {DEFAULTUSER}! 😎")

@CipherElite.on(events.NewMessage(pattern=r"^\.zap$", outgoing=True))
@rishabh()
async def zap(event):
    if event.fwd_from: return
    if not event.reply_to_msg_id:
        await edit_or_reply(event, "⚡ Reply to a user to zap them!")
        return
    reply_message = await event.get_reply_message()
    replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
    name = replied_user.user.first_name or "Unknown"
    await edit_or_reply(event, f"⚡ Zapping {name}...\n🔥 **{name} is toast!** 😜")

@CipherElite.on(events.NewMessage(pattern=r"^\.joke$", outgoing=True))
@rishabh()
async def tell_joke(event):
    if event.fwd_from: return
    jokes = [
        "Pati: Tum jab gusse mein hoti ho toh aur bhi khoobsurat lagti ho...\nPatni: Sachhi? 😊\nPati: Nahi, mujhe pagal kutte ki tarah lagti ho! 🐕😂",
        "Teacher: Kal school kyun nahi aaye the?\nStudent: Sir, raste mein ek board laga tha 'Aage School hai, Dheere Chalein' toh dheere-dheere chalte pahucha toh chutti ho gayi thi! 🏫🚶‍♂️",
        "Santa: Meri biwi mujhe har jagah dhundhti hai.\nBanta: Pyar karti hai bhai!\nSanta: Pyar nahi, shak hai ki main momos na kha raha hoon! 🥟😂"
    ]
    await edit_or_reply(event, random.choice(jokes))
    
