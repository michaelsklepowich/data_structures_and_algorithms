import Tree from './tree.py'
import Node from './node.py'

def find_max_value(binary_tree):
    """This function takes a binary tree and returns the largest value of all the nodes in that tree
    with O(N) space and O(1) time using breadth first traversal while keeping track of the largest value thus far
    in the traversal
    """

    root_node = []
    rootnode.push(binary_tree.root)
    output = []
    
    # helper function
    def is_Null(current_value):
        """this is a helper function to check if the value of all nodes in breadth first traversal have null values
        which means we have gone off the bottom depth of the tree and returns a boolean"""
        return current_value == null

    def _walk(input_list):
        """This is the recursive function in our breadth first traversal which implements a queue without the queue class
        this function returns the value of each node until all node values are returned; the base case is when all
        values of the nodes are null, which means we have gone off the bottom depth of the tree
        """    
        counter = 0
        largest_value = 0
        newNodes = []
        while counter < len(input_list):
            if input_list[counter]:
                if input_list[counter].value > largest_value:
                    largest_value = input_list[counter]
                print('new value: ', input_list[counter])
                output.push(input_list[counter])
                newNodes.push(input_list[counter].left)
                newNodes.push(input_list[counter].right)
        print('newNodes: ', len(newNodes), '\n', newNodes)
        if not all is_Null(newNodes):
            _walk(newNodes)

        _walk(root_node)   
        return 'largest value ' + largest_value

