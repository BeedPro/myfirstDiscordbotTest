import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '.')

#When its online
@client.event
async def on_ready():
    print('Bot is Online') 

#help
@client.command()
async def helpme(ctx):
    await ctx.channel.send("```\n.spam [amount]\n.8ball [Question]\n.playball [Question]\n.clear [amount]\n.kick [@name]\n.ban [@name]\n```")



#checking the ping
@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)} ms')
    
# 8 ball game
@client.command(aliases=['8ball','playball'])
async def _8ball(ctx, * , question):
    responses = ['YES',
                 'DONT WORRY',
                 'NO',
                 'IDK']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

#Clearing
@client.command(aliases=['2clear','allclear'])
async def clear(ctx, amount=100000000000):
    await ctx.channel.purge(limit=amount)

#Spam
@client.command()
async def spam(ctx,amount=100):
    for i in range(amount):
        
        msg = ['Hello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello SpammersHello Spammers']

        await ctx.channel.send(f'{random.choice(msg)}')
        
# Banning and Kicking 
@client.command()
async def kick(ctx, member : discord.Member,*,reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'banned {member.mention}')


@client.command()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')


    for ban_entry in ban_users:
        user = ban_entry.user

        if (user.name,user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'unbanned {user.mention}')
            return


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server. Welcome')

@client.event
async def on_member_remove(member):
    print(f'{member} has left server. Goodbye')


client.run('token')
