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
