#!python
class TrieNode:
    def __init__(self):
        """Initialize this trie tree node with the given data."""
        self.children = [None] * 10 # 10 because numbers of routes 0-9
        self.cost = None # the value stored at the end of each path (route)

class Trie:
    def __init__(self):
        """Initialize this trie tree and insert the given items."""
        self.root = TrieNode()
        
    def get_node(self):
        return TrieNode()
    
    def get_index(self, key):
        return (ord(key) - ord('0'))
    
    def insert(self, route, cost):
        """Inserts the given cost into this trie tree."""
        current_node = self.root
        
        for i, d in enumerate(route):
            if route[i] == "+":
                continue
            index = self.get_index(d)
            # if current digit is not present
            if not current_node.children[index]:
                current_node.children[index] = self.get_node()
            current_node = current_node.children[index]
            
        if current_node.cost:
            if cost > current_node.cost:
                return
        current_node.cost = cost


    def search_and_return_cost(self, phone_number):
        current_node = self.root
        cost = 0
        for i, d in enumerate(phone_number):
            if phone_number[i] == "+":
                continue
            index = self.get_index(d)

            if current_node.children[index] != None:
                current_node = current_node.children[index]
                if current_node.cost != None:
                    cost = current_node.cost

        if current_node.cost != None:
            return current_node.cost
        else: 
            return cost

