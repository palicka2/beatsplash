class HelpCommand:
    async def execute(self, msg, args):
        await msg.channel.send("```"
                               "?help - shows all commands you can use\n"
                               "?play + link - joins your channel and starts playing music\n"
                               "?pause - pauses the current song\n"
                               "?resume - resumes the paused song\n"
                               "?disconnect - stops the music and disconnects from voice channel``` \n"
                               "Hope this helps <@{}>".format(msg.author.id))
