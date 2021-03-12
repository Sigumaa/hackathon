import discord

f = open("token.txt")
token = f.read()
f.close()

client = discord.Client()

@client.event
async def on_ready():
    print("logged in as " + client.user.name)


client.run(token)