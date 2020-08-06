import asyncio
import discord
from discord.ext import commands
import re
from discord.utils import get
import random
import os


client = discord.Client()
client = commands.Bot(command_prefix= '.')
bot = discord.Client()

token = "NzQwODk1NTYwMTkzNjcxMjkw.Xyvqwg.C8C9hM4AhMi-OkbRMFacqOaKb0U"

adminid = [435025892650123277] 

@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("24시 구매 ! TheCheat#1004")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
        embed = discord.Embed(color=0xff00ae)
        embed.add_field(name='[ 더치트 계정샵 ]', value=str(member.mention)+'**님 안녕하세요 !**', inline=True)
        # embed.set_image(url="")
        embed.set_footer(text=f"https://discord.gg/yB3kBd")
        hello = client.get_channel(722810116386324531)
        await hello.send(embed=embed)

@client.event
async def on_member_remove(member):
        embed = discord.Embed(color=0xffa00ae)
        embed.add_field(name='', value=str(member.mention)+'**님 안녕히가세요....**', inline=True)
        # embed.set_image(url="")
        embed.set_footer(text=f"https://discord.gg/yB3kBd")
        hello = client.get_channel(739872922990280807)
        await hello.send(embed=embed)

client.run(token)