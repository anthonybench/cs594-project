#!/usr/bin/env python

#
# Creates a channel, with characteristics/settings of a given channel.
#

#---Dependencies-------------
from discord import Client, Intents
import features
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

      if "create-channel" in message.content:
        res = client.get_all_channels()
        argv = message.content.split(' ')
        for channel in res:
          if len(argv) < 3:
            return
          elif str(channel.type) == 'text' and channel.name == argv[1]:
            print('='*3)
            await channel.clone(name=argv[2])
            print("Channel created!")
            print('='*3)
      else:
        print("Command not recognized.")

  client = MyClient(intents=intents)
  try:
    client.run(secrets['token'])
  except:
    print('Error: 401 Unauthorized.\nInvalid user token.')