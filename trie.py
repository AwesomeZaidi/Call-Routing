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
        
        for i, _ in enumerate(route):
            if route[i] == "+":
                continue
            index = self.get_index(route[i])
            # if current digit is not present
            if not current_node.children[index]:
                current_node.children[index] = self.get_node()
            current_node = current_node.children[index]
            
        if current_node.cost:
            if cost > current_node.cost:
                return
        current_node.cost = cost








    # def search(self, phone_number: str) -> str:
        # """Searches for a phone number in trie and returns cost"""
        # print('in trie search')
        # node = self.root
        # print('node:', node)
        # cost = 0

        # for number in phone_number:
        #     print('number')
        #     number = int(number)
        #     if node.children[number] is not None:
        #         node = node.children[number]
        #         if node.cost is not None:
        #             cost = node.cost

        # # return the cost at node if there is one
        # # if not, return the higher cost stored in the tree
        # return node.cost if node.cost is not None else cost
