
from .linked_list import LinkedList


def ll_merge(linked_list_1, linked_list_2):
    """ function takes two linked lists and "zips" them together by taking alternating
    heads from each list and then adding them into one list for the length of the longest list
    """
    prime = LinkedList()
    if linked_list_1._length > linked_list_2._length:
        cur1 = linked_list_1.head
        cur2 = linked_list_2.head
        prime = linked_list_1

    cur1 = linked_list_2.head
    cur2 = linked_list_1.head
    prime = linked_list_1

    while cur1:
        prime.insert(cur1.val)
        prime.insert(cur2.val)
        cur1 = cur1._next
        cur2 = cur2._next

    return prime