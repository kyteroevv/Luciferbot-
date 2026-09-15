from telethon import events
import random
from plugins.bot import add_handler
from utils.utils import CipherElite
from utils.decorators import rishabh

def init(client_instance):
    commands = [
        ".dice - Roll a dice",
        ".coin - Flip a coin",
        ".decide - Yes or No decision"
    ]
    description = "Fun plugins for entertainment "
    add_handler("fun", commands, description)

async def register_commands():
    @CipherElite.on(events.NewMessage(pattern=r"\.dice"))
    @rishabh()
    async def dice(event):
        number = random.randint(1, 6)
        dice_emojis = ["", "", "", "", "", ""]
        await event.reply(f" {dice_emojis[number-1]} ({number})")

    @CipherElite.on(events.NewMessage(pattern=r"\.coin"))
    @rishabh()
    async def coin(event):
        coins = ["Heads", "Tails"]
        coin_emoji = ""
        result = random.choice(coins)
        await event.reply(f"{coin_emoji} Coin landed on: **{result}**!")

    @CipherElite.on(events.NewMessage(pattern=r"\.decide"))
    @rishabh()
    async def decide(event):
        decisions = ["Yes", "No", "Maybe", "Definitely", "Never"]
        await event.reply(f" **{random.choice(decisions)}**") 
        
    @CipherElite.on(events.NewMessage(pattern=r"\.cocaine$"))
    @rishabh()
    async def cocaine(event):
        intro = """Name :- Cocaine [ nashe wale name ke logo ke karib rehe ]😗
From :- Swarg log [ koi manta nhi kyu ki sab jalte hai bro] 😂
Education :- Dr. B R ambdkar jesa padha likha hu vro .. 🙂
Hobby :- Sab kr leta hu ..
Current Situation :- gareebi tum sab ne dekhi hogi me bhi dekh hi raha hu ..
Dream :- khud ki dharti bana ni hai 😝"""

        await event.reply(intro) 

