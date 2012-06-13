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
    a[2] = int(l[2])
    assert a[0] > 0
    assert a[1] > 0
    return True


def lookForSpecialOdd(n, index):
  if n % 4 == 1 and n > 1 :	# if "n % 4 == 1 && n > 1" then n is a special odd
    #print "c"
    n2 = (n - 1) / 4 * 6 + 2	# calculate corresponding even
    if cacheBaseIndAndRep[1] <= n2 < cacheBaseIndAndRep[1] + CACHE_SIZE : # is n within cache range?
      #print "d"
      index3 =  (cacheBaseIndAndRep[0] + n2 - cacheBaseIndAndRep[1]) % CACHE_SIZE
      cached[index3] = cached[index] - 2 # corresponding even is always minus 2
      
def cachePrevCycleNum(sequence, index) :
  for w in range(len(sequence) - 1) : # store the cycle_length for previous values of n
    #print "e"
    if cacheBaseIndAndRep[1] <= sequence[w + 1] < cacheBaseIndAndRep[1] + CACHE_SIZE : # is previous n within cache range?
      index2 = (cacheBaseIndAndRep[0] + sequence[w + 1] - cacheBaseIndAndRep[1]) % CACHE_SIZE
      #print "f"
      if index == -1 :
	#print "seq0: ", sequence[0]
	cached[index2] = baseCached[sequence[0] - 1] + w + 1
      else :
	cached[index2] = cached[index] + w + 1
      #****************************************************
      lookForSpecialOdd(sequence[w + 1], index2)
      #****************************************************
      
def cachePrevCycleNumAllSequence(sequence) :      
      for w in range(len(sequence) - 1) :
	#print "j"
	if cacheBaseIndAndRep[1] <= sequence[w + 1] < cacheBaseIndAndRep[1] + CACHE_SIZE :
	  #print "k"
	  index = (cacheBaseIndAndRep[0] + sequence[w + 1] - cacheBaseIndAndRep[1]) % CACHE_SIZE
	  cached [index] = w + 2 
	  lookForSpecialOdd(sequence[w + 1], index)
      
# -----------
# collatz_cycle_length
# ---------

def cycle_length (n) :
    assert n > 0
    c = 1
    originN = n
    if originN <= BASE_CACHE_SIZE :
      #print"baseCached"
      return baseCached[originN - 1]
    else: 
      if originN >= cacheBaseIndAndRep[1] + CACHE_SIZE : # is originN out of cache range?
	cacheBaseIndAndRep[1] += 1
	cached[cacheBaseIndAndRep[0]] = 0 # deleting old value
	if cacheBaseIndAndRep[0] < CACHE_SIZE - 1 :
	  cacheBaseIndAndRep[0] += 1
	else :
	  cacheBaseIndAndRep[0] = 0
    sequence = [n, ]
    #print "n: ", n
    while n > 1 :
	if n <= BASE_CACHE_SIZE :
	  #print"baseCached"
	  cachePrevCycleNum(sequence, -1)
	  c = cached[(cacheBaseIndAndRep[0] + originN - cacheBaseIndAndRep[1]) % CACHE_SIZE]
	  break # breaks out of the while loop
	else:
	    if cacheBaseIndAndRep[1] <= n < cacheBaseIndAndRep[1] + CACHE_SIZE : # is n within cache range?
	      #print "A"
	      index = (cacheBaseIndAndRep[0] + n - cacheBaseIndAndRep[1]) % CACHE_SIZE
	      if cached[index] != 0 : # number has a cycleLength already found?
		#print "b"
		#****************************************************
		lookForSpecialOdd(n, index)
		#****************************************************
		cachePrevCycleNum(sequence, index)
	    
		#print "h/i"
		c = cached[(cacheBaseIndAndRep[0] + originN - cacheBaseIndAndRep[1]) % CACHE_SIZE]
		break # breaks out of the while loop
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
        sequence = [n, ] + sequence
    #print sequence
    # now cache the sequence
    if n == 1 :
      #print "i"
      cachePrevCycleNumAllSequence(sequence)
      
    #for w in range(12):
      #print "w: ", w, "  cached[w]: ", cached[w]
    #print "c: ", c
    assert c > 0
    return c    


