def add(n, m):
    """Return the result of adding n and m"""

    return n+m

def add2(n,m):
    print(n+m)


def size(n):
    """Return 'One', 'Two', 'Many' depending on n"""

    if n == 1:
        result = "One"
    elif n == 2:
        result = "Two"
    else:
        result = "Many"
    return result
    
def sumto(n):
    """Return the sum of numbers from 1 to and including n"""

    total = 0
    m = 1
    while n >= m:
        total = total + m  # total += m is a shorthand
        m += 1
    return total
