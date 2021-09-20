import discord
import os
import time
import aiohttp
import http.client
import json
import requests
from random import random
import io
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
from discord_slash import SlashCommand, SlashContext
from ssa_wrapper import *
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '-') #put 
slash = SlashCommand(client, sync_commands=True)
football_api = os.getenv("FOOTBALL")
unsplash = os.getenv("UNSPLASH")
api_football = os.getenv("API_FOOTBALL")
#your own prefix here


def ani_quote():
    response = requests.get("https://some-random-api.ml/animu/quote")
    json_data = json.loads(response.text)
    quote = json_data["sentence"]
    return(quote)

def ani_wink():
    response = requests.get("https://some-random-api.ml/animu/wink")
    json_data = json.loads(response.text)
    img = json_data[f"link"]
    return(img)




@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online
    game = discord.Game('Epic Bot')
    await client.change_presence(status=discord.Status.online, activity=game)
    
@slash.slash(name="update4", description="this command is only for updating the bot")    
async def slashupdate(ctx):
   await ctx.send("Why did you use it?")

@client.command()
async def hello(ctx):
    url = requests.get('https://phoneguyapi.herokuapp.com/test')
    json_data = json.loads(url.text)
    await ctx.send(json_data)



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
        async with wasSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format="png", size=1024)}') as wasImg:
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
        
@client.command()
async def aniquote(ctx):
    response = requests.get("https://some-random-api.ml/animu/quote")
    json_data = json.loads(response.text)
    quote = json_data["sentence"]
    anime = json_data["anime"]
    await ctx.send(f'{sentence} -- {anime}')
        
@slash.slash(name="aniquote", description="gets a random quote from an anime")
async def slashaniquote(ctx):
    response = requests.get("https://some-random-api.ml/animu/quote")
    json_data = json.loads(response.text)
    quote = json_data["sentence"]
    anime = json_data["anime"]
    await ctx.send(f'{sentence} -- {anime}')

@client.command()
async def aniwink(ctx):
    outputwink = ani_wink()
    await ctx.send(outputwink)
        
@slash.slash(name="aniwink", description="shows a gif of an anime character winking")
async def slashaniwink(ctx):
    outputwink = ani_wink()
    await ctx.send(outputwink)

@client.command()
async def meme(ctx):
    response = requests.get('https://meme-api.herokuapp.com/gimme/memes')
    json_data = json.loads(response.text)
    r_title = json_data['title']
    r_img = json_data['url']
    r_postlink = json_data['postLink']
    embed = discord.Embed(title=r_title, url=r_postlink)
    embed.set_image(url=r_img)
    await ctx.send(embed=embed)
    
@slash.slash(name='Matchday', description='Gets a match on the match day')
async def league(ctx, *, league, matchday, number : int):
 connection = http.client.HTTPConnection('api.football-data.org')
 headers = { 'X-Auth-Token': football_api }
 connection.request('GET', f'/v2/competitions/{league}/matches?matchday={matchday}', None, headers )
 response = json.loads(connection.getresponse().read().decode())
 away = response['matches'][number]['awayTeam']['name']
 home = response['matches'][number]['homeTeam']['name']
 await ctx.send(f'{away} vs {home}')  

@client.command()
async def topscorer(ctx):
     connection = http.client.HTTPConnection('api.football-data.org')
     headers = { 'X-Auth-Token': football_api }
     connection.request('GET', '/v2/competitions/PL/scorers?limit=1', None, headers )
     response = json.loads(connection.getresponse().read().decode())
     name = response['scorers'][0]['player']['firstName']
     team = response['scorers'][0]['team']['name']
     await ctx.send(f'{name}  from  {team}')
        
@slash.slash(name='FirstMatch', description='Gets the first match of a team')
async def firstmatch(ctx, *, team):
     connection = http.client.HTTPConnection('api.football-data.org')
     headers = { 'X-Auth-Token': football_api }
     connection.request('GET', f'/v2/teams/{team}/matches?status=SCHEDULED&limit=1', None, headers )
     response = json.loads(connection.getresponse().read().decode())
     away = response['matches'][0]['awayTeam']['name']
     home = response['matches'][0]['homeTeam']['name']
     await ctx.send(f'{away}  vs  {home}')

@slash.slash(name='footsearch', description='searches a football team')
async def search(ctx, *, team):
    true_team = team.replace(' ', '%20')
    conn = http.client.HTTPSConnection("v3.football.api-sports.io")
    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': api_football
    }

    conn.request("GET", f"/teams?search={true_team}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    real_data = json.loads(data)
    name = real_data['response'][0]['team']['name']
    id = real_data['response'][0]['team']['id']
    logo = real_data['response'][0]['team']['logo']
    founded = real_data['response'][0]['team']['founded']
    embed = discord.Embed(title=name)
    embed.set_image(url=logo)
    embed.add_field(name='id:', value=id)
    embed.add_field(name='Founded:', value=founded)
    await ctx.send(embed=embed)
        
        
@client.command()
async def leagues(ctx):
    with open('football.txt', 'r') as foot:
     embed=discord.Embed(title="Leagues List",
     description=foot.read(),color=0xc93bf5)
     await ctx.send(embed=embed)

@client.command()
async def image(ctx, *, search):
    key = unsplash
    url = requests.get(f'https://api.unsplash.com/photos/random?query={search}&orientation=landscape&client_id={key}')
    json_data = json.loads(url.text)
    image = json_data['urls']['regular']
    unsplash_image = json_data['links']['html']
    name = json_data['user']['first_name']
    name_link = json_data['user']['links']['html']
    embed = discord.Embed(title='Image from Unsplash', url=unsplash_image)
    embed.set_image(url=image)
    embed.add_field(name='Image By', value=f'{name} - {name_link}')
    await ctx.send(embed=embed)
    
@client.command()
async def mute(ctx, member : discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f'Muted {member}')
    else:
        await member.add_roles(role)
        await ctx.send(f'Muted {member}')
        
@slash.slash(name='mute', description='Make a role called Muted to use it')
async def slashmute(ctx, member : discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    guild = ctx.guild
    if role not in guild.roles:
        perms = discord.Permissions(send_messages=False)
        await guild.create_role(name="Muted", permissions=perms)
        await member.add_roles(role)
        await ctx.send(f'Muted {member}')
    else:
        await member.add_roles(role)
        await ctx.send(f'Muted {member}')
        
@client.command()
async def delta(ctx):
   await ctx.send(file=discord.File('deltarune.gif'))
    




client.run(os.getenv("TOKEN"))
