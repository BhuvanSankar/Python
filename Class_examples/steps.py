
# 0. put pirate at start
# 1. flip a coin
# 2. move following rules
# 3. update number of tosses
# 4. if off plank add to number of trials; go to 1 unless finished
# 5. calcuate average

# represent pirate position? 0,1, 2 ..., end
# represent heads and tails?
#    0,1
#    True, False
#    even, odd
#    "head", "tail"
#    < 0.5  >= 0.5

#  Head = 1, Tail = 0

# how long is the plank?
# number of trials?

import random

def toss():
    """Return random 0 or 1

    toss() -> int
    """
    return random.randint(0,1)

def move(pos, ht):
    """Return the new position of the pirate given the current position
    and a coin toss

    move(int, int) -> int
    """
    if ht == 1:   # head
        return pos+1
    # tail
    if pos == 0:   
        return 0
    return pos-1

def trial(size):
    """Return the number of coin tosses for pirate to fall in drink

    trial(int) -> int
    """
    pos = 0
    count = 0
    while pos < size:
        count += 1  #  shorthand for count = count + 1
        pos = move(pos, toss())
    return count

def get_average(total_trials, size):
    """Return the average number of coin tosses for given number of trials
    and plank length

    get_average(int, int) -> float
    """
    total_tosses = 0
    num_trials = 0
    while num_trials < total_trials:
        total_tosses += trial(size)
        num_trials += 1
    return total_tosses/total_trials

        


    
