#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement a solution that is more efficient than the naive recursive solution

def eating_cookies(num_cookies, cache={}):
  if num_cookies in cache:  # runtime complexity:  O(n)  because you're looping through the cache object
    return cache[num_cookies]
  
  if num_cookies == 0:  # base case
    value = 1  # runtime complexity:  O(1)
  elif num_cookies > 0:
    print('num of cookies: ', num_cookies)
    value = eating_cookies(num_cookies -1) + eating_cookies(num_cookies-2) + eating_cookies(num_cookies-3)  # runtime complexity:  O(3n!)  b/c calling the function 3x
  elif num_cookies < 0:  # runtime complexity:  O(1)
    value = 0
  
  cache[num_cookies] = value  # runtime complexity:  O(1)
  return value
  # O(n) + O(1) + O(3n!) + O(1) + O(1) 
  # ==> 3 + O(n) + O(3n!)
  # ==> O(3n!) 
  # ==> O(n!) is the most important time complexity to consider in this problem
  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
    

# function takes in n number of cookies
# return number of possible ways to consume the cookies, e.g.: 
  # 1 cookie: 1 way (1, 0)
  # 2 cookies: 2 ways (1, 1; 2, 0)
  # 3 cookies: 4 ways (1, 1, 1; 1, 2; 2, 1, 3, 0)
  # 4 cookies: 7 ways (1, 1, 1, 1; 1, 1, 2; 1, 2, 1; 1, 3; 2, 1, 1; 2, 2; 3, 1)
  # 5 cookies: 13 ways (1, 1, 1, 1, 1; 1, 1, 1, 2; 1, 1, 2, 1; 1, 2, 1, 1; 1, 2, 2; 1, 1, 3; 1, 3, 1; 2, 1, 1, 1; 2, 1, 2; 2, 2, 1; 2, 3; 3, 1, 1; 3, 2)