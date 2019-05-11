# !python

# ==================================================================================
# File: solution_1.py
#
# One-time route cost check
# Desc: You have a carrier route list with 100,000 (100K) entries (in arbitrary order)
# and a single phone number. How quickly can you find the cost of calling this number?

# Copyright © 2019 Jayce Azua and Asim Zaidi. All rights reserved.
# ==================================================================================

# By hand:
# Step 0: Copy full phone number.
# Step 1: Open routes file.
# Step 2: Search for phone number using CMD+F (or CTRL+F on windows).
#         If there are no search results, hit backspace in search bar.
# Step 3: Repeat Step 2 til you find a match.
#         In the unlikely event you get several matches, choose the cheapest.
# If you found a match in Step 3, the cost is the number on the right side of the comma.
# Otherwise, we don't have a matching route, tell your manager sorry.

# By code:

import sys
import re

def read_file(file_name):
	"""
		Opens the file and splits the numbers into a list.
	"""
	with open('data/' + file_name, "r") as file:
		number_data = file.read()
		number_data = re.split(',|\n', number_data)
	return number_data

def find_route_cost(number_data, phone_number):
	"""
		number_data: list of number, cost, number, cost, etc.
		Finds the longest route match and returns the associated cost.
		Runtime: O(n)- O(p*n)
		p = len of phone_number
		n = len of number_data list
	"""
	for _ in number_data[::2]:
		if phone_number in number_data:
			real_index = number_data.index(phone_number)
			return str(number_data[real_index + 1])
		else:
			phone_number = phone_number[:len(phone_number)-1]

	return str(0) # if number not found

def write_cost(phone_number, cost):
	f = open("route-costs-1.txt", "w")
	f.write(phone_number + ", " + number_route_cost)

if __name__ == "__main__":
	#  scenario playing like how Edwin had it.
	paths = read_file("phone-numbers-3.txt")  # phone-numbers
	phone_number = '+141523481111'
	number_route_cost = find_route_cost(paths, phone_number)
	write_cost(phone_number, number_route_cost)


