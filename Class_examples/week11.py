import time

# O(len(xs)) - linear
def sumlist(xs):
    """return the sum of the elems of xs

    sumlist(list(num)) -> num
    """
    r = 0
    for x in xs:
        r += x
    return r

# O(len(xs)**2) - quadratic
def rev1(xs):
    """Return the reverse of xs"""
    r = []
    for i in range(len(xs)):
        r.insert(0, xs[i])
    return r

# O(len(xs))
def rev2(xs):
    r = []
    for i in range(len(xs)-1, -1, -1):
        r.append(xs[i])
    return r



# O(a)
def mult(a, b):
    """return the product of a and b

    mult(int, int) -> int

    Precondition a >= 0
    """
    r = 0
    x = a
    y = b
    while x > 0:
        # loop invariant r + x * y == a*b
        x -= 1
        # r + x * y == r + y + (x-1)*y
        r += y
    return r


#now = time.time()
#mult(50000000, 25)
#print(time.time() - now)



# bitwise and
# consider the numbers (and their binary representation)
# 11 = 1011
#  6 = 0110
# then 11 & 6 is
# 1011 &
# 0110
# ----
# 0010
# (Think of 1 as True and 0 as False and '&' as 'and')
# So if we want to determine if a number is odd then we note that all odd 
# numbers have their "low bit set"
# e.g.
# 3 = 0011
# 5 = 0101
# 7 = 0111
# 2 = 0010
# 4 = 0100
# 6 = 0110
# and so if we & a number with 1 then all other bits in the result will be 0
# except possibly the low bit and so the result will be 1 iff the number
# is odd.

# bit shifting
# 4 = 0100 and so 4 >> 1 moves all bits to the right (down) by 1 to give
# 0010 = 2
# on the other hand 4 << 1 moves all bits to the left (up) to give
# 1000 = 8

# O(log(a)) - log 
def mult2(a, b):
    """return the product of a and b

    mult(int, int) -> int

    Precondition a >= 0
    """
    r = 0
    x = a
    y = b
    while x > 0:
        # loop invariant r + x * y == a*b
        if x & 1 == 1:  #x is odd
            x -= 1
            r += y
        #    x is even
        x >>= 1
        y <<= 1
        # r + (x/2)*(2*y) = r + x * y if x is even
        
    return r
#now = time.time()
#mult2(500000000000000, 25)
#print(time.time() - now)

# O(len(xs)**2)
# selection sort
def ssort(xs):
    """Sort the elems of xs in place"""
    for i in range(len(xs)):
        # loop invariant: sorted([xs[:i]) and xs[:i] =< xs[i:]
        m = xs[i]
        index = i
        for j in range(i, len(xs)):
            if xs[j] < m:
                m = xs[j]
                index = j
        xs[i], xs[index] = xs[index], xs[i]

# best case O(len(xs))
# worst case O(len(xs)**2)
# insertion sort
def isort(xs):
    """Sort the elems of xs in place"""
    for i in range(len(xs)):
        # loop invariant: sorted([xs[:i])
        j = i
        val = xs[i]
        while j > 0 and val < xs[j-1]:
            xs[j] = xs[j-1]
            j -= 1
        xs[j] = val

def merge(xs, ys):
    """Return the merge of sorted lists xs and ys"""
    xi = 0
    yi = 0
    r = []
    while xi < len(xs) and yi < len(ys):
        if xs[xi] < ys[yi]:
            r.append(xs[xi])
            xi += 1
        else:
            r.append(ys[yi])
            yi += 1
    r.extend(xs[xi:])
    r.extend(ys[yi:])
    return r

def msort(xs):
    if len(xs) < 2:
        return xs
    half = len(xs)//2
    return merge(msort(xs[:half]), msort(xs[half:]))


                     


