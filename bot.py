# bot.py
import asyncio
from datetime import datetime
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    date_of_message = datetime.today().strftime('%d/%m/%Y')

    for guild in client.guilds:
        YTrole = None
        for role in guild.roles:
            if role.name == 'premiumYT':
                TYrole = role
            
        if TYrole is not None:
            for mem in TYrole.members:
                await mem.send('págame cerda. -Eros, ' + date_of_message)
    await client.close()

async def main():
    await client.start(TOKEN)

asyncio.run(main())