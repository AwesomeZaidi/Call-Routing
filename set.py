from hashtable import HashTable


class HashSet (object):
  # initializer
  def __init__(self, elements=None):
    self.container = HashTable()
    self.size = self.container.size
    if elements is not None:
      for item in elements:
        self.add(item)

  def __str__(self):
    """Return a formatted string representation of this hash table."""
    items = ["{!r}".format(key) for key, _ in self.container.items()]
    return "{" + ", ".join(items) + "}"

# Part 1
  def add(self, element):
    if self.contains(element):
      return  # simply do nothing - Anisha
    self.size += 1
    self.container.set(element, None)

  def remove(self, element):
    if self.size == 0:
      raise ValueError("Nothing to remove, set is empty")
    self.size -= 1
    self.container.delete(element)

  def contains(self, element):
    return self.container.contains(element)

# Part 2
  def union(self, other_set):
    union = HashSet()
    for key, _ in self.container.items():
      union.add(key)

    for key, _ in other_set.container.items():
      if not self.contains(key):
        union.add(key)
    return union

  def intersection(self, other_set):
    union = HashSet()
    for key, _ in self.container.items():
      if other_set.contains(key):
        union.add(key)
    return union

  def difference(self, other_set):
    union = HashSet()
    for key, _ in self.container.items():
      if not other_set.contains(key):
        union.add(key)
    return union

  def is_subset(self, other_set):
    for key, _ in self.container.items():
      if not other_set.contains(key):
            return False
    return True


if __name__ == "__main__":
  names = ["Winnie", "Kojin", "Brian", "Nabil", "Julia", "Alex", "Nick"]
  s = HashSet(names)