"""
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
"""
#def threeToTwoCycle (n) :

  
def cycle_length2 (n) :
    assert n > 0
    c = 1
    originN = n
    sequence = [n, ]
    #print "n: ", n
    while n > 1 :
	if n < bcacheBaseIndAndRep[1] + BASE_CACHE_SIZE : # is n within cache range?
	  #print "A"
	  index = (n - bcacheBaseIndAndRep[1]) % BASE_CACHE_SIZE
	  if baseCached[index] != 0 : # number has a cycleLength already found?
	    #print "b"
	    #****************************************************
	    if n % 4 == 1 and n > 1 :	# if "n % 4 == 1 && n > 1" then n is a special odd
	      #print "c"
	      n2 = (n - 1) / 4 * 6 + 2	# calculate corresponding even
	      if n2 < bcacheBaseIndAndRep[1] + BASE_CACHE_SIZE : # is n within cache range?
		#print "d"
		index3 =  (n2 - bcacheBaseIndAndRep[1]) % BASE_CACHE_SIZE
		baseCached[index3] = baseCached[index] - 2 # corresponding even is always minus 2
	    #****************************************************
	    for w in range(len(sequence) - 1) : # store the cycle_length for previous values of n
	      #print "e"
	      if sequence[w + 1] < bcacheBaseIndAndRep[1] + BASE_CACHE_SIZE : # is previous n within cache range?
		index2 = (sequence[w + 1] - bcacheBaseIndAndRep[1]) % BASE_CACHE_SIZE
		#print "f"
		baseCached[index2] = baseCached[index] + w + 1
		
	    #****************************************************
	        if sequence[w + 1] % 4 == 1 and sequence[w + 1] > 1 :	# if "n % 4 == 1 && n > 1" then n is a special odd
		  #print "g"
		  n2 = (sequence[w + 1] - 1) / 4 * 6 + 2	# calculate corresponding even
		  if n2 < bcacheBaseIndAndRep[1] + BASE_CACHE_SIZE : # is n within cache range?
		    #print "h"
		    index3 =  (n2 - bcacheBaseIndAndRep[1]) % BASE_CACHE_SIZE
		    baseCached[index3] = baseCached[index2] - 2 # corresponding even is always minus 2
	    #****************************************************
		
	    #print "h/i"
	    c = baseCached[(originN - bcacheBaseIndAndRep[1]) % BASE_CACHE_SIZE]
	    break # breaks out of the while loop
        if (n % 2) == 0 :
            n = (n / 2)
        else :
            n = (3 * n) + 1
        c += 1
        sequence = [n, ] + sequence
    #print sequence
    # now cache the sequence
    if n == 1 :
      #print "i"
      for w in range(len(sequence) - 1) :
	#print "j"
	if sequence[w + 1] < bcacheBaseIndAndRep[1] + BASE_CACHE_SIZE :
	  #print "k"
	  index = (sequence[w + 1] - bcacheBaseIndAndRep[1]) % BASE_CACHE_SIZE
	  baseCached [index] = w + 2 
	  if sequence[w + 1] % 4 == 1 and sequence[w + 1] > 1 :	# if "n % 4 == 1 && n > 1" then n is a special odd
	    #print "L"
	    n2 = (sequence[w + 1] - 1) / 4 * 6 + 2	# calculate corresponding even
	    if n2 < bcacheBaseIndAndRep[1] + BASE_CACHE_SIZE : # is n2 within cache range?
	      #print "m"
	      index3 =  (n2 - bcacheBaseIndAndRep[1]) % BASE_CACHE_SIZE
	      baseCached[index3] = baseCached[index] - 2 # corresponding even is always minus 2
    #for w in range(12):
      #print "w: ", w, "  cached[w]: ", cached[w]
    #print "c: ", c
    #for n in range(10) :
     # print "bcache[", BASE_CACHE_SIZE - 1 - n, "]: ", baseCached[BASE_CACHE_SIZE - 1 - n]
    assert c > 0
    return c    
  
  
