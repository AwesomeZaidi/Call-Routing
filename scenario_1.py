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
	print('phone number:', phone_number)
	# for every other element in number_data:
	for index, element in enumerate(number_data[::2]):
		print('element:', element)
		if phone_number in number_data:
			print('found number in number_data')
			return number_data[index+2]
		else:
			phone_number = phone_number[:index-1]
			print('new phone_number:', phone_number)
	# if number not found
	return 0



  # if phone_number not in number_data:
	# 	index -= 1
	# 	phone_number = phone_number[:index]
# write to a new text file with the answer

if __name__ == "__main__":
	#  scenario playing like how Edwin had it.
	paths = read_file("route-costs-4.txt")
	# print(paths)
	number_route_cost = find_route_cost(paths, '+14152348')
	print(number_route_cost)
	