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
        """
        this method creates a new node and appends to the front of the list
        """
        if self._length == 0:
            self.head = Node(val, self.head)
            self._length += 1
            print(self.head._next)
            return self
        else:
            self.head._next = Node(val, None)
        self._length += 1    


        

    # def includes(self, val: str, data: int) -> bool:
    def includes(self, val: Any) -> bool:
        """
        this method checks to see if any value exists within a node and returns a boolean
        """
        print('head:', self.head)
        current = self.head
        while current is not None:
            if current.val == val:
                print(current.val, val, 'hitting true')
                return True 
            current = current._next
        print(self)    
        return False       

    def insert_before(self, i_data, s_data):
        '''
        Add a new node with the given i_data immediately after the first s_data node
        O(n) time.
        '''
        if self._head is not None:

            curr = self._head
            n = Node(i_data)

            if self._head._data == s_data:
                n._next, self._head = curr, n
                self._length += 1
            else:
                prev = None
                while curr:
                    if curr._data == s_data:
                        n._next, prev._next = curr, n
                        self._length += 1
                    prev, curr = curr, curr._next

    def insert_after(self, i_data, s_data):
        '''
        Add a new node with the given i_data immediately after the first s_data node
        O(n) time.
        '''
        if self._head is not None:

            if self._head._data == s_data:
                self._head._next = Node(i_data, self._head._next)
                self._length += 1

            else:
                curr = self._head
                while curr:
                    if curr._data == s_data:
                        curr._next = Node(i_data, curr._next)
                        self._length += 1
                    curr = curr._next