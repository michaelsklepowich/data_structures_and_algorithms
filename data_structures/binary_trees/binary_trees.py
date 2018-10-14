from .node import Node


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        # number of nodes (?)
        self.length = 0

    def __repr__(self):
        return f'this is the tree aranged in a pre_order structure {pre_order(self)}'

    def __str__(self):
        return f'this is the tree aranged in a pre_order structure {pre_order(self)}'

    def __len__(self):
        """ returns number of nodes in the tree
        """
        return self.length

    def pre_order(self):
        """ as soon as a node is visited it is added to the output
        """
        results = list()

        def _walk(node):
            """ recursive helper function which traverses all left then all right nodes
            """
            results.append(node.val)
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            self.length += 1  
        if self.root:
            _walk(self.root)

        return results

    def post_order(self):
        """ after all nodes have been traversed return the output
        """
        results = list()

        def _walk(node):
            """ recursive helper function which traverses all left then right nodes and then appends them to the output
            """
            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)
            self.length += 1    
            results.append(node.val)

        _walk(self.root)

        return results

    def in_order(self):
        """ returns tree in order of all left nodes then all right nodes
        """
        results = list()

        def _walk(node):
            """ recursive helper function which appends all left nodes before calling itself on right nodes
            """
            if node.left:
                _walk(node.left)

            results.append(node.val)

            if node.right:
                _walk(node.right)
            self.length += 1    
        _walk(self.root)

        return results

def insert(item, self):
    """ based on the value inserted and the current nodes in the tree, 
        deteremine where to put the inserted value
    """
    if (item < self.root):
        if (self.left != None):
            insert(item, self.left)
        else:
            self.left = BinaryTree(item)
    else:
        if (self.right != None):
            insert(item, self.right)
        else:
            self.right = BinaryTree(item)