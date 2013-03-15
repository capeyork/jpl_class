#! /usr/bin/python
import math

def stddev (l, s):
    assert hasattr(l, '__iter__')

    n = s
    sum1 = 0
    sum2 = 0
 
#   iterate once to calculate mean
    for x in l:
        n = n + 1
        sum1 += x
 
#   calculate mean - but using s as a seed to ensure consistent data types (int, float, etc)
    mean = sum1/n
 
#   iterate again to sum the differences
    for x in l:
        sum2 += ((x - mean)*(x - mean)) / (n-1)
    sum2 = math.sqrt(sum2)

    return sum2

result = stddev([1,2,3,4,5], 0.0)
print(result)
