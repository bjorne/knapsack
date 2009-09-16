#!/usr/bin/env python

import sys
sys.path.append('lib')
from exhaust import Exhaust

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: knapsack input/knapsack.txt'
        sys.exit(1)
    filename = sys.argv.pop()
    solution, w, v = Exhaust().solve(filename)
    if solution != []:
        print "solution of weight %d, value %d found:" % (w,v)
        print ", ".join(map(lambda t: str(t), solution))
    else:
        print 'no solution found(!).'
