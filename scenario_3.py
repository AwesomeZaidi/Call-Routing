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
class CallRouter(object):
  
  # ------------------------------------------------------------------------------
  # CallRoutes - Constructor
  # ------------------------------------------------------------------------------
  def __init__(self, carrier_route_path):
      """route_costs: trie tree of costs for routes"""
      self.route_costs = self.__convert_file_into_trie(carrier_route_path)
  
  # ------------------------------------------------------------------------------
  # CallRouter - Intended Private Methods
  # ------------------------------------------------------------------------------
  def __convert_file_into_trie(self, file_path: str) -> Trie:
      """ Returns a Trie tree from the given file_path. Costs of routes."""
      # get number prefixes and costs from lines = numbers_and_costs_from(data_file_path)
      # print('in build_tree')
      trie = Trie()
      # iterates through routes and costs
      with open(file_path, 'r') as f:
        # lines = (l.split(',') for l in f.readlines())
        for line in f:
          line = line[1:-1]
          route, cost = line.split(",")
          # print('line:', line)
          # print('route:', route)
          # print('cost:', cost)
          trie.insert(route, cost)
      return trie

  # ------------------------------------------------------------------------------
  # CallRouter - Public Methods
  # ------------------------------------------------------------------------------
  def read_number(self, path_to_file):
    print('here')
    with open(path_to_file, "r") as file:
      for line in file:
        phone_number = line[:-1]
        print('phone_number:', phone_number)
        cost = self.route_costs.search(phone_number)
        print('cost:', cost)
        # self.write_cost(line, cost)
        return cost


def test_call_router():
  # print('in test router')
  route_costs_path = 'data/route-costs-10.txt'
  phone_number_path = 'data/phone-numbers-3.txt'
  call_router = CallRouter(route_costs_path)
  call_router.read_number(phone_number_path)
  # print('call_router:', call_router.route_costs.__repr__())
  return call_router  
  # numbers = (number for number in
  #   open('data/phone-numbers-3.txt').readlines())
  
  # with open('output/call-costs-3.txt', 'w') as output_file:
  #   for number in numbers:
  #       cost = route_costs_trie.search(number)
  #       output_file.write(f'{number},{cost}\n')

if __name__ == '__main__':
  test_call_router()
  print('done')







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
