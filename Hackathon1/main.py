import discord
from discord.ext import tasks

f = open("token.txt")
TOKEN = f.read()
f.close()

intents = discord.Intents.default()
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print("logged in\n")
	await client.change_presence(activity=discord.Game(name="Discord", type=1))
	loop.start()

GUILD_ID = 815946801755586570

id = [688227388907323472]

@tasks.loop(seconds=15)
async def loop():
    guild = client.get_guild(GUILD_ID)
    for member in guild.members:
        if "online" in member.status:
            if member.id in id:
                print("on-line")
        else:
            if member.id in id:
                print("off-line")


@client.event
async def on_message(message):

	if message.author.bot:
		return

	if message.content == "!ping":
		await message.channel.send("pong!")


client.run(TOKEN)