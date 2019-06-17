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
    
    name = "Dice Roller"
    command1 = "**~Roll** (number of dice)**D**(any number of sides)"
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
    if message.content.startswith("~Roll "):
        
        toRoll = message.content[6:]
        
        D = toRoll.index("D")
        
        number = toRoll[:D]
        sides = toRoll[D+1:]
        
        msg = ""
        x = 0
        y = 0

        
        for i in range(int(number)):
            x = random.randint(1,int(sides)+1)
            msg += ":game_die:{} : {}".format(str(i+1),str(x))
            msg += "\n"
            y+=x
        
        msg += "Total : {}".format(str(y))
        
        
        if len(msg) < 700:
            await message.channel.send(msg)
        else:
            await message.channel.send(":scream: please roll less dice, or less sides. We don't want to flood the discord!")



                
                
client.run('NTkwMDIwMTQ3MjYwMTYyMDc5.XQcKSg.52WJ5pBxM4RFIvvV-Wpv2wvdnAs') 

