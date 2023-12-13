
"""
Bitcoin is a form of digitial currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

In a file called bitcoin.py, implement a program that:

Expects the user to specify as a command-line argument the number of Bitcoins, 
, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
"""


import requests
import sys
import json

if len(sys.argv) == 2 :
  try:
    bitcoin_num = float(sys.argv[1])
  except:
    sys.exit('Command line arguement is not a number')
  try:  
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
  except requests.RequestException:
    sys.exit('Something bad happened') 

  o = response.json()
  price = float(o['bpi']['USD']['rate_float'])
  value = float(sys.argv[1])
  total_amount = value * price
  print(f'{total_amount:,.4f}')
  

else:
  sys.exit('Missing command line arguement')
