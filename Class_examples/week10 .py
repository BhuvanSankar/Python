def sumto(n):
    """ Return the sum of numbers from 0 to n

    sumto(int) -> int

    Precondition: n >= 0
    """

    if n == 0:
        # base case
        return 0
    else:
        print("n = ", n)
        m = sumto(n-1)
        print("m = ", m)
        return m + n



def is_palindrome(s):
    """Return True iff s is a palindrome

    is_palindrome(str) -> boolean
    """

    if len(s) < 2:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[1:-1])

    
def max_of_list(xs):
    """Return the max elem of a non-empty list

    max_of_list(list(X)) -> X
    """
    if len(xs) == 1:
        return xs[0]
    else:
        m = max_of_list(xs[1:])
        if m < xs[0]:
            return xs[0]
        else:
            return m


class Cons(object):
    def __init__(self, head, tail = None):
        self._head = head
        self._tail = tail

    def head(self):
        return self._head

    def tail(self):
        return self._tail

    def is_empty_tail(self):
        return self._tail == None

    def __repr__(self):
        return "Cons({0}, {1})".format(self._head, self._tail)


c1 = Cons(1, Cons(2,Cons(3)))

c2 = Cons(4, Cons(5))


def member_cons(x, clist):
    """Return True iff x is in clist

    member_cons(X, Cons(X)) -> boolean
    """
    if clist.is_empty_tail():
        return x == clist.head()
    else:
        return x == clist.head() or member_cons(x, clist.tail())



def append_cons(cl1, cl2):
    """Return the cons list obtained by appending cl1 and cl2

    append_cons(Cons(X), Cons(X)) -> Cons(X)
    """
    if cl1.is_empty_tail():
        return Cons(cl1.head(), cl2)
    else:
        return Cons(cl1.head(), append_cons(cl1.tail(), cl2))

                    
    






### Towers of Hanoi


def towers(from_, to, other, n, d):
    """ Print out instructions for moving a tower of
    n disks from the from_ slot to the to slot.
    d is not really required
    """
    if n == 0:
        return
    else:
        towers(from_, other, to, n-1, d+1)
        print(2*d*' '+"Move disc from {0} to {1}".format(from_, to))
        towers(other, to, from_, n-1, d+1)

#towers('A', 'B', 'C', 6, 0)



### Kosh snowflake


import turtle
# turtle.reset()  - reset the turtle
# turtle.up() down() - lift/drop pen
# turtle.left(angle) right(angle) - turn
# turtle.forward(dist) - move forward
# turtle.color(colour) - change colour
# turtle.begin_fill() turtle.end_fill()- start/stop filling
# turtle.speed(speed) - set speed - 'fast' 'fastest'

def eg():
    turtle.reset()
    turtle.up()
    turtle.goto(-200,-150)
    turtle.down()
    turtle.speed('fastest')
    turtle.begin_fill()
    turtle.color('blue')
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)
    turtle.forward(400)
    turtle.left(120)
    turtle.end_fill()

#eg()
#input('')

def koch(depth, size):
    """Draw a kosh snowflake to given depth and size"""
    turtle.reset()
    turtle.up()
    turtle.goto(-200,-150)
    turtle.down()
    koch_edge(depth, size)
    turtle.left(120)
    koch_edge(depth, size)
    turtle.left(120)
    koch_edge(depth, size)
    #turtle.left(120)

    
def koch_edge(depth, size):
    """Draw an edge to given depth and size finishing in the same direction
    that we started in"""
    if depth == 0:
        turtle.forward(int(size))
    else:
        koch_edge(depth-1, size/3)
        turtle.right(60)
        koch_edge(depth-1, size/3)
        turtle.left(120)
        koch_edge(depth-1, size/3)
        turtle.right(60)
        koch_edge(depth-1, size/3)
       
koch(3, 200) 

