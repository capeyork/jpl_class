#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------
import sys

cache = [0] * 1000000

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a[0] = int(l[0])
    a[1] = int(l[1])
    assert a[0] > 0
    assert a[1] > 0
    return True

# ------------
# collatz_max_cycle
# ------------

def collatz_max_cycle (n) :

#   check for existing value
    if(cache[n] > 0):
        print("returning from cache")
        return cache[n]

#   initialize counter
    cycle = 1
    while n != 1:
        cycle += 1
        #print("n is currently")
        #print(n)
#       check if n is odd
        if(n % 2):
            #m = 3*n + 1 #initial solution
            m = n + (n>>1) + 1
            cycle += 1
        else:
            m = n/2
        n = m

#       store intermediate cycles to cache
        cache[n] = cycle

    print("new cache item stored")
    print(cache[n])
    return cycle
# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0

    collatz_max_cycle(10)
    assert cache[5] == 6
    # <your code>

#   initialize return value
    max_cycle = 1

#   set i,j in order
    #if(j<i):
        #j = i - j
        #i -= j
        #assert i <= j
    if(j<i):
        a = j
        b = i
    else:
        a = i
        b = j

    assert a <= b

#   take upper half by dividing b by 2 and use that when it makes sense (the range didn't get bigger)
    new = b >> 1
    if(new > a):
        a = new
    #print(a,b)

#   loop through all values between i,j
    for n in range(a,b+1):
        #print(n)
        m = collatz_max_cycle(n)
        if(m > max_cycle):
            max_cycle = m

    #assert collatz_max_cycle(22) == 16
    assert max_cycle > 0
    return max_cycle

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    a = [0, 0]
    while collatz_read(r, a) :
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)

collatz_solve(sys.stdin, sys.stdout)
