#!/usr/bin/env python
# definite kill! double compile!


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

def generate_optimal_solution(num_items, capacity, min_value, max_value):
    opt = []
    for i in range(0, num_items):
        w = capacity / num_items # size
        v = random.randint(min_value, max_value) # value
        opt.append((w,v))
    print "generated optimal solution of %d items with total size %d and value %d"
            % (num_items, size_of_solution(opt), value_of_solution(opt))
    return opt

# writes randomly generated input to knapsack problem to stdout,
# optimal solution to stderr.
def generate_input(n=100, capacity=32):
    # strategy: define capacity of knapsack,
    # distribute capacity over m items and give those items a very high weight.
    # make sure those items are optimal by not giving any other item a higher weight.

    m = 4 # number of items in optimal solution.
    opt_min_weight, opt_max_weight = 10, 20
    
    # generate the optimal solution.
    opt = generate_optimal_solution(m, capacity, opt_min_weight, opt_max_weight)
    
    # generate n-m items that can not be part of the optimal solution.
    items = generate_random_items()
    
    

if __name__ == '__main__':
    generate_input(10)
