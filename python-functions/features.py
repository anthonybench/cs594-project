#
# Creates a channel, with characteristics/settings of a given channel.
#
async def createChannel(client, message):
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

#
# Delivers a file to channel.
#
async def deliverFile(File, message):
  res = message.channel
  print('='*3)
  payload = File('test-file-system/hello.txt')
  await res.send(file=payload)
  print('='*3)

#
# Send direct message to user who requests it
#
async def dmMe(message):
  await message.author.send(content="Hello! Beep boop!")
  print('='*3)
  print('Direct message sent!')
  print('='*3)

#
# List channels in guild
#
async def listChannels(client):
  res = client.get_all_channels()
  for channel in res:
    print('='*3)
    print("{0}".format(channel.name))
    print('='*3)

#
# List channel/guild members
#
async def listMembers(client):
  res = client.get_all_members()
  for member in res:
    print('='*3)
    print("Name: {0}\nID: {1}\nWeb Status: {2}\nMobile Status: {3}\nGuild Permissions: {4}".format(member.name, member.id, member.web_status, member.mobile_status, member.guild_permissions))
    print('='*3)

#
# Send message to one or more distinct channels
#
async def messageChannels(client, message):
  res = [i for i in client.get_all_channels() if str(i.type) == 'text']
  for channel in res:
    if channel.name in message.content:
      print('='*3)
      print(channel.name)
      await channel.send(content="Messaging distinct channel! Beeop boop!")
      print('='*3)


async def logOut(message):
  await message.channel.send(content="Signing off!")