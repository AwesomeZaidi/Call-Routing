# !python

# ==================================================================================
# File: scenario_2.py

# List of route costs to check
# You have a carrier route list with 100,000 (100k) entries (in arbitrary order) and a list of
# 1000 phone numbers. How can you operationalize the route cost lookup problem.

# Copyright © 2019 Jayce Azua and Asim Zaidi. All rights reserved.
# ==================================================================================

# ----------------------------------------------------------------------------------
# Imports
# ----------------------------------------------------------------------------------
import os
import sys
import time
from hashtable import HashTable

# ----------------------------------------------------------------------------------
# CallRoutes (Class)
# ----------------------------------------------------------------------------------
class Hash_CallRouter(object):

    # ------------------------------------------------------------------------------
    # CallRoutes - Constructor
    # ------------------------------------------------------------------------------
    
    def __init__(self, carrier_route_path):
        """
            Create a new CallRoutes instance.
            Runtime: Θ(1) Space: Θ(1).
        """
        self.route_costs_hashtable = self.__convert_file_into_hashtable(carrier_route_path)

    # ------------------------------------------------------------------------------
    # CallRouter - Intended Private Methods
    # ------------------------------------------------------------------------------
    
    def __convert_file_into_hashtable(self, file_path):
        """
            Read route costs file into a dictionary and return the result.
            Runtime: Θ(n) Space: Θ(m)
            n = number of lines in file
            m = total entries in the hash table
        """
        hash_lookup = HashTable()
        with open('data/' + file_path, "r") as file:
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
        """
            Read phone numbers into a list and return the result.
            Runtime: Θ(n) Space: Θ(1)
        """

        with open('data/' + path_to_file, "r") as file:
           for line in file:
               line = line[:-1]
               cost = self.find_route_cost(line)
               self.write_cost(line, str(cost))
    
    # ------------------------------------------------------------------------------
    # CallRouter - Public Methods
    # ------------------------------------------------------------------------------
    
    def find_route_cost(self, phone_number):
        """
            Goes through phone number backwards to find matching route in hashtable.
            Args: phone_number:     phone number (string)
            Runtime: O(1*) Space: O(1)

            1* = 7 digits of phone number
        """
        for _ in phone_number:
            if self.route_costs_hashtable.contains(phone_number):
                cost = self.route_costs_hashtable.get(phone_number)
                return cost
            else:
                phone_number = phone_number[:len(phone_number)-1]
        return 0
        

    def write_cost(self, phone_number, cost):
        """
            Write phone number and cost to a new file
            Args:	phone_number:	phone number (string)
                    call_cost:		cost to call (string)
        """
        with open('data/' + "call-costs-2.txt", "a") as f:
            f.write(phone_number + ", " + cost + "\n")

def test_call_router():
    start = time.time()
    carrier_route_path = 'route-costs-106000.txt'
    call_router = Hash_CallRouter(carrier_route_path)
    load_time = round(time.time() - start, 4)
    print("\nBuilding the Hashtable took: {} seconds.".format(load_time))
    phone_number = 'phone-numbers-10000.txt'
    start = time.time()
    call_router.read_number(phone_number)
    load_time = round(time.time() - start, 4)
    print("\nLooking up 10000 numbers in a Hashtable took: {} seconds.".format(load_time))

# ------------------------------------------------------------------------------
# Memory Usage Function (Inspired by research)
# ------------------------------------------------------------------------------
def get_memory(): 
    pass


if __name__ == '__main__':
    print("\nInitializing Scenario 2...")
    test_call_router()

# Solution Trade off summary/analysis
# In this scenario we decided to store all our route
# costs into a hash table for constant look up time and iterate through the number backwards
# until we found a match. For the size of the data set this solution seemed appropriate here
# and it allows us to have constant look up time allowing the program to run very fast.
