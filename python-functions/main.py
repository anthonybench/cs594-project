#!/usr/bin/env python

# Execution agent for python-supported features.

#---Dependencies-------------
from discord import Client, Intents, File
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

    # Handlers
    async def on_message(self, message):
      print('Message from {0.author}: {0.content}'.format(message))

      if "create-channel" in message.content:
        await features.createChannel(client, message)
      elif "deliver-file" in message.content:
        await features.deliverFile(File, message)
      elif "dm-me" in message.content:
        await features.dmMe(message)
      elif "list-channels" in message.content:
        await features.listChannels(client)
      elif "list-members" in message.content:
        await features.listMembers(client)
      elif "message-channels" in message.content:
        await features.messageChannels(client, message)
      elif "/logout" in message.content:
        await features.logOut(message)
        await client.close()
        return
      else:
        print("Command not recognized.")

  client = MyClient(intents=intents)
  try:
    client.run(secrets['token'])
  except:
    print('Error: 401 Unauthorized.\nInvalid user token.')