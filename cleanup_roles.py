import discord

client = discord.Client()
yyaen_id = 95485950833983488
shreeder_id = 161215065926795265
set_your_roles_channel_id = 492305188829265941
wrong_channel_msg = "This isn't #set_your_roles"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == shreeder_id:
        # Night Shreeder
        if "night" in message.content.lower():
            await message.channel.send("gn Shreeder")
    
    if message.content.startswith('$testcleanup'):
        print("Test command called")
        print(message.channel.id)
        await _cleanup_channel(message.channel, True)

    if message.content.startswith('$cleanup'):
        print(message.channel.id)
        if message.channel.id == set_your_roles_channel_id:
            await _cleanup_channel(message.channel, False)
        else:
            await message.channel.send(wrong_channel_msg)
            print(wrong_channel_msg)

async def _cleanup_channel(channel, dryrun):
    async for elem in channel.history():
        if elem.author.id != yyaen_id:
            try:
                if dryrun:
                    print("{} :: {}".format(elem.author, elem.content))
                else:
                    await elem.delete()
            except Exception as e:
                print("Failed to delete msg :: {}".format(e))



def get_credentials():
    with open("config.txt") as f:
        return f.readline()

client.run(get_credentials())