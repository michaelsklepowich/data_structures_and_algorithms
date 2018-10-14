from .node import Node


class Stack:
    def __init__(self):
        self.top = None
        self._length = 0

    def __repr__(self):
        pass

    def __str__(self):
        """ starting at self.top, output intially assigned to front of stack and continues through concatinating onto output string
        """
        current_node = self.top
        output = f'(Head: {self.top})'
        while current_node:
            current_node = current_node._next
            output += f' -> (Next: {current_node})'
        return output + ''

    def __len__(self):
        """ returns self._length
        """
        return self._length

    def push(self, value):
        """ method which takes a value and add it to the top of the stack, then returns the newly-added value
        """
        self.top = Node(value, self.top)

        self._length += 1

        return self.top

    def pop(self):
        """ reassigns top value to top._next, removes and returns top value in the stack
        """
        tmp = self.top
        self.top = tmp._next
        tmp._next = None

        self._length -= 1
        return tmp.value

    def peek(self):
        """ returns the top of the stack without modifying the stack
        """
        return self.top