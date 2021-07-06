#!/usr/bin/python

import sys

def rock_paper_scissors(rounds_remaining):  # n represents the number of plays per round
  possible_plays = ["rock", "paper", "scissors"]
  list_of_possible_outcomes = []
  
  def helper_function(rounds_remaining, results=[]):
    if rounds_remaining == 0:
      print('results: ', results)
      return list_of_possible_outcomes.append(results)
    for play in possible_plays:
      helper_function(rounds_remaining-1, results+[play])
  
  helper_function(rounds_remaining)
  return list_of_possible_outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')