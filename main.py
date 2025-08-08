import time

def fetch_price():
   # This should connect to a real API like Binance or Coinbase
   return 100  # dummy price

def should_buy(price):
   return price < 105

def should_sell(price):
   return price > 110

def run_bot():
   while True:
       price = fetch_price()
       if should_buy(price):
           print("Buying at", price)
       elif should_sell(price):
           print("Selling at", price)
       else:
           print("Holding at", price)
       time.sleep(5)

if __name__ == "__main__":
   run_bot()
