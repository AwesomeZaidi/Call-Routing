# !python

# ==================================================================================
# File: scenario_3.py

# You have 5 carrier route lists, each with 10,000,000 (10m) entries (in arbitrary order)
# and a list of 10,000 phone numbers. How can you speed up your route cost lookup
# solution to handle this larger dataset

# Copyright © 2019 Jayce Azua and Asim Zaidi. All rights reserved.
# ==================================================================================

import re
import os
import glob


class TrieNode:
  def __init__(self, value=None):
      self.value = value
      self.dictionary = {}
      self.cost = None

class Trie:
  def __init__(self, files):
    self.root = TrieNode()
    for file in files:
      self.buildTrieOfRoutes(file)

  def buildTrieOfRoutes(self, file):
    """
      Takes in a file with lines of 'route,costs' and builds a Trie of the routes' digits.
    """
    for line in open(file):
      current = self.root
      route, cost = line.split(",")
      cost = float(cost.strip("\n"))
      for digit in route:
        if digit not in current.dictionary:
            current.dictionary[digit] = TrieNode(digit)
        current = current.dictionary[digit]
      if current.cost:
        if current.cost > cost:
            current.cost = cost
      else:
        current.cost = cost

  def findLowestCostsAndPrintThemToFile(self, file):
    """Finds the lowest costs for each phone number in the input file."""

    for phoneNumber in open(file):
      current = self.root
      minimum = float('inf')
      for digit in phoneNumber:
        if digit in current.dictionary:
          if current.cost:
              minimum = min(minimum, current.cost)
          current = current.dictionary[digit]
        else:
          phoneNumber = phoneNumber.strip("\n")
          if minimum != float('inf'):
              with open("output_logs/route-costs-3.txt", "a+") as f:
                      f.write(phoneNumber + ", " + str(minimum) + '\n')
          else:
              with open("output_logs/route-costs-3.txt", "a+") as f:
                      f.write(phoneNumber + ", 0 \n")
          break  # break out of the 'for digit in phoneNumber' loop
          # and start on the next phoneNumber.

# ideas: sorting our data:
class Quick_Sort(object):
  def __init__(self, arbitrary_order):
    pass

  def quick_sort(self, arbitrary_order):
    self.quick_sort2(arbitrary_order, 0, len(arbitrary_order)-1)

  def quick_sort2(self, arbitrary_order, low, high):
    if low < high:
      p = self.partition(arbitrary_order, low, high)
      self.quick_sort2(arbitrary_order, low, p - 1)
      self.quick_sort2(arbitrary_order, p + 1, high)

  def get_pivot(self, arbitrary_order, low, high):
    mid = (high + low) // 2
    pivot = high
    if arbitrary_order[low] < arbitrary_order[mid]:
      if arbitrary_order[mid] < arbitrary_order[high]:
        pivot = mid
    elif arbitrary_order[low] < arbitrary_order[high]:
      pivot = low
    return pivot

  def partition(self, arbitrary_order, low, high):
    pivotIndex = self.get_pivot(arbitrary_order, low, high)
    pivotValue = arbitrary_order[pivotIndex]
    arbitrary_order[pivotIndex], arbitrary_order[low] = arbitrary_order[low], arbitrary_order[pivotIndex]
    border = low

    for i in range(low, high + 1):
      if arbitrary_order[i] < pivotValue:
        border += 1
        arbitrary_order[i], arbitrary_order[border] = arbitrary_order[border], arbitrary_order[i]
    arbitrary_order[low], arbitrary_order[border] = arbitrary_order[border], arbitrary_order[low]
    return border


if __name__ == "__main__":
  pass
