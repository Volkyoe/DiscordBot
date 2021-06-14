hint = ''
pokedex = []

with open('pokedex.txt', encoding='utf8') as fp:
  for line in fp:
    line = line.strip().lower()
    i = line.find(' ') + 1
    number = int(line[0: i])
    names = [e[1: -1] for e in line[i+1: -1].split(', ')]
    for name in names:
      pokedex.append((name, number))

def match(new_hint):
  global hint, pokedex
  matches = []
  if len(new_hint) != len(hint):
    hint = '?' * len(new_hint)
  hint = ''.join([s if h == '?' else h for s, h in zip(hint, new_hint)])

  for pokemon, number in pokedex:
    if len(pokemon) != len(hint):
      continue
    if all([h == '?' or h == p for p, h in zip(pokemon, hint)]):
      matches.append(pokemon)
  return matches

def reset():
  global hint
  hint = ''