import discord
import asyncio
import youtube_dl
from Commands.DisconnectCommand import DisconnectCommand
from Commands.PlayCommand import PlayCommand
from Commands.HelpCommand import HelpCommand
from Commands.PauseCommand import PauseCommand
from Commands.ResumeCommand import ResumeCommand

token = "MTAzNTkwOTUwNjExNjM1NDE4OA.GgBVb9.0_Sg6UPW0EGLcF8TM2gTjZOj7DLT5iCAas7UB8"
intents = discord.Intents.all()

client = discord.Client(intents=intents)

voice_clients = {}


yt_dl_options = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_options)

ffmpeg_options = {'options': '-vn'}

commands =  {"help": HelpCommand(),
             "play": PlayCommand(voice_clients, ytdl, ffmpeg_options),
             "pause": PauseCommand(voice_clients),
             "resume": ResumeCommand(voice_clients),
             "disconnect": DisconnectCommand(voice_clients)}

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

@client.event
async def on_message(msg):
    cmnd = msg.content.lower().strip()
    if cmnd[0] == "?":
        args = cmnd.split(" ")
        cmnd_name = args[0][1:]
        if cmnd_name in commands.keys():
            c = commands.get(cmnd_name)
            if len(args) == 1:
                await c.execute(msg, "")
            else :
                await c.execute(msg, args[1])

client.run(token)


