#!python

class TrieNode:
    def __init__(self):
        """Initialize this trie tree node with the given data."""
        self.children = [None] * 10 # 10 because numbers of routes 0-9
        self.cost = None # the value stored at the end of each path (route)

    def __repr__(self):
        """Return a string representation of this trie tree node."""
        return f"NODE({self.children})"

class Trie:
    def __init__(self):
        """Initialize this trie tree and insert the given items."""
        self.root = TrieNode()
        self.size = 0

    def __repr__(self):
        "return a string represention of this trie tree"
        return 'size: {}'.format(self.size)
    
    def insert(self, phone_number: str, cost: int):
        """Inserts the given item into this trie tree."""
        node = self.root

        for number in phone_number:
            number = int(number)
            print(node)
            # if there's no child node, create it where we want it, at the number.
            if node.children[number] is None: 
                node.children[number] = TrieNode()
            # otherwise, set the node to that nodes child number.
            node = node.children[number]