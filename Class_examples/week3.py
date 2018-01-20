
def get_index(char, string):
    """Return the index of the first char in string.
    If not there return -1

    get_index(str, str) -> int
    """
    for i, c in enumerate(string):
        if c == char:
            return i
    return -1

def get_all_indexes(char, string):
    """Return a tuple of all the indexes of char in string

    get_all_indexes(str, str) -> tuple(str)
    """
    result = ()
    for i, c in enumerate(string):
        if c == char:
            result += (i,)
    return result

    
