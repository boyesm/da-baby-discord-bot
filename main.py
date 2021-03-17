import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "da baby" in message.content:
        await message.channel.send('Let\'s Go!')

    if "Da baby" in message.content:
        await message.channel.send('Let\'s Go!')
    
    if "Da Baby" in message.content:
        await message.channel.send('Let\'s Go!')

    if "da Baby" in message.content:
        await message.channel.send('Let\'s Go!')

    if "dababy" in message.content:
        await message.channel.send('Let\'s Go!')

client.run('ODIxODczNDY5NjE5OTYxOTE2.YFKDUA.NzDHznC648FcI3Qp1idDyp4biws')