import Tree from ./tree.py

def find_max_value(tree):
    max_value = 0
    def _walk(node):
        if node.val > max_value:
            max_value = node.val
        if node.left:
            _walk(node.left)
        if node.right:
            _walk(node.right)        
    _walk(tree.root)
    return max_value