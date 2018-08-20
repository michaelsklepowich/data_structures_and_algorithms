from .node import Node
from typing import Any


class LinkedList(object):
    def __init__(self):
        self.head: Node = None
        self._length: int = 0

    def __str__(self):
        return f'Head: {self.head} | Length: {self._length}'

    def __repr__(self):
        return f'<Linked List | Head: {self.head} | Length: {self._length}>'

    def __len__(self):
        return self._length
 
    # def __iter__(self):
    #     pass
    #
    # def __next__(self):
    #     pass

    def insert(self, val: Any) -> Node:
        if self._length == 0:
            self.head = Node(val, self)
            self._length += 1
            print(self.head._next)
            return self
        else:
            self.head._next = Node(val, None)
        self._length += 1    


        

    # def includes(self, val: str, data: int) -> bool:
    def includes(self, val: Any) -> bool:
        counter = 0
        test = self._length
        while counter < test:
            if self.head.val == val:
                print(self.head.val, val, 'hitting true')
                return True
            print(self.head._next, 'hitting')    
            self = self.head._next
            counter += 1
        return False       