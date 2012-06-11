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
    sequence = [n, ]
    while n > 1 :
	if n < cBaseIndReps + CACHE_SIZE :
	  index = (cacheBaseInd + n - cBaseIndReps) % CACHE_SIZE
	  if cached[index] != 0 : # that number has a cycleLength already found
	    for w in range(len(sequence) - 1) :
	      if sequence[w + 1] < cBaseIndReps + CACHE_SIZE :
		cached[sequence[w + 1]] = cached[index] + w + 1
	    break
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
        sequence = [n, ] + sequence
    print sequence
    # now cache the sequence
    if n == 1 :
      for w in range(len(sequence)) :
	if sequence[w] < cBaseIndReps + CACHE_SIZE :
	  index = (cacheBaseInd + sequence[w] - cBaseIndReps) % CACHE_SIZE
	  cached [index] = w + 1 
    
    assert c > 0
    return c    



def cycle_length2 (n) :
    assert n > 0
    c = 1
    while n > 1 :
	# diagnostic prints
        print "smallerRngeLmt: ", smallerRngeLmt
        print "n: ", n
        
        if n < cBaseIndReps + CACHE_SIZE : 	# if "current < cBaseIndReps + CACHE_SIZE"
						# then n is cacheable
	  index = (cacheBaseInd + n - cBaseIndReps) % CACHE_SIZE
	  if cached[n - smallerRngeLmt] <= 0 :	
	    if (n % 2) == 0 :
	  
		n = (n / 2)
	    else :
		n = (3 * n) + 1
	    c += 1
	  else :
	    c += cached[n - smallerRngeLmt]
	    n = 1
    assert c > 0
    
    # calculate cached index from cacheBaseInd,
    # cBaseIndReps, and current
    if current < cBaseIndReps + CACHE_SIZE :
      index = (cacheBaseInd + current - cBaseIndReps) % CACHE_SIZE
      cached [index] = currentCycleLength
    
    return c 

#def threeToTwoCycle (n) :

  


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
      smallerRngeLmt = j
      current = j
      max = i
    cBaseIndReps = smallerRngeLmt
    maxCycleLength = 1
    currentCycleLength = 0
    index = 0
    # Progress to the 1st special-odd
    # A special-odd is one that you can subtract 2 
    # from its cycle to get the cycle_length of
    # a corresponding even
    # ergo--> "&& (current <= 1 || current % 4 != 1)"
    while current <= max && (current <= 1 || current % 4 != 1):
      currentCycleLength = cycle_length(current)
      # see if new maximum was found
      if currentCycleLength > maxCycleLength :
	maxCycleLength = currentCycleLength
      current = current + 1
      
    # current has is currently pointing to a special-odd
    while current + 3 <= max :
      currentCycleLength = cycle_length2(current)
      
      
      
      # see if new maximum was found
      if currentCycleLength > maxCycleLength :
	maxCycleLength = currentCycleLength
      current = current + 1
    
    
    # last 3 or fewer numbers to calculate
    while current <= max :
      currentCycleLength = cycle_length(current)
      
      
      
      # see if new maximum was found
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
    #a = [0, 0]
    while collatz_read(r, a) :
	smallerRngeLmt = a[0]
        v = collatz_eval(a[0], a[1])
        collatz_print(w, a[0], a[1], v)
        
        
        
import sys

#from Collatz import collatz_solve

# ----
# main
# ----
current = 0
cacheBaseInd = 0 	# going to create a looping array for a cache; 
			# this is the base of the array;
			# this is incremented when deleting cached values that 
			# are no longer necessary
			
cBaseIndReps = 0 	# the number corresponding to the cycle length
			# that's stored at the cache's base index
			# denoted by cacheBaseIndex
smallerRngeLmt = 0
a = [0, 0]
cached = [0, ]
h = [0, ]
CACHE_SIZE = 1000
for n in range(CACHE_SIZE): 	# setting up cache of size CACHE_SIZE
  cached += h			# with initial values of 0
print cached
collatz_solve(sys.stdin, sys.stdout)