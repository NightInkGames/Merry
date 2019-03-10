from discord.ext import commands
import discord
from discord import Game
import time

bot = commands.Bot(command_prefix=";MN-", ";mN-", ";mn-", ";Mn-")
bot.load_extension('ModCommands')
bot.remove_command('help')
@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name="With my Prefix (;MN-)"))
    print("Logged in as " + bot.user.name)

#Version 0.0.1

@bot.command()
async def cookie():
    await bot.say(':cookie:')

@bot.command(pass_context=True)
async def ping(ctx):
    resp = await bot.say('Pongaboo! Loading...')
    diff = resp.timestamp - ctx.message.timestamp
    await bot.edit_message(resp, 'Pongaboo! That took me {:.1f}ms.'.format(1000*diff.total_seconds()))

@bot.command(pass_context=True)
async def commands(ctx):
    embed = discord.Embed(title='Command List', description='A list of all commands! My creator is constantly working with me to add more, so please have some patience!', color=0x9b21a5)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/549689069827784715/551814807620157472/merrybotpfp.png')
    embed.add_field(name="Info", value="help, commands, info, userinfo, ping", inline=False)
    embed.add_field(name="Social", value="Coming soon", inline=False)
    embed.add_field(name="Memes", value="Coming soon", inline=False)
    embed.add_field(name="Fun", value="cookie", inline=False)
    embed.add_field(name="Moderation", value="kick, ban, mute", inline=False)
    embed.add_field(name="Calculator", value="add, multiply, sub, div", inline=False)
    embed.add_field(name="Misc", value="Coming soon", inline=False)
	embed.add_field(name=" ", value="For more information on a certain command, type ;MN-help <command>", inline=False)
    embed.set_footer(text='© NightInk')
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def userinfo(ctx,member: discord.Member=None):
        'Show info about a member'
        if member is None:
            member = ctx.message.author
        em = discord.Embed(color=0x00ff00)
        em.add_field(name='Name', value='{0.name}'.format(member))
        em.add_field(name='ID', value='{0.id}'.format(member))
        em.add_field(name='Top Role', value='{0.top_role}'.format(member))
        em.add_field(name='Roles', value=', '.join(g.name for g in member.roles))
        em.add_field(name='Joined', value='{0.joined_at}'.format(member))
        em.add_field(name='Registered', value='{0.created_at}'.format(member))
        em.set_thumbnail(url=member.avatar_url)
        await bot.say(embed=em)

@bot.command()
async def add(a : int, b : int):
    await bot.say(a + b)

@bot.command()
async def multiply(a : int, b : int):
    await bot.say(a * b)

@bot.command()
async def sub(a : int, b : int):
    await bot.say(a - b)

@bot.command()
async def div(a : int, b : int):
    await bot.say(a / b)

@bot.command()
async def mute():
    await bot.say("This command is currently unavailable! Please have some patience until it's finished!")

@bot.command(pass_context=True)
async def info(ctx):
    embed = discord.Embed(title='Bot Info', description='Info about me, such as my version!', color=0x9b21a5)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/549689069827784715/551814807620157472/merrybotpfp.png')
    embed.add_field(name="Version", value="0.0.1", inline=True)
    embed.set_footer(text='© NightInk')
    await bot.say(embed=embed)

@bot.command(pass_context = True)
async def say(ctx,*,message):
    if ctx.message.author.id == '374996779781062656':
         await bot.say(message)
    else:
        await bot.say("Sorry, can't do that for ya. Bot Owner only.")
		
#Version 0.1.0

@bot.listen()
async def on_member_join(Member):
	if ctx.sever.id == '397528685672005632'
    role = discord.utils.get(Member.server.roles,  name="Unverified")
	    await bot.add_roles(Member, role)
     else:
        return;
	
@bot.listen()  
async def on_command_error(self, error: Exception):
    if isinstance(error, commands.CommandNotFound):
        await bot.say("What? It seems like that command doesn't exist!")



bot.run(os.getenv("TOKEN"))
