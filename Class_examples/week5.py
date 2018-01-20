
# print v. return?
# almost always return - print almost always (only) used for user interaction

# indentation - use to determine a block of code - everything after a :
# i.e. after a while, for, if, elif, else, ...
# at the same of greater indentation level is within the same block of code
# When the indentation level decreases then no longer in that block of code

# for v. while
# A rule of thumb: if you know before the loop how many iterations of the loop
# there will be then use a for loop. Otherwise use a while loop.
# EG. If you are processing the chars of a string or the elements of a list
# then you know how many elements there are so use a for loop.
# Don't write
# i = 0
# while i < len(text):
#    process(text[i])
#    i += 1
# Instead write
# for c in text:
#    process(c)
# and if you need the index as well write
# for i,c in enumerate(text):
#    process(c,i)
#
# On the other hand if you are doing an interaction with a user or you are
# simulating some sort of process/robot/game then you probably don't know
# how many steps there will be so you CAN'T use a for loop.
# So the pirate simulation is an example as we don't know how many coin tosses
# are needed. But we do know how many trials we do so we should be using a
# for loop for that


# lists are mutable
# run the code below in the simulator
# copy and paste from here
def list_eg(xs):
    for i, x in enumerate(xs):
        xs[i] = x*2

ys = [1,2,3,4]

print(list_eg(ys))
print(ys)
# to here

# objects are treated in an "interesting way" when treated as a boolean value
print("bool(0) =",bool(0))
print("bool(42) =",bool(42))
print("bool('') =",bool(''))
print("bool('Spam') =",bool('Spam'))
print("bool([]) =",bool([]))
print("bool([1,2]) =",bool([1,2]))
print("bool(None) =",bool(None))

x = 12
print("x % 3 or x % 5 == 0  =", x % 3 or x % 5 == 0)
print("x % 3 == 0 or x % 5 == 0  =", x % 3 == 0 or x % 5 == 0)

# Why exceptions?
# If you don't use exceptions then problems have to be dealt with at each
# level of function calls as below
def f1(a1):
    x = f2(a1)
    if x is None:
        return None
    return x + 1

def f2(a2):
    x = f3(a2)
    if x is None:
        return None
    return x + 1

def f3(a3):
    if a3 == 0:
        return None
    return 100 % a3

# If you do use exceptions - there are choices
# Here we choose to trap (catch) the exception in f1e
def f1e(a1):
    try:
        return 1+f2e(a1)
    except ValueError as e:
        print(str(e))
        return None

def f2e(a2):
    return f3e(a2) + 1

def f3e(a3):
    if a3 == 0:
        raise ValueError("Can't use 0")
    return 100 % a3
        


    
