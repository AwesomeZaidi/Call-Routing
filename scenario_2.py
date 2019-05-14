# !python

# ==================================================================================
# File: scenario_2.py

# List of route costs to check
# You have a carrier route list with 100,000 (100k) entries (in arbitrary order) and a list of
# 1000 phone numbers. How can you operationalize the route cost lookup problem.

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

class CallRouter(object):
    
    # ------------------------------------------------------------------------------
    # CallRoutes - Constructor
    # ------------------------------------------------------------------------------
    def __init__(self, carrier_route_path):
        """
            route_costs: hash table: routes : costs
        """
        self.route_costs = self.__convert_file_into_hashtable(carrier_route_path)
    
    # ------------------------------------------------------------------------------
    # CallRouter - Intended Private Methods
    # ------------------------------------------------------------------------------
    def __convert_file_into_hashtable(self, path_to_file):
        """Turns txt into hash set"""
        hash_lookup = HashTable()
        with open('data/' + path_to_file, "r") as file:
           for line in file:
                line = line[:-1]
                carrier, cost = line.split(",")
                
                if hash_lookup.contains(carrier):
                    original_cost = hash_lookup.get(carrier)

                    if cost < original_cost:
                        hash_lookup.set(carrier, cost)
                else:
                    hash_lookup.set(carrier, cost)
        return hash_lookup

    def read_number(self, path_to_file):
        with open('data/' + path_to_file, "r") as file:
           for line in file:
               line = line[:-1]
               cost = self.find_route_cost(line)
               self.write_cost(line, cost)

    # ------------------------------------------------------------------------------
    # CallRouter - Public Methods
    # ------------------------------------------------------------------------------
    def find_route_cost(self, phone_number):
        for _ in phone_number:

            if self.route_costs.contains(phone_number):

                cost = self.route_costs.get(phone_number)
                return cost

            else:
                phone_number = phone_number[:len(phone_number)-1]
        return str(0)
        

    def write_cost(self, phone_number, cost):
        with open('data/' + "call-costs-2.txt", "a") as f:
            f.write(phone_number + ", " + cost + "\n")

def test_call_router():
    # phone_numbers_path = 'data/phone-numbers-1000.txt'
    carrier_route_path = 'route-costs-10000000.txt'
    call_router = CallRouter(carrier_route_path)
    call_router.read_number('phone-numbers-10000.txt')
    return call_router.route_costs.values()

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
    test_call_router()
    load_time = round(time.time() - start, 4)
    print("\nThis took: {}.".format(load_time))
    get_memory()
