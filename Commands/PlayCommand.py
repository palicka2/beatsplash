import asyncio
import discord



class PlayCommand:
    def __init__(self, voice_clients, ytdl, ffmpeg_options):
        self.voice_clients = voice_clients
        self.ytdl = ytdl
        self.ffmpeg_options = ffmpeg_options

    async def execute(self, msg, args):
        try:
            voice_client = await msg.author.voice.channel.connect()
            self.voice_clients[voice_client.guild.id] = voice_client

            url = msg.content.split()[1]
            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))
            print(data['url'])
            song = data['url']
            player = discord.FFmpegPCMAudio(song, **self.ffmpeg_options, executable="ffmpeg\\bin\\ffmpeg.exe")

            self.voice_clients[msg.guild.id].play(player)
            await msg.channel.send("Playing ")


        except Exception as err:
            print(err)


