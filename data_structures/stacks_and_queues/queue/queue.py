from .node import Node


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self._length = 0

    def __repr__(self):
        pass

    def __str__(self):
        """ starting at self.front, output intially assigned to front of queue and continues through concatinating onto output string
        """
        if not self.front:
            return 'Empty Queue'
        current_node = self.front
        output = f'(Head: {self.front})'
        while current_node:
            current_node = current_node._next
            output += f' -> (Next: {current_node})'
        return output + ''

    def __len__(self):
        """ returns the self._length
        """
        return self._length

    def enqueue(self, value):
        """Method which accepts a value, sets self.back to the newly created node and returns the created node
        """
        if not self.front:
            self.front = Node(value)
        else:
            newNode = Node(value)
            current = self.front
            while current._next:
                current = current._next
            current._next = newNode
            self.back = Node(value)

        self._length += 1

        return self.front

    def dequeue(self):
        """Method takes no arguments and removes and returns the first value in the queue using temporary variable to keep reference to self.head
        """
        temp = self.front
        self.front = tmp._next
        temp._next = None

        self._length -= 1
        return temp.value

    def peek(self):
        """ no arguments aside from self to be able to return self.front
        """
        return self.front