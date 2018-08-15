
def insert_shift_array(array, value):
    middle = len(array) // 2
    new_array = []
    counter = 0
    while (counter < len(array) +1):
        new_array[counter] = array[counter]
        if (counter == middle):
            new_array[counter] = value
            counter += 1
        counter += 1
    print(new_array)        