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

class Hash_CallRouter(object):
# ------------------------------------------------------------------------------
# CallRoutes - Constructor
# ------------------------------------------------------------------------------
    def __init__(self, carrier_route_path):
        """ route_costs: hash table: routes : costs"""
        self.route_costs_hashtable = self.__convert_file_into_hashtable(carrier_route_path)
# ------------------------------------------------------------------------------
# CallRouter - Intended Private Methods
# ------------------------------------------------------------------------------
    def __convert_file_into_hashtable(self, file_path):
        """Turns txt into hash set"""
        hash_lookup = HashTable()
        with open('data/' + file_path, "r", buffering=200000000) as file:
           for line in file:
                line = line[:-1]
                route, cost = line.split(",")
                if hash_lookup.contains(route):
                    original_cost = hash_lookup.get(route)
                    if cost < original_cost:
                        hash_lookup.set(route, cost)
                else:
                    hash_lookup.set(route, cost)
        return hash_lookup

    def read_number(self, path_to_file):
        with open('data/' + path_to_file, "r", buffering=200000000) as file:
           for line in file:
               line = line[:-1]
               cost = self.find_route_cost(line)
               self.write_cost(line, str(cost))
# ------------------------------------------------------------------------------
# CallRouter - Public Methods
# ------------------------------------------------------------------------------
    def find_route_cost(self, phone_number):
        for _ in phone_number:
            if self.route_costs_hashtable.contains(phone_number):
                cost = self.route_costs_hashtable.get(phone_number)
                return cost
            else:
                phone_number = phone_number[:len(phone_number)-1]
        return 0
        

    def write_cost(self, phone_number, cost):
        with open('data/' + "call-costs-2.txt", "a") as f:
            f.write(phone_number + ", " + cost + "\n")

def test_call_router():
    carrier_route_path = 'route-costs-106000.txt'
    phone_number_path = 'phone-numbers-1000.txt'
    call_router = Hash_CallRouter(carrier_route_path)
    call_router.read_number(phone_number_path)
    return call_router
# ------------------------------------------------------------------------------
# Memory Usage Function (Inspired by research)
# ------------------------------------------------------------------------------
def get_memory(): 
    pass


if __name__ == '__main__':
    start = time.time()
    print("\nInitializing Scenario 2 wait...")
    test_call_router()
    load_time = round(time.time() - start, 4)
    print("\nThis took: {}.".format(load_time))
    get_memory()
