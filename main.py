import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from google_images_download import google_images_download
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '-') #put your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    
    
@client.command()
async def count(ctx, number : int):
    await ctx.send(number +1)

@client.command()
async def clear(ctx, number : int):
    await ctx.channel.purge(limit=number+1)   

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

@client.command()
async def stab(ctx, person : discord.Member):
  await ctx.send("Yo" + " " + person.mention + " " + "has been stabbed")
  
@client.command()
async def source(ctx):
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
async def image(ctx, *, text):
  response = google_images_download.googleimagesdownload()
  arguments = {text,"limit":1,"print_urls":True}
  paths = response.download(arguments)
  await ctx.send("{}".format(paths))











  


client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!
