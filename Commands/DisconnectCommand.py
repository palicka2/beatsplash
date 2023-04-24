class DisconnectCommand:
    def __init__(self, voice_clients):
        self.voice_clients = voice_clients

    async def execute(self, msg, args):
            try:
                self.voice_clients[msg.guild.id].stop()
                await self.voice_clients[msg.guild.id].disconnect()
            except Exception as err:
                print(err)
