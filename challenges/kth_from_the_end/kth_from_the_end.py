import LinkedList from ./linked_list.py

def kth_from_the_end(self, input_list):
    """ this function takes a list as input and traveres the entire list, 
        then from the end moves backwards k times
    """
        var2 = 0
        current = input_list.head

        while current._next:
            var2 += 1
            current = current._next
        
        front_index = var2 - arg
        current = input_ist.head
        while front_index != 0:
            front_index -= 1
            current = current._next

        return current.val
            