#!python

class TrieNode:
    def __init__(self):
        """Initialize this trie tree node with the given data."""
        self.children = [None] * 10 # 10 because numbers of routes 0-9
        self.cost = None # the value stored at the end of each path (route)
        self.leaf = False

    def __repr__(self):
        """Return a string representation of this trie tree node."""
        return f"NODE({self.children})"

class Trie:
    def __init__(self):
        """Initialize this trie tree and insert the given items."""
        self.root = self.get_node()
        self.root.cost = "+"
        self.size = 0

    def __repr__(self):
        "return a string represention of this trie tree"
        return 'size: {}'.format(self.size)

    def get_node(self):
        return TrieNode()
    
    def get_index(self, key):
        return (ord(key) - ord('0'))
    
    def insert(self, route, cost):
        """Inserts the given cost into this trie tree."""
        node = self.root
        length = len(route)
        for level in range(length):
            index = self.get_index(route[level])
            # if current character is not present
            if not node.children[index]:
                node.children[index] = self.get_node()
                self.size += 1
            node = node.children[index]

        node.leaf = True
        
        if node.cost is not None:
            if cost > node.cost:
                return
        node.cost = cost

    def search(self, phone_number: str) -> str:
        """Searches for a phone number in trie and returns cost"""
        print('in trie search')
        node = self.root
        print('node:', node)
        cost = 0

        for number in phone_number:
            print('number')
            number = int(number)
            if node.children[number] is not None:
                node = node.children[number]
                if node.cost is not None:
                    cost = node.cost

        # return the cost at node if there is one
        # if not, return the higher cost stored in the tree
        return node.cost if node.cost is not None else cost
