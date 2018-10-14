class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'<Node | Val: {self.value} | Left: {self.left} | Right: {self.right}>'