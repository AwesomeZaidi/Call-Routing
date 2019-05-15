#!python
class TrieNode:
    def __init__(self):
        """Initialize this trie tree node with the given data."""
        # self.children = [None] * 10 # 10 because numbers of routes 0-9
        self.children = {}
        self.cost = None  # the value stored at the end of each path (route)

    def __repr__(self):
        return "TrieNode({} children)".format(len(self.children))


class Trie:
    def __init__(self):
        """Initialize this trie tree and insert the given items."""
        self.root = TrieNode()

    def get_node(self):
        return TrieNode()

    # def get_index(self, key): # might not need this.
    #     return (ord(key) - ord('0'))

    def insert(self, route, cost):
        """Inserts the given cost into this trie tree."""
        current_node = self.root

        for d in route:
            if d not in current_node.children:
                current_node.children[d] = self.get_node()
            current_node = current_node.children[d]

        if current_node.cost:
            if cost > current_node.cost:
                return
        current_node.cost = cost

    def search_and_return_cost(self, phone_number):
        current_node = self.root
        cost = 0
        for d in phone_number:

            if d in current_node.children:
                current_node = current_node.children[d]
                if current_node.cost != None:
                    cost = current_node.cost

        if current_node.cost != None:
            return current_node.cost
        else:
            return cost


if __name__ == "__main__":
    pass
    # use this as test
    # route = "+415890"
    # cost = "0.045"
    # test_trie = Trie()
    # test_trie.insert(route, cost)
    # print(test_trie.search_and_return_cost("+4158901111"))
    # print(bool(test_trie.root.children["+"].children["4"].children["1"].children["5"].children["8"].children["9"].children["0"].children))
