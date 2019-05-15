# !python

# ==================================================================================
# File: solution_1.py
#
# One-time route cost check
# Desc: You have a carrier route list with 100,000 (100K) entries (in arbitrary order)
# and a single phone number. How quickly can you find the cost of calling this number?

# Copyright © 2019 Jayce Azua and Asim Zaidi. All rights reserved.
# ==================================================================================

import os
import re
import sys
import time
import mmap
import random
import resource
import platform

def parse_file(file_name):
	"""
		Opens the file and splits the routes and costs into a list.
		Args: file_name - name of route-costs file (string)
		Returns: route_costs_data - route costs [+123, 0.4, +234, 0.3.. etc.] (list) 
		Runtime: O(n) -> n = number of lines in the file
	"""
	with open('data/' + file_name, "r") as file:
		route_costs_data = file.read()
		route_costs_data = re.split(',|\n', route_costs_data)
	return route_costs_data 

def find_call_cost(route_costs, phone_number):
	"""
		Finds the longest route match for the given phone number and returns the cost.
		Args:	route_costs:	Numbers and their costs [+123, 0.5, +456, 0.3... etc]
				phone_number:	phone number (string)
		Returns: lowest call cost matching the phone number in routes or 0 if nothing is found.
		Runtime: O(n) -> O(p*n)
		p = len of phone_number
		n = len of number_data list
	"""
	for _ in phone_number:
		if phone_number in route_costs:
			real_index = route_costs.index(phone_number)
			return str(route_costs[real_index + 1])
		else:
			phone_number = phone_number[:len(phone_number)-1]

	return str(0) # if number not found

def write_cost(phone_number, call_cost):
	"""
		Write phone number and cost to a new file
		Args:	phone_number:	phone number (string)
				call_cost:		cost to call (string)
	"""
	f = open('data/' + "call-costs-1.txt", "w")
	f.write(phone_number + ", " + call_cost)


# ------------------------------------------------------------------------------
# Memory Usage Function (Inspired by research)
# ------------------------------------------------------------------------------
def get_memory(): 
    pass

if __name__ == "__main__":
	start = time.time()
	print("\nInitializing Scenario 1...")
	route_costs_data = parse_file("route-costs-106000.txt")
	load_time = round(time.time() - start, 4)
	print("\nParsing data took: {}.".format(load_time))
	start = time.time()
	phone_number = '+14152348111'
	call_cost = find_call_cost(route_costs_data, phone_number)
	load_time = round(time.time() - start, 4)
	print("\nSingle phone search took: {}.".format(load_time))
	write_cost(phone_number, call_cost)
	
	


# Our the manual solution inspired by Nicoli Safai
# 0. Copy full phone number.
# 1. Open routes file.
# 2. Search for phone number using `CMD+F` (or `CTRL+F` on windows).
# - If there are no search results, hit `backspace` in search bar.
# 3. Repeat `Step 2` til you find a match.
# - In the unlikely event you get several matches, choose the cheapest.
# If you found a match in Step 3, the cost is the number on the right side of the comma.

# Solution Trade off summary/analysis
# In this scenario we needed the quickest implementation possible and didn't have the
# development time to create an optimized solution. We decided to store all our route
# costs into a list and iterate through it in O(n) time to try and find a matching
# route for our given phone number.
