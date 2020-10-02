import discord

client = discord.Client()
yyaen_id = 95485950833983488
set_your_roles_channel_id = 492305188829265941
wrong_channel_msg = "This isn't #set_your_roles"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$testcleanup'):
        print("Test command called")
        print(message.channel.id)
        if message.channel.id == set_your_roles_channel_id:
            async for elem in message.channel.history():
                if elem.author.id != yyaen_id:
                    try:
                        print("{} :: {}".format(elem.author, elem.content))
                    except:
                        continue
        else:
            await message.channel.send(wrong_channel_msg)
            print(wrong_channel_msg)

    if message.content.startswith('$cleanup'):
        print(message.channel.id)
        if message.channel.id == set_your_roles_channel_id:
            async for elem in message.channel.history():
                if elem.author.id != yyaen_id:
                    try:
                        await elem.delete()
                    except Exception as e:
                        print("Failed to delete message :: {}".format(e))
                        continue
        else:
            await message.channel.send(wrong_channel_msg)
            print(wrong_channel_msg)

def get_credentials():
    with open("config.txt") as f:
        return f.readline()

client.run(get_credentials())