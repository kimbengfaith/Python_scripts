#! /usr/bin/python3

"""
In this project i created a program that tells you when the value of your bitcoin falls bellow $30,000.

If the bicoin falls below $30,000, a message will be given to you

I assumed that 1 bitcoin is worth $40,000.
"""

investment_in_bitcoin = int(input("Enter your bitcoint amount: "))
bitcoin_to_usd = int(input("Enter you bitcoin amount in usd: ")) 

# function that calculates the value of the bitcoin in usd.

def bitcointousd(bitcoin_amount, bitcoin_value_usd):
  usd_value = bitcoin_amount*bitcoin_value_usd
  return usd_value

investment_in_usd = bitcointousd(investment_in_bitcoin, bitcoin_to_usd)

# Checks if the the investment has gone bellow 30000
if investment_in_usd <= 30000:
  print('Investment below $30,000! SELL!')
else:
  print('Investment above $30,000')