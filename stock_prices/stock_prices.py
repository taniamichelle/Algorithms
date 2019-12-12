#!/usr/bin/python

import argparse
# ROUGH SOLUTION: less efficient
# def max_profit(price_array):
#   profit = 0
#   for i in range(len(price_array)):
#     buy = price_array[i]
#     for j in range(i + 1, len(price_array)):
#       sell = price_array[j]
#       if profit < sell - buy:  
#         profit = sell - buy  # update value of profit      
#   return profit

# arr = [10, 7, 5, 8, 11, 9]
# print(max_profit(arr))

def find_max_profit(prices):
  current_min_price_so_far = prices[0] # price at zero index
  max_profit_so_far = prices[1] - prices[0] # subtract price at zero index from price at first index

  for i in range(1, len(prices)):
    if prices[i] < current_min_price_so_far:  # if price we're looking at is less than the current min price: 
      current_min_price_so_far = prices[i]  # the current min price will be the price we're looking at
    elif prices[i] - current_min_price_so_far > max_profit_so_far:
      max_profit_so_far = prices[i] - current_min_price_so_far
  
  return max_profit_so_far

arr = [10, 7, 5, 8, 11, 9]
print(find_max_profit(arr))

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
  
  
