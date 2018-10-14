class Node:
    def __init__(self, value, _next=None):
        self._value = value
        self._next = _next

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'<Node | Val: {self._value} | Next: {self._next}>'
