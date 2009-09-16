#!/usr/bin/env python
# definite kill! double compile!

import sys, random

def weight_of_solution(solution):
    size = 0
    for item in solution:
        size += item[0]
    return size

def value_of_solution(solution):
    value = 0
    for item in solution:
        value += item[1]
    return value


def print_input(items, capacity):
    for item in items:
        print "(%d,%d)" % item
    print "capacity=%d" % capacity

def print_optimal(opt):
    for item in opt:
        print >> sys.stderr, "(%d,%d)" % item



def generate_optimal_solution(capacity):
    opt = []
    remaining_capacity = capacity
    min_size, max_size = 2, 12
    vpw_factor = 5 # value per weight factor.

    while remaining_capacity > 0:
        # size
        w = random.randint(min(min_size, remaining_capacity), min(max_size, remaining_capacity))
        remaining_capacity -= w
        # value
        v = random.randint(w*vpw_factor, (w*2)*vpw_factor)
        opt.append((w,v))
#    print >> sys.stderr, "generated optimal solution of %d items with total size %d and value %d" \
#            % (len(opt), weight_of_solution(opt), value_of_solution(opt))
    return opt

def generate_random_items(num_items, max_value_per_weight_ratio):
    items = []
    for i in range(0, num_items):
        v = random.randint(1, 4) # 0 and 10 are arbitrary values, mind.
        # now, pick w to assure value/weight < max_value_per_weight_ratio
        max_w = int(max_value_per_weight_ratio/v)
        w = random.randint(min(1,max_w), max_w)
        items.append((w,v))
    print >> sys.stderr, "generated %d random items with total size %d and value %d" \
            % (num_items, weight_of_solution(items), value_of_solution(items))
    return items


# writes randomly generated input to knapsack problem to stdout,
# optimal solution to stderr.
#
# capacity - capacity of knapsack
# n - the number of items to generate.
# m - the number of items in generated optimal solution.
def generate_input(capacity=32, n=1000):

    # strategy:
    # define capacity of knapsack,
    # distribute capacity over m items and give those items a very high weight.
    # make sure those items are optimal by not giving any other item a higher weight.

    # generate the optimal solution.
    opt = generate_optimal_solution(capacity)
    
    # generate items that can not be part of the optimal solution.
    opt_value_per_weight = value_of_solution(opt) / float(weight_of_solution(opt))
    items = generate_random_items(n-len(opt), opt_value_per_weight)
    items += opt
    random.shuffle(items)
    
    print_input(items, capacity)
    print_optimal(opt)

if __name__ == '__main__':
    generate_input()
