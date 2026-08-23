# =============================================================================
#  CipherElite Userbot Plugin - Mega Ultimate Master File (All-in-One)
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
    """Initialize the mega all-in-one plugin"""
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
        ".wifi      - WiFi signal hack & disconnect animation",
        ".ghost     - Ghost mode invisibility animation",
        # --- Classic Animations ---
        ".mind      - Brain cleanup sequence",
        ".explode   - Explosive animation",
        ".dial      - Simulate a call to a VIP",
        ".zap       - Zap someone with a fun animation",
        ".joke      - Tell a random funny joke"
    ]
    description = "Mega collection of all desi swag, flirt lines, massive animations and auto-tag responder"
    add_handler("mega_ultimate_master", commands, description)

async def edit_or_reply(event, text):
    try:
        return await event.edit(text)
    except Exception:
        return await event.reply(text)


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
        "Tumhe paane ke liye dua toh nahi ki, par jab se tum mile ho, har dua mein bas tumhara hi naam aata hai! 🤲❤️",
        "Suna hai ki pyaar andha hota hai... par jabse tumhein dekha hai, mujhe sab kuch bilkul saaf-saaf dikhne laga hai! 👀✨",
        "Tumhe dekh kar lagta hai ki khuda ne aaj koi aur kaam nahi kiya hoga, bas tumhe banane mein poori jaan laga di hogi! 🎨💖",
        "Aapka gussa bhi itna pyaara lagta hai ki dil karta hai baar-baar koi galti karte rahein! 🤭⚡",
        "Zindagi ke safar mein humein hazaron log mile, par aap jaisa 'bug' kisi ke code mein nahi mila jo seedha dil mein fix ho jaye! 💻💘",
        "Tumhari awaz sunkar aisa lagta hai jaise koi soothing playlist chal rahi ho jo kabhi khatam na ho! 🎶🌹",
        "Apni aakhon se keh do ki humara peecha chhor dein, warna humein bhi aapse pyaar karne ki aadat ho jayegi! 😉✨",
        "Tumhe dekhne ke baad mujhe kisi aur ki taraf dekhne ki zaroorat hi nahi padti, kyunki mera saara focus tum par hi lock ho jata hai! 🎯❤️",
        "Tumhari baatein sunkar aisa lagta hai ki jaise koi khubsurat novel padh raha hoon jiska ant kabhi aaye hi na! 📖💫",
        "Suno... tumse baat karke na ek alag hi sukoon milta hai, jaise poore din ki thakaan ek hi pal mein gayab ho gayi ho! ✨❤️",
        "Tumhari har ek baat mein koi toh aisi jaadui baat hai, jo mujhe baar-baar tumhari taraf kheench leti hai! 😉🌹"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.shayari$", outgoing=True))
@rishabh()
async def shayari_command(event):
    if event.fwd_from: return
    shayaris = [
        "Teri adaon ka nasha hi kuch alag hai, \nDil toh chahta hai ki bas tumhe dekhte rahein, \nKambhakht ye waqt bhi tumhare aage aakar ruk jata hai! ⏳💖",
        "Aankhon se aankhon ki baat hoti hai, \nJab tum haste ho toh dil ki har fariyad poori hoti hai! ✨🌹",
        "Na jane kyu tumhe dekhne ke baad kisi aur ko dekhne ka dil hi nahi karta, \nLagta hai khuda ne tumhare alawa sabko draft mein daal diya hai! 📱😂",
        "Tumhari khamoshi bhi ek geet lagti hai, \nAur tumhara har ek andaz mujhe apni taraf kheenchta hai! 🎶💫",
        "Fursat mein jab kabhi khuda ne tumhe banaya hoga, \nUsne bhi socha hoga ki aaj apni sabse khoobsurat masterpiece zameen par utaar raha hoon! 🎨❤️",
        "Tujhse milne ke baad yeh samajh aaya, \nKi khushiyon ke liye daulat ki nahi, bas ek pyare chehre ki zaroorat hoti hai! 🌟🥰",
        "Lafzon ki talash mein hum kahan kahan gaye, \nPar jab aap samne aaye, toh hum saare lafz bhool gaye! 📜❤️",
        "Kitni ajeeb baat hai na, \nHum duniya bhar ki baatein yaad rakhte hain, \nPar jab tum samne aate ho toh sirf tumhara chehra yaad rehta hai! 🌙💭",
        "Dhadkano ko bhi ab teri aadat ho gayi hai, \nJab bhi tu online aati hai, ye dil bina notification ke hi buzz karne lagta hai! 💓📱",
        "Raat ki tanhai mein jab chand se baat hoti hai, \nKasam se, wahi baat phir tumhare sath hoti hai! ✨🌌",
        "Zindagi ke har mod par tera sath chahiye, \nTu mile ya na mile, par teri yaadon ka yeh khubsurat ehsaas hamesha paas chahiye! 🌹🤝"
    ]
    await edit_or_reply(event, random.choice(shayaris))

