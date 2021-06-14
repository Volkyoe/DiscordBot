from flask import Flask
from threading import Thread
from replit import db

app = Flask('')

@app.route('/')
def home():
  return f"Hello. I am alive!"

@app.route('/hint/<channel>')
def get_hint(channel):
  return db[channel] if channel in db else ''

@app.route('/prefix_del')
def get_del():
  return db['cmd_del']

def run():
  app.run(host='0.0.0.0', port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()