
import discord
import random

client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')



@client.event
async def on_guild_join(guild):
    
    name = "**🎱 Fortune Teller**"
    command1 = "~8ball (your message here)"
    command2 = ""
    command3 = ""
    command4 = ""
    
    join_message = """Hello {}
    I'm {}, created by b9king#6857 with help from I am Moonslice#4132
    My commands are:
    {}
    You can support my creator here: https://www.patreon.com/b9king
    """.format(guild.name,name,command1)    
    
    x = guild.channels
    y = False
    
    for i in x:
        if i.permissions_for(guild.me).send_messages and not y:
            print(i)
            x = i
            break
    await x.send(join_message)
            
    
    
    #general.permissions_for(guild.me).send_messages:
        #await general.send(join_message)
    
@client.event
async def on_message(message):
    if message.content.startswith("~8ball"):
        eightball = ["it is certain", "it is decidedly so", "without a doubt", "yes-definitely", "you may rely on it", "as I see it, yes","most likely","outlook good","yes","signs point to yes", "reply hazy, try again", "ask again later", "better not tell you now","cannot predict now","concentrate and ask again", "Don't count on it", "My reply is no","my sources say no", "Outlook not so good", "very doubtful"]
        
        message.content = message.content.replace("~8ball", "")
        msg = " 🎱 In regards to '" + message.content + "' " + random.choice(eightball).format(message)
        await message.channel.send(msg)        



                
                
client.run('NTkwMDQ3NDc2ODMzMDU4ODI5.XQci_w.vRIut5pfABulPVpRHH2MjYBT1QA') 

