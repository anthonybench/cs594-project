#!/usr/bin/env python

import discord
from json import load;

with open("data.json", "r") as json_file:
  secrets = json.load(json_file)
  class MyClient(discord.Client):
      async def on_ready(self):
          print('Logged on as {0}!'.format(self.user))

      async def on_message(self, message):
          print('Message from {0.author}: {0.content}'.format(message))
          ress = client.get_all_channels()

          res = []
          for i in ress:
            res.append(i.name)
          print(res)

  client = MyClient()
  client.run(secrets.token)