@CipherElite.on(events.NewMessage(pattern=r"^\.nazar$", outgoing=True))
@rishabh()
async def nazar_command(event):
    if event.fwd_from: return
    lines = [
        "Nazrein milti hain toh dil dhadakta hai, aur jab aap haste ho toh system hil jata hai! 👀💥",
        "Hum toh bas aapse nazrein chura rahe thay, kambhakht dil ne aapki aankhon mein hi ghar bana liya! 🏡❤️",
        "Aapki ek jhalak ke liye humne apne sare important kaam chhor rakhe hain! 😍⏳",
        "Nazar jo tumse mili toh yeh pata chala, ki khoobsurati sirf kitabon mein nahi, saamne bhi baithi hoti hai! 📖✨",
        "Tumhari ek nazar ke liye hum zamane se lad sakte hain, bas shart yeh hai ki tum humari taraf dekho! 🛡️❤️"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.chand$", outgoing=True))
@rishabh()
async def chand_command(event):
    if event.fwd_from: return
    lines = [
        "Log kehte hain chand ka tukda ho aap, par sach toh yeh hai ki chand khud aapka daag chhipane ki koshish karta hai! 🌙😂",
        "Aasmaan ka chand toh sabko dikhta hai, par mera chand toh phone ki screen par chat kar raha hai! 📱💫",
        "Chand ko bhi guroor tha ki uske paas noor hai, phir maine aapki profile pic dikha di aur wo chup ho gaya! 🌌🔥",
        "Log chand ko dekh kar eid manate hain, aur hum aapko dekh kar har din celebrate karte hain! 🌙🎉"
    ]
    await edit_or_reply(event, random.choice(lines))

@CipherElite.on(events.NewMessage(pattern=r"^\.bc$", outgoing=True))
@rishabh()
async def bc_command(event):
    if event.fwd_from: return
    responses = [
        "Abe kisko yaad kar raha hai bhai, seedhe kaam ki baat kar! 😒🔥",
        "Bole toh aag laga rakhi hai market mein! 😎⚡",
        "Abe chup kar, kitna bolega! 🐒🤫",
        "Bhai ka naam hi kaafi hai is field mein! 🦁👑",
        "Suna hai tu aajkal kuch zyada hi ud raha hai? Niche utar aa! 🛬😂"
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
        "Humse jalne wale log bhi kya kamaal ke hain... jalte khud hain aur roshni humari dekhte hain! 😎✨",
        "Sher ki bhook aur humara attitude kabhi kam nahi hota! 🗿👑"
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
        "Zindagi mein do hi cheezein tough hain—pehla code ka bug theek karna, aur doosra bewakoof doston ko samjhana! 🗿🥀",
        "Pehle log dil se baat karte the, aajkal log sirf Wi-Fi range ke hisaab se rishte rakhte hain! 📶💀"
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
        "🎉 **JACKPOT!** Tune saare paise jeet liye! (Par virtual wale) 💰😎"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.wifi$", outgoing=True))
@rishabh()
async def wifi_animation(event):
    if event.fwd_from: return
    steps = [
        "📶 WiFi Signal: Strong [████]",
        "📉 Intercepting router frequency... [██░░]",
        "⚠️ Changing DNS and IP address...",
        "❌ **Connection Lost!** Router ka connection uchaal diya gaya hai! 🛜💥"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)

@CipherElite.on(events.NewMessage(pattern=r"^\.ghost$", outgoing=True))
@rishabh()
async def ghost_animation(event):
    if event.fwd_from: return
    steps = [
        "👻 Activating Ghost Protocol...",
        "🕶️ Hiding IP and digital footprint...",
        "🌫️ Disappearing from public networks...",
        "🥷 **GHOST MODE ENABLED:** Ab hum invisible hain! Koi trace nahi milega! 👻💨"
    ]
    event = await edit_or_reply(event, steps[0])
    for step in steps[1:]:
        await asyncio.sleep(0.6)
        await event.edit(step)


# ==================== CLASSIC ANIMATIONS ====================

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


# ==================== AUTO MENTION RESPONDER ====================

@CipherElite.on(events.NewMessage(incoming=True))
async def mention_responder(event):
    if event.is_group and event.mentioned:
        dosti_roast_replies = [
            "Abe kisne yaad kiya mujhe? Thoda sabar kar, ya dimaag kharab ho gaya hai tera? 😂🔥",
            "Bhai bina wajah tag mat kar, pehle apne level ka koi dhoondh le! 🥱💀",
            "Suna hai tu mujhe yaad kar raha tha? Ja pehle thanda paani pi le! 🧊😂",
            "Abe oye, tag karne ki aadat chhor de warna block karne mein 2 second lagenge! 🚫⚡",
            "Tera message mil gaya, ab zyada oversmart mat ban, jaake chup-chap baith ja! 🐒🤫",
            "Naam mat le, direct samne aakar baat kar na! 😎🦁",
            "Lagta hai aaj tera dimaag phir se ghutne mein chala gaya hai jo mujhe tag kar raha hai! 🤡📉",
            "Itna pyaar kyon aa raha hai bhai? Kahin mujhse koi kaam toh nahi nikalwana? 🤨💸"
        ]
        await event.reply(random.choice(dosti_roast_replies))
