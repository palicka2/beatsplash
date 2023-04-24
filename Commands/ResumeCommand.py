class ResumeCommand:
    def __init__(self, voice_clients):
        self.voice_clients = voice_clients

    def execute(self, msg, args):
        try:
            self.voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)

