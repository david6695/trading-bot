import ccxt
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()

with open("config.json") as f:
   config = json.load(f)

kraken = ccxt.kraken({
   'apiKey': os.getenv('KRAKEN_API_KEY'),
   'secret': os.getenv('KRAKEN_API_SECRET'),
})

symbol = config["trading_pair"]
amount = config["trade_amount"]

def fetch_price():
   ticker = kraken.fetch_ticker(symbol)
   return ticker['last']

def execute_trade(price):
   if price <= config["strategy"]["buy_threshold"] * fetch_price():
       print("Buying", symbol)
       # kraken.create_market_buy_order(symbol, amount)
   elif price >= config["strategy"]["sell_threshold"] * fetch_price():
       print("Selling", symbol)
       # kraken.create_market_sell_order(symbol, amount)
   else:
       print("Holding at", price)

while True:
   try:
       current_price = fetch_price()
       print("Current price:", current_price)
       execute_trade(current_price)
       time.sleep(10)
   except Exception as e:
       print("Error:", str(e))
       time.sleep(15)
