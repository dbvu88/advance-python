#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:38:59 2018

@author: duc
"""

from itertools import *

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# -------- chain ------------------------
for i in chain(a, b, c):
    print(i)
    
print(chain(a, b, c))

print(list(chain(a[2:], b[:5], c[2:7])))
# ---------------------------------------


# ----- count -------


    # count(start = 0, step = 1)
"""for i in count(1, .5):
    print(i)"""

"""for i in count():
    print(i)"""

    # islice(iterable, start, stop[, step])
for i in islice(count(), 0, 101, 5):
    print(i)
    
#---------------------
    
#------- compress ----------
    
binary_filter = [1,0,0,0,1,0,1,0,0,1,]
for i in compress(b, binary_filter):
    print(i)
#---------------------------
    
#________ map, filter _________
    
evens = [x for x in a if x % 2 == 0]
print(evens)

odds = list(filter(lambda x: x % 2 == 1, a))
print(odds)
    
a = filter(lambda x: x % 2 == 1, a)
#_______________________________


    

    
