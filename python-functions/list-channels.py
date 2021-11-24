#!/usr/bin/env python

#
# List channels in guild
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

      if "list-channels" in message.content:
        res = client.get_all_channels()
        for channel in res:
          print('='*3)
          print("{0}".format(channel.name))
          print('='*3)
      else:
        print("Command not recognized.")

  client = MyClient(intents=intents)
  client.run(secrets['token'])