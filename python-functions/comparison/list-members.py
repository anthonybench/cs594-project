#!/usr/bin/env python

#
# List channel/guild members
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

      if "list-members" in message.content:
        res = client.get_all_members()
        for member in res:
          print('='*3)
          print("Name: {0}\nID: {1}\nWeb Status: {2}\nMobile Status: {3}\nGuild Permissions: {4}".format(member.name, member.id, member.web_status, member.mobile_status, member.guild_permissions))
          print('='*3)
      else:
        print("Command not recognized.")

  client = MyClient(intents=intents)
  client.run(secrets['token'])