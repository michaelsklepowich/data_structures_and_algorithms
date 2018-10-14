
from hash_table import HashTable


def left_join(hash1, hash2):
    """ combines the values into matching keys from hash1 and hash2 into a new hash table
    """
    output = []
    idx = 0
    for i in range(0, len(hash1.hashtable)):
        if hash1.hashtable[i] and hash2.hashtable[i]:
            output.append(hash1.get(hash1.hashtable[i][0][0])[0])
            output[idx].append(hash2.get(hash2.hashtable[i][0][0])[0][1])
            idx += 1
        elif hash1.hashtable[i]:
            output.append(hash1.get(hash1.hashtable[i][0][0])[0])
            output[idx].append('none')
            idx += 1

    return output