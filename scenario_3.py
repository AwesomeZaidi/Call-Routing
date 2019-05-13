# !python

# ==================================================================================
# File: scenario_3.py

# You have 5 carrier route lists, each with 10,000,000 (10m) entries (in arbitrary order)
# and a list of 10,000 phone numbers. How can you speed up your route cost lookup
# solution to handle this larger dataset

# Copyright © 2019 Jayce Azua and Asim Zaidi. All rights reserved.
# ==================================================================================

import re
import os
import glob
from trie import Trie

def build_trie(file_path: str) -> Trie:
    """ Returns a Trie tree from the given file_path. Costs of routes."""
    # get number prefixes and costs from 
    # lines = numbers_and_costs_from(data_file_path)
    trie = Trie()

    # iterates through routes and costs
    with open(file_path, 'r') as f:
        lines = (l.split(',') for l in f.readlines())

    for route, cost in lines:
        trie.insert(route[1:], float(cost))

    return trie

def test_call_router():
      route_costs_path = 'data/route-costs-10000000.txt'
      route_costs_trie = build_trie(route_costs_path)

      numbers = (number for number in
        open('data/phone-numbers-1000.txt').readlines())
      
      with open('output/call-costs-3.txt', 'w') as output_file:
        for number in numbers:
            cost = route_costs_trie.search(number)
            output_file.write(f'{number},{cost}\n')

if __name__ == '__main__':
  test_call_router()







# def buildTrieOfRoutes(self, file):
#   """
#     Takes in a file with lines of 'route,costs' and builds a Trie of the routes' digits.
#   """
#   for line in open(file):
#     current = self.root
#     route, cost = line.split(",")
#     cost = float(cost.strip("\n"))
#     for digit in route:
#       if digit not in current.dictionary:
#           current.dictionary[digit] = Trie(digit)
#       current = current.dictionary[digit]
#     if current.cost:
#       if current.cost > cost:
#           current.cost = cost
#   else:
#     current.cost = cost

#   def findLowestCostsAndPrintThemToFile(self, file):
#     """Finds the lowest costs for each phone number in the input file."""

#     for phoneNumber in open(file):
#       current = self.root
#       minimum = float('inf')
#       for digit in phoneNumber:
#         if digit in current.dictionary:
#           if current.cost:
#               minimum = min(minimum, current.cost)
#           current = current.dictionary[digit]
#         else:
#           phoneNumber = phoneNumber.strip("\n")
#           if minimum != float('inf'):
#               with open("output_logs/route-costs-3.txt", "a+") as f:
#                       f.write(phoneNumber + ", " + str(minimum) + '\n')
#           else:
#               with open("output_logs/route-costs-3.txt", "a+") as f:
#                       f.write(phoneNumber + ", 0 \n")
#           break  # break out of the 'for digit in phoneNumber' loop
#           # and start on the next phoneNumber.
