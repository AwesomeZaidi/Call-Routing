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
	file = open(file_name, "r")
	number_data = file.read()
	file.close()
	number_data = re.split(',|\n', number_data)
	return number_data

#  find the longest prefix match

# write to a new text file with the answer

if __name__ == "__main__":
  #  scenario playing like how Edwin had it.
	pass
	