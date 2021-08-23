import discord
import os
import time
import aiohttp
import json
import io
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from discord_slash import SlashCommand, SlashContext
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '-') #put 
slash = SlashCommand(client, sync_commands=True)

#your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
@slash.slash(name="update1", description="this command is only for updating the bot")    
async def slashupdate(ctx):
   await ctx.send("Why did you use it?")


@client.command()
async def count(ctx, number : int):
    await ctx.send(number +1)

@client.command()
async def clear(ctx, number : int):
    await ctx.channel.purge(limit=number+1)   

@slash.slash(name="clear", description="clears messages")
async def slashclear(ctx, number : int):
    await ctx.channel.purge(limit=number+1)
    await ctx.send("Deleted messages")
    time.sleep(3)
    await ctx.channel.purge(limit=1)

@client.command()
async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

@client.command()
async def say(ctx, *, text):
 await ctx.channel.purge(limit=1)
 await ctx.send(text)

@slash.slash(name="say", description="say")
async def slashsay(ctx, *, text):
  await ctx.send(text)
  
@client.command()
async def stab(ctx, person : discord.Member):
  await ctx.send("Yo" + " " + person.mention + " " + "has been stabbed")
  
@client.command()
async def source(ctx):
  await ctx.send("https://github.com/Phoneguytech75/PhoneguyBot")

@slash.slash(name="Source", description="sends the source code link to the server")
async def slashsource(ctx):
  await ctx.send("https://github.com/Phoneguytech75/PhoneguyBot")



@client.command()
async def server(ctx):
  await ctx.send("https://discord.gg/vFrsNYxz3G")

@client.command()
async def vote(ctx):
  await ctx.send("https://top.gg/bot/852619132138160148")

@client.command()
async def commands(ctx):
  with open('commands.txt', 'r') as cmds:
    embed=discord.Embed(title="Commands List",
    description=cmds.read(),color=0xc93bf5)
    await ctx.send(embed=embed)

@slash.slash(name="Commands", description="shows the list of Commands")
async def slashcommands(ctx):
  with open('commands.txt', 'r') as cmds:
    embed=discord.Embed(title="Commands List",
    description=cmds.read(),color=0xc93bf5)
    await ctx.send(embed=embed)


@client.command()
async def update(ctx):
  with open('commands.txt', 'r') as cmds:
    embed=discord.Embed(title="Commands List",
    description=cmds.read(),color=0xc93bf5)
    await ctx.channel.purge(limit=2)
    await ctx.send(embed=embed)

@client.command()
async def avatar(ctx, member : discord.Member):
  await ctx.channel.purge(limit=1) 
  await ctx.send("{}".format(member.avatar_url))


@client.command()
async def toprole(ctx, member : discord.Member):
  await ctx.send(member.top_role)
  

@client.command()
async def football(ctx):
  with open('output.txt', 'r') as fp:
     await ctx.send(fp.read())

@client.command()
async def trigger(ctx, member : discord.Member):
  async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
         imageData = io.BytesIO(await trigImg.read())
         await trigSession.close()
         await ctx.send(file=discord.File(imageData, 'triggered.gif'))

@slash.slash(name="Trigger", description="trigger someone")
async def slashtrigger(ctx, member : discord.Member):
  async with aiohttp.ClientSession() as trigSession:
        async with trigSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format="png", size=1024)}') as trigImg:
         imageData = io.BytesIO(await trigImg.read())
         await trigSession.close()
         await ctx.send(file=discord.File(imageData, 'triggered.gif'))      
        
@client.command()
async def wasted(ctx, member : discord.Member):
  async with aiohttp.ClientSession() as wasSession:
        async with wasSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as wasImg
         imageData = io.BytesIO(await wasImg.read())
         await wasSession.close()
         await ctx.send(file=discord.File(imageData, 'wasted.gif'))    
        
@client.command()
async def simp(ctx, member : discord.Member):
  async with aiohttp.ClientSession() as simpSession:
        async with simpSession.get(f'https://some-random-api.ml/canvas/simpcard?avatar={member.avatar_url_as(format="png", size=1024)}') as simpImg:
         imageData = io.BytesIO(await simpImg.read())
         await simpSession.close()
         await ctx.send(file=discord.File(imageData, 'anime.png'))
        
@client.command()
async def passed(ctx, member : discord.Member):
  async with aiohttp.ClientSession() as passSession:
        async with passSession.get(f'https://some-random-api.ml/canvas/passed?avatar={member.avatar_url_as(format="png", size=1024)}') as passImg:
         imageData = io.BytesIO(await passImg.read())
         await passSession.close()
         await ctx.send(file=discord.File(imageData, 'passed.gif'))         

client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!
