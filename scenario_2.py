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

class CallRouter(object):

    # function to convert phone_numbers file into a list of numbers
    # function to convert route_costs into a hash set with lowest costs for routes

    # function to find the lowest cost of a number in the route_costs hash set
    
    # go through our phone_numbers list and run each one in find_lowest_price_for_number
    # write each number and its cost into a text file.

    def __init__(self, phone_numbers_path, route_prices_path):
        self.phone_numbers = self.parse_phone_numbers(phone_numbers_path)
        # self.parse_routes()

    def convert_file_into_array(self, path_to_file):
        """Turns txt file into list without '\n' or '+' characters"""
        file = open(path_to_file, 'r')
        file_content = file.read() # string representation of .txt file
        file.close()
        # (1) Remove '+', turn into array and (2) remove last (empty) item
        array = re.sub(r'\+', "", file_content).split('\n')
        array.pop() # remove last item of array which is empty
        return array

    def parse_phone_numbers(self, phone_numbers_path):
        """Turns txt file into list of phone numbers without the +"""
        return self.convert_file_into_array(phone_numbers_path)

    def parse_routes(self, carrier_routes_path):
        pass

    # Solve for each first number in phone_numbers file and write to file.

def test_call_router():
    phone_numbers_path = 'data/phone-numbers-1000.txt'
    route_prices_path = 'data/route-costs-1000.txt'
    call_router = CallRouter(phone_numbers_path, route_prices_path)
    # Look up costs
    # results_array = call_router.save_routing_costs(call_router.phone_numbers)
    # for result in results_array:
    #   print(result)

if __name__ == '__main__':
    test_call_router()
