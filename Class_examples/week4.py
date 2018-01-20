
def double(xs):
    """Return the list of the doubles of the elems of xs

    double(list(int)) -> list(int)
    """
    result = []
    for x in xs:
        result.append(2*x)
    return result

def evens(xs):
    """Return the even elems of xs

    evens(list(int)) -> list(int)
    """
    result = []
    for x in xs:
        if x % 2 == 0:
            result.append(x)
    return result

