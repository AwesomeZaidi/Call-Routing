# !python

# ==================================================================================
# File: scenario_2.py

# List of route costs to check
# You have a carrier route list with 100,000 (100k) entries (in arbitrary order) and a list of
# 1000 phone numbers. How can you operationalize the route cost lookup problem.

# Copyright © 2019 Jayce Azua and Asim Zaidi. All rights reserved.
# ==================================================================================

import random # generate random numbers
import re # regular expressions
import sys # command line args
from hashtable import HashTable 

class CallRouter(object):

    # function to convert phone_numbers file into a list of numbers
    # function to convert route_costs into a hash set with lowest costs for routes

    # function to find the lowest cost of a number in the route_costs hash set
    
    # go through our phone_numbers list and run each one in find_lowest_price_for_number
    # write each number and its cost into a text file.

    def __init__(self, carrier_route_path):
        self.route_costs = self._convert_file_into_hashtable(carrier_route_path)

    def _convert_file_into_hashtable(self, path_to_file):
        """Turns txt into hash set"""
        hash_lookup = HashTable()
        with open('data/' + path_to_file, "r") as file:
           for line in file:
            #    remove end of string
            line = line[:-1]
            # slice through comma space
            carrier, cost = line.split(",")

            if hash_lookup.contains(carrier):
                original_cost = hash_lookup.get(carrier)
                if cost < original_cost:
                    hash_lookup.set(carrier, cost)
            else:
                hash_lookup.set(carrier, cost)
        return hash_lookup

def test_call_router():
    # phone_numbers_path = 'data/phone-numbers-1000.txt'
    carrier_route_path = 'carrier-routes-4.txt'
    call_router = CallRouter(carrier_route_path)
    return call_router.route_costs.values()

if __name__ == '__main__':
    print(test_call_router())
