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
      with open(file_path, 'r', buffering=2000000) as f:
        # lines = (l.split(',') for l in f.readlines())
        for line in f:
          line = line[:-1]
          route, cost = line.split(",")

          trie.insert(route, cost)
      return trie

  # ------------------------------------------------------------------------------
  # CallRouter - Public Methods
  # ------------------------------------------------------------------------------



def test_call_router():
  # print('in test router')
  route_costs_path = 'data/carrier-routes-10.txt'
  # phone_number_path = 'data/phone-numbers-3.txt'
  call_router = CallRouter(route_costs_path)
  return call_router.route_costs.root.children[1].children
# +34749512, 0.27
# +1423927, 0.03
if __name__ == '__main__':
  print(test_call_router())
