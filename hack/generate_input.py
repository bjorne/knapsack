#!/usr/bin/env python
# definite kill! double compile!

import sys, random

def size_of_solution(solution):
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



def generate_optimal_solution(num_items, capacity, min_value, max_value):
    opt = []
    for i in range(0, num_items):
        w = capacity / num_items # size
        v = random.randint(min_value, max_value) # value
        opt.append((w,v))
#    print >> sys.stderr, "generated optimal solution of %d items with total size %d and value %d" \
#            % (num_items, size_of_solution(opt), value_of_solution(opt))
    return opt

def generate_random_items(num_items, max_value_per_weight_ratio):
    items = []
    for i in range(0, num_items):
        v = random.randint(1, 4) # 0 and 10 are arbitrary values, mind.
        # now, pick w to assure value/weight < max_value_per_weight_ratio
        max_w = int(max_value_per_weight_ratio/v)
        w = random.randint(min(1,max_w), max_w)
        items.append((w,v))
#    print >> sys.stderr, "generated %d random items with total size %d and value %d" \
#            % (num_items, size_of_solution(items), value_of_solution(items))
    return items


# writes randomly generated input to knapsack problem to stdout,
# optimal solution to stderr.
#
# capacity - capacity of knapsack
# n - the number of items to generate.
# m - the number of items in generated optimal solution.
def generate_input(capacity=32, n=1000, m=8):

    # strategy:
    # define capacity of knapsack,
    # distribute capacity over m items and give those items a very high weight.
    # make sure those items are optimal by not giving any other item a higher weight.

    opt_min_weight, opt_max_weight = 10, 20
    
    # generate the optimal solution.
    # the optimal solution has value >= m*opt_min_weight
    # and value-per-weight >= (m*opt_min_weight) / capacity
    opt = generate_optimal_solution(m, capacity, opt_min_weight, opt_max_weight)
    
    min_opt_value = (m*opt_min_weight) / float(capacity)
    opt_value_per_weight = value_of_solution(opt) / float(size_of_solution(opt))
    
    # generate n-m items that can not be part of the optimal solution.
    items = generate_random_items(n-m, opt_value_per_weight)
    items += opt
    random.shuffle(items)
    
    print_input(items, capacity)
    print_optimal(opt)

if __name__ == '__main__':
    generate_input()
