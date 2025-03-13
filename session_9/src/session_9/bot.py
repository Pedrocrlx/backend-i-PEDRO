import discord
from dotenv import load_dotenv
from rich import print

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(
        f'We have [bold green]logged[/bold green] in as [bold blue]{client.user}[/bold blue]')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('oi'):
        await message.channel.send('funfa ou nada')
