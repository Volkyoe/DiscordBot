import discord
import os
from replit import db
from keep_alive import keep_alive
import pokebot
from logs.my_log import log

log('logs/discord.log')
db['cmd_del'] = '$del'
db['cmd_channel'] = '$channel'

bot = discord.Client()

for k in db.keys():
  print(db[k])

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  
  msg = message.content
  channel = message.channel.id

  for embed in message.embeds:
    if 'A wild pokémon has appeared!' in embed.title:
      pokebot.reset()
      db[channel] = 'p!h'
  
  hint_pref = 'The pokémon is '
  if msg.startswith(hint_pref):
    print(msg)
    hint = msg[len(hint_pref): -1].replace('\\_', '?').lower()
    print(hint)
    result = pokebot.match(hint)
    print(result)
    if not result:
      pokebot.reset()
    db[channel] = f'p!c {result[0]}' if len(result) == 1 else 'p!h'

  caught_pref = 'Congratulations'
  if msg.startswith(caught_pref):
    db[channel] = ''
    pokebot.reset()
  
  if msg.startswith(db['cmd_del']):
    await message.delete()

  if msg.startswith(db['cmd_channel']):
    await message.channel.send(f'This channel `id` is `{channel}`')

keep_alive()
bot.run(os.environ['TOKEN'])
