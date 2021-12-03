#!/usr/bin/env python

#
# Send direct message to user who requests it
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

      if "dm-me" in message.content:
        await message.author.send(content="Hello! Beep boop!")
        print('='*3)
        print('Direct message sent!')
        print('='*3)
      else:
        print("Command not recognized.")

  client = MyClient(intents=intents)
  client.run(secrets['token'])