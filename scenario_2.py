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
    def __init__(self, phone_numbers_path, route_prices_path):
        self.phone_numbers = self.parse_phone_numbers(phone_numbers_path)
    
    def turn_txt_file_into_array(self, path_to_file):
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
        return self.turn_txt_file_into_array(phone_numbers_path)


# def read_file(file_name): <- our data structure to look up
# 	"""
# 		Opens the file and splits the numbers into a list.
# 	"""
# 	with open('data/' + file_name, "r") as file:
# 		number_data = file.read()
# 		number_data = re.split(',|\n', number_data)
# 	return number_data


# def find_route_cost(number_data, phone_number):
	# for _ in phone_number:
	# 	if phone_number in number_data:
	# 		real_index = number_data.index(phone_number)
	# 		return str(number_data[real_index + 1])
	# 	else:
	# 		phone_number = phone_number[:len(phone_number)-1]

	# return str(0)  # if number not found
