#!/usr/bin/env python

#
# Send message to one or more distinct channels
#

#---Dependencies-------------
from discord import Client, Intents
from json import load

#---Parameters---------------
intents = Intents(messages=True, guilds=True, members=True)

#---Execution----------------
with open("config.json", "r") as json_file:
  secrets = load(json_file)
  class MyClient(Client):
    async def on_ready(self):
      print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
      print('Message from {0.author}: {0.content}'.format(message))

      if "message-channels" in message.content:
        # res = [i for i in client.get_all_channels() if i.type == 'text']
        res = [i for i in client.get_all_channels() if str(i.type) == 'text']
        for channel in res:
          if channel.name in message.content:
            print('='*3)
            print(channel.name)
            await channel.send(content="Messaging distinct channel! Beeop boop!")
            print('='*3)
      else:
        print("Command not recognized.")

  client = MyClient(intents=intents)
  client.run(secrets['token'])