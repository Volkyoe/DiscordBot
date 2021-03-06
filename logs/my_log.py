import logging

def log(fname):
  logger = logging.getLogger('discord')
  logger.setLevel(logging.DEBUG)
  handler = logging.FileHandler(filename=fname, encoding='utf-8', mode='w')
  handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
  logger.addHandler(handler)