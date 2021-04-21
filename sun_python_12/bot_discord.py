import discord

TOKEN = 'ODMzMjc3OTE4NTY5NDMxMDUw.YHwAiQ.ZyBozximImJuXUKbrGDOmQZvyNs'

# хранится наш бот
client = discord.Client()

@client.event
async def on_message(message):
    print(message)

client.run(TOKEN)
