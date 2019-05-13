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

        if node.cost is not None:
            if cost > node.cost:
                return
        node.cost = cost

    def search(self, phone_number: str) -> str:
        """Searches for a phone number in trie and returns cost"""
        """Return the cost of a longest route in this trie search tree matching the given phone number"""
        node = self.root
        cost = 0

        for number in phone_number:
            number = int(number)
            if node.children[number] is not None:
                node = node.children[number]
                if node.cost is not None:
                    cost = node.cost
        # return the cost at node if there is one
        # if not, return the higher cost stored in the tree
        return node.cost if node.cost is not None else cost