def collatz_setUpBaseCache () :
  collatz_evalBase()


def collatz_evalBase() :
    """
    i is the beginning of the range, inclusive
    j is the end of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    #assert i = j
    current = 1 
    max = BASE_CACHE_SIZE
    maxCycleLength = 1
    while current <= max :
      currentCycleLength = cycle_length2(current)
      
      
      
      # see if new maximum was found
      if currentCycleLength > maxCycleLength :
	#print "******************************************************** max at: ", current
	#print smallerRngeLmt
	maxCycleLength = currentCycleLength
      current = current + 1
    # <your code>
    #v = 1
    assert maxCycleLength > 0
    print "maxCycleLength: ", maxCycleLength
    return maxCycleLength


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
      smallerRngeLmt = i
      current = i
      max = j
    else :
      smallerRngeLmt = j
      current = j
      max = i
      
    half = max//2
    print "half: ", half
    if current < half :
      current = half
    print "current: ", current
    cBaseIndReps = smallerRngeLmt
    maxCycleLength = 1
    currentCycleLength = 0
    index = 0
    
    """
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
      specialOdd = true
      currentCycleLength = cycle_length2(current)
      
      
      
      # see if new maximum was found
      if currentCycleLength > maxCycleLength :
	maxCycleLength = currentCycleLength
      current = current + 1
    """
    
    # last 3 or fewer numbers to calculate
    cacheBaseIndAndRep[1] = current
    while current <= max :
      currentCycleLength = cycle_length(current)
      #print "current: ", current
      
      
      # see if new maximum was found
      if currentCycleLength > maxCycleLength :
	#print "******************************************************** max at: ", current
	#print smallerRngeLmt
	maxCycleLength = currentCycleLength
      current = current + 1
    for y in range(CACHE_SIZE) :
      cached[y] = 0
    # <your code>
    #v = 1
    assert maxCycleLength > 0
    return maxCycleLength

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    prints the values of i, j, and vgit 
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
	collatz_evalBase()
        v = collatz_eval(a[0], a[1])
        
        if v != a[2] :
	  print "****************************************************************************"
	  print "Wrong: For i: ", a[0], "   and j: ", a[1], "*********************************************************"
	  print " should be: ", a[2], "  but calculates: ", v, "*********************************************************"
	  print "****************************************************************************"
	assert a[2] == v
        collatz_print(w, a[0], a[1], v)
        
        
        
import sys

#from Collatz import collatz_solve

# ----
# main
# ----

#specialOdd = false
current = 0
cacheBaseIndAndRep = [0, 1]
bcacheBaseIndAndRep = [0, 1]
#cacheBaseInd = 0 	# going to create a looping array for a cache; 
			# this is the base of the array;
			# this is incremented when deleting cached values that 
			# are no longer necessary
			
#cBaseIndReps = 0 	# the number corresponding to the cycle length
			# that's stored at the cache's base index
			# denoted by cacheBaseIndex
#smallerRngeLmt = 0
a = [0, 0, 0]
#a = [0, 0]
cached = [0, ]
baseCached = [0, ]
h = [0, ]
BASE_CACHE_SIZE = 4000
CACHE_SIZE = 10000
for n in range(CACHE_SIZE - 1): 	# setting up cache of size CACHE_SIZE
  cached += h			# with initial values of 0
for n in range(BASE_CACHE_SIZE - 1): 	# setting up cache of size CACHE_SIZE
  baseCached += h			# with initial values of 0
#print cached
print len(cached)
print len(baseCached)
collatz_solve(sys.stdin, sys.stdout)