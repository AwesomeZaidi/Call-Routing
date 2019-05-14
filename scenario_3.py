# !python

# ==================================================================================
# File: scenario_3.py

# You have 5 carrier route lists, each with 10,000,000 (10m) entries (in arbitrary order)
# and a list of 10,000 phone numbers. How can you speed up your route cost lookup
# solution to handle this larger dataset

# Copyright © 2019 Jayce Azua and Asim Zaidi. All rights reserved.
# ==================================================================================

# scenario 1 - 3
import os
import re
import sys
import time
import mmap
import random
import resource
import platform
# scenario 2
from hashtable import HashTable
# scenario 3
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
  def __convert_file_into_trie(self, file_path: str):
      """ Returns a Trie tree from the given file_path. Costs of routes."""
      # get number prefixes and costs from lines = numbers_and_costs_from(data_file_path)
      # print('in build_tree')
      trie = Trie()
      # iterates through routes and costs
      with open('data/' + file_path, 'r', buffering=2000000000) as f:
        for line in f:
          line = line[:-1]
          route, cost = line.split(",")

          trie.insert(route, cost)
      return trie

  def read_number(self, path_to_file):
    with open('data/' + path_to_file, "r", buffering=200000000) as file:
        for line in file:
            line = line[:-1]
            cost = self.route_costs.search_and_return_cost(line)
            self.write_cost(line, str(cost))



  # ------------------------------------------------------------------------------
  # CallRouter - Public Methods
  # ------------------------------------------------------------------------------
  def write_cost(self, phone_number, cost):
      with open('data/' + "call-costs-3.txt", "a") as f:
          f.write(phone_number + ", " + cost + "\n")

# ------------------------------------------------------------------------------
# Memory Usage Function (Inspired by https://github.com/edwintcloud)
# ------------------------------------------------------------------------------
def get_memory(): 
    """Print memory usage to stdout."""
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if platform.system() == 'Linux':
        usage = round(usage/float(1 << 10), 2)
    else:
        usage = round(usage/float(1 << 20), 2)
    print("Current Memory Usage: {} mb.".format(usage))



if __name__ == '__main__':
  start = time.time()
  print("\nInitializing please wait...")
  route_costs_path = 'route-costs-10000000.txt'
  phone_number_path = 'phone-numbers-10000.txt'
  call_router = CallRouter(route_costs_path)
  call_router.read_number(phone_number_path)
  load_time = round(time.time() - start, 4)
  print("\nThis took: {}.".format(load_time))
  get_memory()
  
# maybe implement for memoization
