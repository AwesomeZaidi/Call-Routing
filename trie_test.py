import unittest
from trie import TrieNode, Trie


class TrieNode_Test(unittest.TestCase):
    def test_init(self):
      data = "ABC"
      trie_node = TrieNode()
      assert bool(trie_node.children) == False
      assert len(trie_node.children) == 0
      assert trie_node.cost == None
      trie_node.children[data] = True
      assert trie_node.children[data] == True


class Trie_Test(unittest.TestCase):
  def test_init(self):
    trie_tree = Trie()
    data = "ABC"
    assert bool(trie_tree.root.children) == False
    assert len(trie_tree.root.children) == 0
    assert trie_tree.root.cost == None
    trie_tree.root.children[data] = True
    assert trie_tree.root.children[data] == True

  def test_insert(self):
    trie_tree = Trie()
    keys = "ABC"
    value = "FOUND ME"
    trie_tree.insert(keys, value)
    assert len(trie_tree.root.children) == 1
    assert trie_tree.root.children["A"].cost == None
    assert trie_tree.root.children["A"].children["B"].cost == None
    assert trie_tree.root.children["A"].children["B"].children["C"].cost == value


  def test_search_and_return_cost(self):
    trie_tree = Trie()
    route = "+415890"
    cost = "0.045"
    trie_tree.insert(route, cost)
    assert len(trie_tree.root.children) == 1
    assert trie_tree.search_and_return_cost(route) == cost
