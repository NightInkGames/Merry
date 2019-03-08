import discord
from discord.ext import commands

class Moderation():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members = True) 
    async def kick(self,ctx, userName: discord.User):
            await self.bot.kick(userName)
            await self.bot.say("Gotcha! Kicked their nuts outta here! :3")

    @commands.command(pass_context = True)
    @commands.has_permissions(ban_members = True) 
    async def ban(self,ctx, userName: discord.User):
            await self.bot.ban(userName)
            await self.bot.say("Gotcha! Banned 'em!")

#kick, ban, mute

def setup(bot):
    bot.add_cog(Moderation(bot))
