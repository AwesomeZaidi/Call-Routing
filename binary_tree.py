# !python


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.left is not None or self.right is not None
    

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""

        left_height = 0
        right_height = 0

        # if left child has a value, calculate its height
        if self.left:
            left_height = 1 +self.left.height()
        
        # if right child has a value, calculate its height
        if self.right:
            right_height = 1 +self.right.height()
    
        # Return the greater of the left height and right height + 1
        return 1 + max(left_height, right_height)

    

