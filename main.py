import discord
import os
import weatherbot


TOKEN = 'OTA0MjY1Mzc1MzQzMDc5NTA1.YX5AwQ.5eeVmGdw22i5LeRFDJ1Cas3DVdU'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hi'):
        await message.channel.send("Hello!!!")
    if message.content.startswith('$'):
        cityName = message.content[1:]

        data = weatherbot.weatherBot(cityName)
        await message.channel.send(data)



client.run(TOKEN)
