#!/usr/bin/env python

#
# Delivers a file to channel.
#

#---Dependencies-------------
from discord import Client, Intents, File
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

      if "deliver-file" in message.content:
        res = message.channel
        print('='*3)
        payload = File('test-file-system/hello.txt')
        await res.send(file=payload)
        print('='*3)
      else:
        print("Command not recognized.")

  client = MyClient(intents=intents)
  client.run(secrets['token'])