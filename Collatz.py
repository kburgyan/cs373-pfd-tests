#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2011
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a reader
    a is an array on int
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
    
# -----------
# collatz_cycle_length
# ---------

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c    


# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i is the beginning of the range, inclusive
    j is the end of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    #assert i = j
    assert i > 0
    assert j > 0
    if i < j :
      current = i
      max = j
    else :
      current = j
      max = i
    maxCycleLength = 1
    currentCycleLength = 0
    while current <= max :
      currentCycleLength = cycle_length(current)
      if currentCycleLength > maxCycleLength :
	maxCycleLength = currentCycleLength
      current = current + 1
    # <your code>
    #v = 1
    assert maxCycleLength > 0
    return maxCycleLength

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end of the range, inclusive
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
        
        
        
import sys

#from Collatz import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)