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
from set import HashSet 

class CallRouter(object):

    # function to convert phone_numbers file into a list of numbers
    # function to convert route_costs into a hash set with lowest costs for routes

    # function to find the lowest cost of a number in the route_costs hash set
    
    # go through our phone_numbers list and run each one in find_lowest_price_for_number
    # write each number and its cost into a text file.

    def __init__(self, phone_numbers_path, carrier_route_path):
        self.phone_numbers = self.parse_phone_numbers(phone_numbers_path)
        self.parse_carrier_routes(carrier_route_path)

    def convert_file_into_array(self, path_to_file):
        """Turns txt file into list without '\n'"""
        with open('data/' + path_to_file, "r") as file:
            data = file.read()
            data = re.split(',|\n', data)
        return data

    def parse_phone_numbers(self, phone_numbers_path):
        """Turns txt file into list of phone numbers without the +"""
        return self.convert_file_into_array(phone_numbers_path)

    def convert_file_into_hashset(self, path_to_file):
        """Turns txt into hash set"""
        with open('data/' + path_to_file, "r") as file:
            data = file.readline()

            # data = re.split(',|\n', data)
        return data

    def parse_carrier_routes(self, carrier_routes_path):
        """Turns txt file into a hash set with routes and costs"""
        return self.convert_file_into_array(carrier_routes_path)


def test_call_router():
    phone_numbers_path = 'data/phone-numbers-1000.txt'
    carrier_route_path = 'data/route-costs-100.txt'
    call_router = CallRouter(phone_numbers_path, carrier_route_path)
    return call_router

if __name__ == '__main__':
    print(test_call_router())
