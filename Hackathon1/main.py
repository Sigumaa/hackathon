import discord
from discord.ext import tasks
from datetime import datetime
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

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

x=[]
y=[]

@tasks.loop(seconds=5)
async def loop():
    n = datetime.now()
    guild = client.get_guild(GUILD_ID)
    for member in guild.members:
        if "online" in member.status:
            if member.id in id:
                y.append(1)
                x.append(n)
        else:
            if member.id in id:
                y.append(0)
                x.append(n)
    if n.hour == 0 and n.minute == 31:
        plt.plot(x, y);
        plt.savefig("a.png")


@client.event
async def on_message(message):

	if message.author.bot:
		return

	if message.content == "!ping":
		await message.channel.send("pong!")


client.run(TOKEN)