
#Author: Yoshiki Hoshinaga
#Date : June 6 2020
#
# Estimating pi
#

import random
import math

def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <=1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 2 BELOW. ###

#part 1

def for_pi(n):
    c=0
    pi=0
    for i in range(1,n+1):
        if throw_dart():
            c+=1
        pi=4*c/i
        print('{} hits out of {} throws so that pi is {}'.format(c,i,pi))
    return pi

for_pi(10)
print('')
#part 2
def while_pi(error):
    c=0
    n=0
    pi=0
    while abs(pi-math.pi)>error:
        if throw_dart():
            c+=1
        n+=1
        pi=4*c/n
        print('{} hits out of {} throws so that pi is {}'.format(c,n,pi))
    return n

while_pi(0.1)
