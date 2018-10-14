from .stack import Stack


def multi_braket_validation(in_string):
    """ Validates that the string, if contianing brakets closes them correctly
        by using a stack to make sure that every value has been properly "addressed"
    """
    openings = ['[', '(', '{']
    closings = [']', ')', '}']
    #using a stack to make sure that each push bracket is addressed in a FILO fashion
    stack = Stack()
    for i in range(len(in_string)):
        if in_string[i] in openings:
            stack.push(in_string[i])
        if in_string[i] in closings:
            if len(stack) == 0:
                return False
            #making sure the open bracket matches the closed bracket
            elif openings[closings.index(in_string[i])] != stack.top.val:
                return False
            else:
                stack.pop()
    if len(stack) > 0:    
        return False
    
    return True
        